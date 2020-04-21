#Dados para importar e fazer plot dos dados

#imports
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from operator import itemgetter, attrgetter #para a ordenação dos valores

file = pd.read_csv('dados dos potenciais/placas paralelas.txt', header=0, sep='	')
#---> Seria uma boa colocar para importar mais de um arquivo de uma vez e plotar todos em documentos separados
# print (file)
print()


#Nesse documento, as colunas estão denominadas, respectivamente, 'X', 'Y' e 'Potencial'
data = [] #já conhecemos o número de colunas a ser tratado
for i in range (len(file)): 
#escreve as informações do file em listas, para melhor operação; 
#---> Acho que é possível mudar depois    
    data.append([file.loc[i, 'X'] , 
                 file.loc[i, 'Y'] , 
                 file.loc[i, 'Potencial'] ])
# print(data)
print()    


f = sorted(data, key=itemgetter(2), reverse=True)
# print(f)
print()

# lista = []
# for i in range(len(f)):
#     lista.append(f[i][2])
# print(lista)        

gg=[]
# buffer = f[len(f) - 1][2]
buffer = None
for i in range(  ( len(f) )  ):
    if i != len(f) - 1:
        if ( f[i][2] == f[i+1][2] ) or ( f[i][2] != f[i+1][2] and f[i][2] == f[i-1][2] ):
            if f[i][2] != buffer:
                gg.append( [f[i]] )
                buffer = f[i][2]
            else:
                gg[len(gg) -1].append( f[i] ) 
    elif i == len(f) - 1: #comparar só o último, que não tem posterior
        if f[i][2] == f[i-1][2]:
            if f[i][2] != buffer:
                gg.append( [f[i]] )
                buffer = f[i][2]
            else:
                gg[len(gg) -1].append( f[i] ) 

#   Apartamos os elementos que se repetem dos que não se repetem. A partir disso, escolhemos um elemento para ser comparado
# com o primeiro (o último, já que, por causa da ordenação, não é igual ao primeiro). Depois disso, comparamos esse elemento
# com o primeiro da lista: se ele se mostrar diferente, criamos uma nova lista, colocamos ele lá dentro e também atualizamos
# o buffer com esse valor (e repete); se forem iguais, ele adiciona na última sublista previamente criada.

print(gg)


#AJUSTAR NOMES DE VARIÁVEIS







