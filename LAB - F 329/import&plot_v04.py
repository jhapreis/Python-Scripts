#Dados para importar e fazer plot dos dados

#imports
import matplotlib.pyplot as plt
# import numpy as np
import pandas as pd
from operator import itemgetter #para a ordenação dos valores

# =============================================================================
# Ler dados dos arquivos
# =============================================================================
file = pd.read_csv('dados dos potenciais/placas paralelas.txt', header=0, sep='	')
#---> Seria uma boa colocar para importar mais de um arquivo de uma vez e plotar todos em documentos separados
# print (file,'\n')



# =============================================================================
# Alocando os dados em listas (em uma matriz)
# =============================================================================
#Nesse documento, as colunas estão denominadas, respectivamente, 'X', 'Y' e 'Potencial'
data = [] #já conhecemos o número de colunas a ser tratado
for i in range (len(file)): 
#escreve as informações do file em listas, para melhor operação; 
#---> Acho que é possível mudar depois    
    data.append([file.loc[i, 'X'] , 
                 file.loc[i, 'Y'] , 
                 file.loc[i, 'Potencial'] ])
# print(data,'\n') 



# =============================================================================
# Ordenando os valores da matriz (segundo o elemento '2')
# =============================================================================
#Ordenando os elementos para depois procurar as equipotenciais
f = sorted(data, key=itemgetter(2), reverse=True)
# print(f,'\n')
     

  
# =============================================================================
# Encontrando e separando as equipotenciais
# =============================================================================
equipotenciais=[]
x = []
y = []
v = []
buffer = None
for i in range( len(f)  ):
    if i != len(f) - 1:
        if ( f[i][2] == f[i+1][2] ) or ( f[i][2] != f[i+1][2] and f[i][2] == f[i-1][2] ):
            if f[i][2] != buffer:
                equipotenciais.append( [f[i]] )
                x.append( [ f[i][0] ] )
                y.append( [ f[i][1] ] )
                v.append( [ f[i][2] ] )
                buffer = f[i][2]
            else:
                equipotenciais[len(equipotenciais) -1].append( f[i] )
                x[len(x) -1].append( f[i][0] )
                y[len(y) -1].append( f[i][1] )
                v[len(v) -1].append( f[i][2] )
    elif i == len(f) - 1: #comparar só o último, que não tem posterior
        if f[i][2] == f[i-1][2]:
            if f[i][2] != buffer:
                equipotenciais.append( [f[i]] )
                x.append( [ f[i][0] ] )
                y.append( [ f[i][1] ] )
                v.append( [ f[i][2] ] )
                buffer = f[i][2]
            else:
                equipotenciais[len(equipotenciais) -1].append( f[i] )
                x[len(x) -1].append( f[i][0] )
                y[len(y) -1].append( f[i][1] )
                v[len(v) -1].append( f[i][2] )
#   Apartamos os elementos que se repetem dos que não se repetem. A partir disso, escolhemos um elemento para ser comparado
# com o primeiro (o último, já que, por causa da ordenação, não é igual ao primeiro). Depois disso, comparamos esse elemento
# com o primeiro da lista: se ele se mostrar diferente, criamos uma nova lista, colocamos ele lá dentro e também atualizamos
# o buffer com esse valor (e repete); se forem iguais, ele adiciona na última sublista previamente criada.
# print(equipotenciais,'\n')
# for i in range (len (equipotenciais) ):
#     print (equipotenciais[i])
# print()




# =============================================================================
# 
# =============================================================================
cores = ['blue', 'pink', 'orange', 'red', 'brown', 'green', 'yellow', 'purple', 'black', 'violet', 'salmon', 'silver']
c = 0
# for conjunto in equipotenciais:
#     if len(conjunto) > 5:
#         for tripla in conjunto:
#             print(tripla)
#             # print(tripla[0], tripla[1])
#             plt.scatter(tripla[0], tripla[1], color=cores[c])
#             c += 1
# plt.xlabel('eixo x'), plt.ylabel('eixo y'), plt.title('nome do gráfico'), plt.ylim(0, 30), plt.xlim(0,40), plt.grid(True)
# plt.show()                 # exibe todos os desenhos, juntos


    

