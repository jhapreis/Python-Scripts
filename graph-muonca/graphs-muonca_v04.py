#Gerador de gráficos para uma tabela qualquer do Muoncq
#A primeira coluna é o tempo, a segunda é a temperatura e a terceira, a pressão

import matplotlib.pyplot as plt
import numpy as np 
import time
from datetime import datetime, timezone
import sys

#diga o nome do arquivo que deseja plotar como um argumento; deve estar no mesmo diretório
if ( len (sys.argv) ) == 1:
    sys.exit('por favor, insira o nome do arquivo como parâmetro')
file = sys.argv[1]
tempo, temperatura, pressão = np.loadtxt( file, delimiter = ' ', unpack = True)

#a ideia para converter o tempo é pegar o second a que se refere à meia-noite do dia 
#(que está relacionado com o primeiro elemento do dia), 
#subtrair o valor do tempo desse valor e converter para horas

#tempo[0] da lista de tempos, convertido para o formato de data e hora em GM00
#e depois como string (para nomear o plot)
tempo_0 = time.gmtime(tempo[0])
data_0 = str(tempo_0.tm_year) + ',' + str(tempo_0.tm_mon) + ',' + str(tempo_0.tm_mday)

#instante de época inicial do dia, em GM00
second_day_inicial = datetime (tempo_0.tm_year, tempo_0.tm_mon, tempo_0.tm_mday, 0, 0, 0, tzinfo=timezone.utc).timestamp() #AAAA,M,D,h,m,s; GM00

tempo_em_horas = []
for i in range ( 0, len(tempo) ): #converter para horas
    tempo_em_horas.append (   float ( "%.3f" % ( (tempo[i] - second_day_inicial) / 3600 )  )   )


#convertendo a pressão para mbar
for i in range ( 0, len(pressão) ): #converter para mbar
    pressão[i] = pressão [i] /100    

## =============================================================================
## Plot 1: temperatura vs tempo
## =============================================================================
#
#plt.plot (tempo_em_horas,temperatura, label = 'Temperatura')
#plt.xlabel('tempo (h)')
#plt.ylabel('temperatura (ºC)')
#plt.title('Temperatura vs tempo; Muonca' + data_0)
#plt.legend()
#plt.show()
#
## =============================================================================
## Plot 2: pressão vs tempo
## =============================================================================
#
#for i in range ( 0, len(pressão) ): #converter para mbar
#    pressão[i] = pressão [i] /100
#
#plt.plot (tempo_em_horas,pressão, label = '')
#plt.xlabel('tempo (h)')
#plt.ylabel('pressão (mbar)')
#plt.title('Pressão vs tempo; Muonca' + data_0)
#plt.legend()
#plt.show()
    
fig, ax1 = plt.subplots()

color = 'tab:green'
ax1.set_xlabel ('time (h)')
ax1.set_ylabel ('temperature(ºC)', color=color)
ax1.plot (tempo_em_horas,temperatura, color=color)
ax1.tick_params (axis='y', labelcolor=color)

ax2 = ax1.twinx()  # instantiate a second axes that shares the same x-axis

color = 'tab:blue'
ax2.set_ylabel ('pressure (mbar)', color=color)  # we already handled the x-label with ax1
ax2.plot (tempo_em_horas,pressão, color=color)
ax2.tick_params (axis='y', labelcolor=color)

#fig.tight_layout()  # otherwise the right y-label is slightly clipped

plt.title('Pressão e temperatura vs tempo; Muonca' + data_0)

plt.show()
