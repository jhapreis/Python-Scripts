# -*- coding: utf-8 -*-
"""
Spyder Editor

Este é um arquivo de script temporário.
"""

#Plot de famílias de soluções de EDOs

import matplotlib.pyplot as plt
import numpy as np

# geramos um domínio das abcissas, só pra poder usá-las para os desenhos
x = np.arange(0, 10, 0.1) 
c = 0 # valor inicial da constante

for i in range (0, 10, 1): # ajustando o 'range', mudamos quantos membros da família aparecerão
    f_x = 2/3*np.cos(x) + 4/3*np.sin(x) + c*np.e**(-0.5*x)   # definimos qual a família de funções a ser desenhada
    plt.plot(x, f_x)       # adicione, ao gráfico, cada desenho (dentro do 'loop')
    c = c + 1              # adiciona o 'step' à constante

  
# function to show the plot 
plt.xlabel('eixo x')
plt.ylabel('eixo y') ##seria interessante conseguir escrever qual a função##
plt.grid(True)             # coloca a malha no desenho
plt.title('Famílias de funcções, a partir das constantes')
plt.show()                 # exibe todos os desenhos, juntos