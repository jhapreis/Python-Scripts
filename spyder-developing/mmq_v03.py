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
    print ('\nOK! Você selecionou o método com polinômios. \n')
else:
    raise NameError ('Você selecionou um valor que eu não sei trabalhar com. Tente novamente.')    



# =============================================================================
# Def. das funções
# =============================================================================

# Linearização por ln
def linearizaPorLog(_x_data, _y_data):
    """
    No caso de uma função do tipo y = a·x^b, onde queremos encontrar a e b,
podemos simplesmente linearizar a equação para algo como
        ln y = ln a + b·ln x
    Daí, temos uma equação do tipo
        Y = A + b·X.
    """
    global _foi_linearizado
    _foi_linearizado = True
   
    print ('\nLinearizando os dados... \n')
    _X , _Y = [] , [] 
    _counter = 0
    for i in range(  len(_x_data)  ):
        if _x_data[i] == 0 or _y_data[i] == 0: # Existe um problema ao tentar calcular ln(0)
            _counter += 1
        else:
           _X.append( np.log(_x_data[i]) )
           _Y.append( np.log(_y_data[i]) )
    if _counter > 0:
        print(f'Encontramos dados {_counter} nulos. Como ln(0) não existe, ignoramos eles')

    return _X, _Y


# DES-linearização por ln
def DESlinearizaPorLog(_resultados):
    """
    Como usamos a linearização por ln, 
        y = a·x^b --> Y = A + b·X.
    Daí, o coeficiente A precisa ser reajustado como a = e^A.
    """
    # print(_resultados)
    _aux = [  np.e**_resultados[0] , _resultados[1] ]
    # print (_aux)
    
    return _aux


# Criação do da matriz-polinomial dado o espaço gerados de P_n
def MatrizPolinomialF(_base, _x_data):
    """
    Com a base polinomial P_n, a primeira coluna é preenchida com '1',
a segunda com x_i^1 = x_i e da terceira em diante, seguem-se as potências.    
    """
    print (f'\nConstruindo matriz polinomial F com base {_base}... \n')
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


# Criação do polinômio de grau n
def polinomioGrauN(_x_value, _base_coefficients):
    """
    Retorna um polinômio para '_x_values' dados os '_base_coefficients' 
    matriz de base = {1, x, x², ..., x^} 
    coeficientes da base = {c_0, c_1, ..., c_n} = [C]
    """
    _y = 0
    for i in range( len(_base_coefficients) ):
        if i > 0:
            _y += _base_coefficients[i]*(_x_value**i)
        elif i == 0:
            _y += _base_coefficients[0]
    return _y


# Criação da função para uma função de base exponencial
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


# Resolve o sistema normal, conhecida a matriz F
def resolveSistemaNormal(_Fmatrix, _y_data):
    """
    A ideia desse bloco é que possa ser aplicado a qualquer base que se escolha.
Isto é, ele resolve o sistema normal. A base que você usou antes é problema de outro método.
    
    Para resolver o sistema, precisamos elencar a matrizF transposta, já feita, de tal modo que
        matrizF^T · matrizF · C = matrizF^T · Y. 
    Daí, só precisamos montar a matriz Y a partir dos dados e resolver o sistema linear para C.  
    """
    print('\nResolvendo sistema normal... \n')
    
    _Y = np.array(_y_data).T   # cria o vetor-coluna com os dados de y
    _A = _Fmatrix.T @ _Fmatrix # cria a matriz-transposta da matrizF e faz produto matricial
    _B = _Fmatrix.T @ _Y
    _C = np.linalg.solve(_A, _B) # resolve o sistema linear
    _C = _C.tolist() # converte a solução para uma lista
    print('\nEsta é a solução do sistema: \n{} \n'.format(_C))
    
    return _C



# =============================================================================
# Dados
# =============================================================================

n_data = [100, 200, 400, 600, 800, 
          1000, 2000, 3000, 4000, 5000,
          6000, 7000, 8000, 9000, 10000]
