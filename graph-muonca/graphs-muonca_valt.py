#Gerador de gráficos para múltiplas tabelas quaisquer do Muonca
#A primeira coluna é o tempo, a segunda é a temperatura e a terceira, a pressão

import matplotlib.pyplot as plt
import numpy as np 
import time
from datetime import datetime, timezone
import sys
import os


# =============================================================================
# Importando dados
# =============================================================================
print ('''\nGerador de gráficos para múltiplas tabelas quaisquer do Muonca.
A primeira coluna é o tempo, a segunda é a temperatura e a terceira, a pressão.\n''')

#diga o nome do arquivo que deseja plotar como um argumento; deve estar no mesmo diretório
if ( len (sys.argv) ) == 1:
    print ('Se você deseja colocar o arquivo como parâmetro, tecle [1] e rode o programa novamente;\nSe deseja criar um gráfico com os PTmuonca.txt do diretório, tecle [Enter]')
    userInput = input()
    if userInput == '1':
        sys.exit('Por favor, insira o nome do arquivo como parâmetro')
    elif userInput != '1':
        userInput = 0        

#do jeito que está, é necessário lançar o nome de cada arquivo pra fazer o plot
tempo = []
temperatura = []
pressão = []

#se passou-se um parâmetro para o plot
if ( len (sys.argv) ) > 1:
    for i in range ( 1, len(sys.argv) ):
        file = sys.argv [i]
        tiempo, temperature, pressure = np.loadtxt( file, delimiter = ' ', unpack = True)
        tempo.extend(tiempo)
        pressão.extend(pressure)
        temperatura.extend(temperature)   
#se NÃO passou-se um parâmetro,
#lê-se todos os .txt's do diretório e colocar numa lista
elif ( len (sys.argv) ) == 1:
    path = '.' #você pode mudar o diretório aqui; 
    #se deixar assim, ele busca os que estão no mesmo local
    files = []
    # r=root, d=directories, f = files
    for r, d, f in os.walk(path):
        for file in f:
            if 'PTmuonca.txt' in file:
                files.append(os.path.join(file))    
    files.sort() #ordenar do menor dia para o maior
#    print (files)
    for i in range ( len(files) ):
        file = files[i]
        X, Y, Z = np.loadtxt( file, delimiter = ' ', unpack = True)
        tempo.extend(X)
        temperatura.extend(Y)
        pressão.extend(Z)
        
# =============================================================================
# Convertendo os dados 
# =============================================================================

#a ideia para converter o tempo é pegar o second a que se refere à meia-noite do dia 
#(que está relacionado com o primeiro elemento do dia), 
#subtrair o valor do tempo desse valor e converter para horas

#tempo[0] da lista de tempos, convertido para o formato de data e hora em GM00
#e depois como string (para nomear o plot)
tempo_0 = time.gmtime(tempo[0])
data_0 = str(tempo_0.tm_year) + ',' + str(tempo_0.tm_mon) + ',' + str(tempo_0.tm_mday)
print ('data_0 =', data_0)

#instante de época inicial do dia, em GM00
second_day_inicial = datetime (tempo_0.tm_year, tempo_0.tm_mon, tempo_0.tm_mday, 0, 0, 0, tzinfo=timezone.utc).timestamp() #AAAA,M,D,h,m,s; GM00
print ('second_day_inicial =', second_day_inicial)

tempo_em_dias = []
for i in range ( len(tempo) ): #converter para horas
    tempo_em_dias.append (   float ( "%.3f" % ( (tempo[i] - second_day_inicial) / (24*3600) )  )   )

#convertendo a pressão para mbar
for i in range ( len(pressão) ): #converter para mbar
    pressão[i] = pressão [i] /100    
    
# =============================================================================
# Plots
# =============================================================================
fig, ax1 = plt.subplots()

color = 'tab:green'
ax1.set_xlabel ('time (days)')
ax1.set_ylabel ('temperature(ºC)', color=color)
ax1.plot (tempo_em_dias,temperatura, color=color)
ax1.tick_params (axis='y', labelcolor=color)

ax2 = ax1.twinx()  # instantiate a second axes that shares the same x-axis

color = 'tab:blue'
ax2.set_ylabel ('pressure (mbar)', color=color)  # we already handled the x-label with ax1
ax2.plot (tempo_em_dias,pressão, color=color)
ax2.tick_params (axis='y', labelcolor=color)

#fig.tight_layout()  # otherwise the right y-label is slightly clipped

plt.title('Pressão e temperatura vs tempo; Muonca' + data_0)

plt.show()