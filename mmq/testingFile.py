#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 19 15:20:22 2020

@author: jorgereis
"""

from mainFile import *
import matplotlib.pyplot as plt


# =============================================================================
# Dados
# =============================================================================

n_data = [100, 200, 400, 600, 800, 
          1000, 2000, 3000, 4000, 5000,
          6000, 7000, 8000, 9000, 10000]
t_data = [0.0003, 0.0014, 0.0043, 0.0126, 0.0244,
          0.0425, 0.2163, 0.5015, 0.9702, 1.6451,
          2.5825, 3.7516, 5.2557, 7.0075, 9.0550]











# =============================================================================
# Regressão usando linearização com ln
# =============================================================================

print('# =============================================================================')
print('ESTES SÃO OS VALORES PASSANDO POR UMA REGRESSÃO LINEAR')
print('# =============================================================================')

base = 2 #Y = A + b·X

# for i in range ( len(n_data) ):
#     print (n_data[i], t_data[i])

x_data , y_data = linearizaPorLog(n_data , t_data)
foi_linearizado = True

matrixF = MatrizPolinomialF(base, x_data)
# print( '\nThis is the polinomial-based matrice F: \n{}'.format(matrixF) )


C = resolveSistemaNormal(matrixF, y_data)


if foi_linearizado == True:
    coeff = DESlinearizaPorLog(C)
    print (f'\nCoeficientes deslinearizados: \n{coeff}\n')
else:
    coeff = C   
    

pts_na_função = []
for i in range( len(n_data) ):
    pts_na_função.append( coeff[0]*(n_data[i]**coeff[1])  )
delta_1 = resquicio(  t_data, pts_na_função  )
    


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
plt.plot(x, polinomioGrauN(x, C), color = 'dimgrey', label='função LINEARIZADA')



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

plt.title(f'Valores linearizados: \nY = { round(C[0],5) } + { round(C[1],5) }·X')
plt.legend()
plt.show()



# =============================================================================
# Plots função original após linearizar
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
    f'Valores do original pós-linearizar: \nt = { round( coeff[0]*(10**9) , 4) }· (n^{ round(coeff[1], 4) } ) E-9'
    )
plt.legend()
plt.show()













print('# =============================================================================')
print('AGORA, OS VALORES POR POLINÔMIO DE GRAU 3')
print('# =============================================================================')


# =============================================================================
# Regressão por polinômio de grau 3 
# =============================================================================

base = 4 #y = c_0 + c_1·x + c_2·x² + c_3·x³

matrixF = MatrizPolinomialF(base, n_data)
C = resolveSistemaNormal(matrixF, t_data)


pts_na_função = []
for i in range( len(n_data) ):
    pts_na_função.append( polinomioGrauN(n_data[i], C) )
delta_2 = resquicio(   t_data, pts_na_função  )




# =============================================================================
# Plot polinômio de grau 3
# =============================================================================

print('\nSeguem os gráficos... \n')

'''
Plot dos dados
'''
plt.scatter(n_data , t_data, color='black', label='linearizados')


'''
Plot da função encontrada mediante a base escolhida
'''
x = np.linspace(0,20000)
plt.plot(x, polinomioGrauN(x, C), color = 'dimgrey', label='função POLIMIAL')



'''
Alinhamento do gráfico
'''
x_min, x_max = 0, 12000
y_min, y_max = 0, 10
plt.axis([x_min, x_max,
          y_min, y_max])

cte = 10**12 # ajuste da função

plt.title(f'Valores por polinômio de grau 3: \nt = { round(cte*C[0]) } + { round(cte*C[1]) }·x + { round(cte*C[2]) }·x² + { round(cte*C[3]) }·x³ E-12')
plt.xlabel('número n de dimensões')
plt.ylabel('tempo t (em segundos)')
plt.legend()
plt.show()








delta = [delta_1 , delta_2]
print(f'Esses são os valores para os resíduos de a·x^b vs polinômio de grau 3 \n{delta}\n')








print('# =============================================================================')
print('FIIIIIIIMMMMMM')
print('# =============================================================================')
























