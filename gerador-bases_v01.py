import numpy as np

#inserir comandos para o usuário dizer os parâmetros

variable = 2
individual = 4

lines = variable**individual

aux = []
for i in range (lines):
    aux.append(i)
    aux[i] = str( np.base_repr(aux[i] , 
                          base=variable, 
                          padding=0) )
    aux[i] = aux[i].zfill(individual)
    # print(aux[i])
print()

# =============================================================================
# os valores que saem daqui são strings, não números 
# =============================================================================

counting = 0
for i in range( len(aux) ):
    if aux[i].count('0') >= 2: #essa condicional é um exemplo
        print(aux[i])
        counting += 1
        

# print ( aux[0].count('0') )
    

print('\n', counting)