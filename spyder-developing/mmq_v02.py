#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 18 18:48:50 2020

@author: jorgereis
"""

# =============================================================================
# Imports e interface com o usuário
# =============================================================================
import numpy as np
import matplotlib.pyplot as plt

# userInput = input (
# 'Qual a base que você quer que eu use? \nPor favor, selecione dentre exp.[1], trig.[2] ou polin.[3] \n'
                   # )

userInput = '3'

IMpossible_values = ['1', '2', 'e', 'E', 't', 'T']
possible_values = ['3', 'p', 'P']

if userInput in IMpossible_values:
    raise NameError ('Ainda não sei fazer assim desse jeito, sorry :/')
elif userInput in possible_values:
    print ('OK! Você selecionou o método com polinômios. \n')
else:
    raise NameError ('Você selecionou um valor que eu não sei trabalhar com. Tente novamente.')    



# =============================================================================
# Def. das funções
# =============================================================================

def linearizaPorLog(_x_data, _y_data):
    """
    No caso de uma função do tipo y = a·x^b, onde queremos encontrar a e b,
podemos simplesmente linearizar a equação para algo como
        ln y = ln a + b·ln x
    Daí, temos uma equação do tipo
        Y = A + b·X.
    """
    print ('\nLinearizando os dados... \n')
    _X , _Y = [] , [] 
    _counter = 0
    for i in range(  len(_x_data)  ):
        if _x_data[i] == 0 or _y_data[i] == 0:
            _counter += 1
        else:
           _X.append( np.log(_x_data[i]) )
           _Y.append( np.log(_y_data[i]) )
    if _counter > 0:
        print(f'Encontramos dados {_counter} nulos. Como ln(0) não existe, ignoramos eles')

    return _X, _Y



def polinomialF(_base, _x_data, _y_data):
    """
    Com a base polinomial P_n, a primeira coluna é preenchida com '1',
a segunda com x_i^1 = x_i e da terceira em diante, seguem-se as potências.    
    """
    print ('\nConstruindo matriz polinomial F \n')
    _null_matrix = np.zeros(   (  len(_x_data) , _base  )   )
    
    for i in range( len(_null_matrix[0]) ):
        if i == 0:
            _null_matrix[:,i] = 1
        elif i == 1:
            _null_matrix[:,i] = np.array(_x_data)
        else:
            _aux = np.zeros(   ( len(_x_data) , 1)   ) # vetor-coluna nulo
            for j in range ( len(_x_data) ):
                _aux[j] = _x_data[j]**i        
            _null_matrix[:,i] = _aux[:,0]
    
    return _null_matrix



def polinomioGrauN(_x_value, _base_coefficients):
    """
    Retorna um polinômio para '_x_values' dados os '_base_coefficients' 
    matriz de base = {1, x, x², ..., x^} 
    coeficientes da base = {c_0, c_1, ..., c_n} = [C]
    """
    _y = 0
    for i in range( len(_base_coefficients) ):
        if i > 0:
            print (_base_coefficients[i])
            _y += _base_coefficients[i]*(_x_value**i)
        elif i == 0:
            _y += _base_coefficients[0]
    return _y



def exponencialOrdemN(_x_value, _base_coefficients):
    pass
    """
    Retorna uma função que é CL das exponenciais para '_x_values' dados os '_base_coefficients' 
    matriz de base = {e^-kx , ... , e^-x , 1 , e^x , ... , e^kx} 
    coeficientes da base = {c_0, c_1, ..., c_n} = [C]
    """
    pass
'''
Estou tendo problemas para firmar um termo geral para as bases trig. e exp.
'''
    





# =============================================================================
# Dados
# =============================================================================
x_data = [1, 2, -1, -2]
y_data = [5, 7,  1, -1]
# y = 2x + 3

base = 2 #Y = a + b·x




# =============================================================================
# Resolver sistema linear
# =============================================================================


matrixF = polinomialF(base, x_data, y_data)
# print( '\nThis is the polinomial-based matrice F: \n{}'.format(matrixF) )

"""
Para resolver o sistema, precisamos elencar a matrizF transposta, de tal modo que
matrizF^T · matrizF · C = matrizF^T · Y. 
Daí, só precisamos resolver o sistema linear para C.  
"""

Y = np.array(y_data).T # cria o vetor-coluna com os dados de y
# print(Y)

A = matrixF.T @ matrixF # cria a matriz-transposta da matrizF e faz produto matricial
# print('\n', A, '\n')

B = matrixF.T @ Y

C = np.linalg.solve(A, B) # resolve o sistema linear
C = C.tolist() # converte a solução para uma lista
# print('\nEsta é a solução do sistema: \n{} \n'.format(C))





# =============================================================================
# Plots
# =============================================================================

'''
Plot dos dados
'''
plt.scatter(x_data , y_data)


'''
Plot da função encontrada mediante a base escolhida
'''
x = np.linspace(-100,100)
plt.plot(x, polinomioGrauN(x, C))



'''
Alinhamento do gráfico
'''
x_min, x_max = 1.1*min(x_data), 1.1*max(x_data)
y_min, y_max = 1.1*min(y_data), 1.1*max(y_data)
plt.axis([x_min, x_max,
          y_min, y_max])

plt.show()