t_data = [0.0003, 0.0014, 0.0043, 0.0126, 0.0244,
          0.0425, 0.2163, 0.5015, 0.9702, 1.6451,
          2.5825, 3.7516, 5.2557, 7.0075, 9.0550]
base = 2 #Y = a + b·x

# for i in range ( len(n_data) ):
#     print (n_data[i], t_data[i])

origData_x , origData_y = n_data , t_data
x_data , y_data = linearizaPorLog(n_data , t_data)








# =============================================================================
# Resolver sistema linear
# =============================================================================


matrixF = MatrizPolinomialF(base, x_data)
# print( '\nThis is the polinomial-based matrice F: \n{}'.format(matrixF) )


C = resolveSistemaNormal(matrixF, y_data)


if _foi_linearizado == True:
    coeff = DESlinearizaPorLog(C)
    print (f'\nCoeficientes deslinearizados: \n{coeff}\n')
else:
    coeff = C







# =============================================================================
# Plots linearizados
# =============================================================================

print('\nSeguem os gráficos... \n')

'''
Plot dos dados
'''
plt.scatter(x_data , y_data, color='black', label='linearizados')


'''
Plot da função encontrada mediante a base escolhida
'''
x = np.linspace(-100,100)
plt.plot(x, polinomioGrauN(x, C), color = 'dimgrey', label='função linearizada')



'''
Alinhamento do gráfico
'''
# x_min, x_max = min(x_data), max(x_data)
# y_min, y_max = min(y_data), max(y_data)
# plt.axis([x_min, x_max,
#           y_min, y_max])
x_min, x_max = 4 , 10
y_min, y_max = -10, 5
plt.axis([x_min, x_max,
          y_min, y_max])

plt.title(f'Valores linearizados: Y = { round(C[0],5) } + { round(C[1],5) }·X')
plt.legend()
plt.show()



# =============================================================================
# Plots função original
# =============================================================================

'''
Plot dos dados ORIGINAIS (pontos experimentais)
'''
plt.scatter(n_data , t_data, color = 'black', label='dados originais')

'''
Plot da função encontrada mediante a base escolhida
'''
x = np.linspace(0,20000)
y = coeff[0]*(x**coeff[1])
plt.plot(x, y, color = 'dimgrey', label = 'função t(n)=a·n^b')

'''
Alinhamento do gráfico
'''
x_min, x_max = 0, 12000
y_min, y_max = 0, 10
plt.axis([x_min, x_max,
          y_min, y_max])

plt.xlabel('número n de dimensões')
plt.ylabel('tempo t (em segundos)')
plt.title(
    f'Valores linearizados: t = { round( coeff[0]*(10**9) , 4) }· (n^{ round(coeff[1], 4) } ) E-9\n'
    )
plt.legend()
plt.show()



# # =============================================================================
# # Comparando com o esperado
# # =============================================================================
# '''
# Plot dos dados ORIGINAIS (pontos experimentais)
# '''
# plt.scatter(n_data , t_data, color = 'black', label='pontos experimentais')

# '''
# Plot da função encontrada mediante a base escolhida
# '''
# x = np.linspace(0,20000)
# y = coeff[0]*(x**coeff[1])
# plt.plot(x, y, color = 'dimgrey', label='função encontrada pelo MMQ')

# '''
# Plot da função ESPERADA: t(n) = 2/3·k·n³
# '''
# k = 3/2 * coeff[0] 
# z = (k)*(x**3)
# plt.plot(x, z, color = 'mediumvioletred', label=f'função esperada: t(n) = {round(k*10**9,3)}·n^3 E-9\n')

# '''
# Alinhamento do gráfico
# '''
# # x_min, x_max = 0, 12500
# # y_min, y_max = 0, 5
# # plt.axis([x_min, x_max,
# #           y_min, y_max])

# plt.xlabel('número n de dimensões')
# plt.ylabel('tempo t (em segundos)')
# plt.title(f'Valores para comparação dos resultados \n')
# plt.legend()
# plt.show()