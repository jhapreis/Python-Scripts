#Gerar um número aleatório

import numpy as np

def gerar_lista (x, y):
    lista = []
    i = 0
    for i in range (x, y):
        i += 1
        lista.append(i)
    return (lista)

n_from = int ( input('from:',) )
n_to = int ( input('to:',) )

numbers = gerar_lista (n_from , n_to)


#print (lista)
print ( np.random.choice(numbers) )