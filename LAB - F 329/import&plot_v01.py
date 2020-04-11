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

for i in range((len(f) - 1)):
    if ( f[i][2] == f[i+1][2] ) or ( f[i][2] != f[i+1][2] and f[i][2] == f[i-1][2] ):
        gg.append( [ f[i][2] ] ) 
        
        
print(gg)

# coord = []
# for i in f:
#     c = 0
#     for j in f:
#         if i[2] == j[2] and i != j:
#             c += 1
#             coord.append(i)
#             continue
# print(coord)









