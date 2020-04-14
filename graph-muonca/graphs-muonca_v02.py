#Gerador de gráficos para uma tabela qualquer do Muoncq
#A primeira coluna é o tempo, a segunda é a temperatura e a terceira, a pressão

import matplotlib.pyplot as plt
import numpy as np 
from datetime import datetime, timezone

tempo, temperatura, pressão = np.loadtxt('190604003611PTmuonca.txt', delimiter = ' ', unpack = True)

#pegar o second a que se refere à meia-noite do dia, 
#subtrair o valor do tempo desse valor e converter para horas

tempo_0 = datetime (2019,6,4,0,0,0, tzinfo=timezone.utc).timestamp() #AAAA,M,D,h,m,s; GM00
#print (tempo_0)

tempo_em_horas = []
for i in range ( 0, len(tempo) ): #converter para horas
    tempo_em_horas.append (   float ( "%.3f" % ( (tempo[i] - tempo_0) / 3600 )  )   )
#print (tempo_em_horas)

# =============================================================================
# Plot 1: temperatura vs tempo
# =============================================================================

plt.plot (tempo_em_horas,temperatura, label = 'Temperatura')
plt.xlabel('tempo (h)')
plt.ylabel('temperatura (ºC)')
plt.title('Temperatura vs tempo; Muonca 04/06/2019')
plt.legend()
plt.show()

# =============================================================================
# Plot 2: pressão vs tempo
# =============================================================================

for i in range ( 0, len(pressão) ): #converter para mbar
    pressão[i] = pressão [i] /100
#print (pressão)

plt.plot (tempo_em_horas,pressão, label = '')
plt.xlabel('tempo (h)')
plt.ylabel('pressão (mbar)')
plt.title('Pressão vs tempo; Muonca 04/06/2019')
plt.legend()
plt.show()