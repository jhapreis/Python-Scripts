#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun  3 00:04:23 2020

@author: jorgereis
"""
# =============================================================================
# Imports
# =============================================================================

import numpy as np


# =============================================================================
# Dados do problema
# =============================================================================

# dados do receptor
data_x = [47.0, 90.0, 140.0, 190.0] #km
data_y = [102.0, 43.0, 101.0, 47.0] #km
data_t = [465.15, 301.04, 236.67, 297.21] #micro sec,

# velocidade da luz
# c = 300000 #300,000 km/s
# print(c)


# =============================================================================
# 
# =============================================================================


'''
CORRIGIR: TRATAR XY COMO COORDENADAS 'ABSOLUTAS' DO DESENHO
'''


# def distance_xy(x_coordinates, y_coordinates):
#     distance_xy = []
#     for i in range ( len(x_coordinates) ):
#         aux = None # provavelmente é uma linha desnecessária
#         # d = sqrt(x² + y²)
#         aux = np.sqrt(  (x_coordinates[i])**2 + (y_coordinates[i])**2  )
#         distance_xy.append(aux)
#     # print('distâncias calculadas por xy: {} \n'.format(distance_xy))
#     return distance_xy # retorna uma lista

def distanceSquared_xy(x_coordinates, y_coordinates):
    distance_xy = []
    for i in range ( len(x_coordinates) ):
        aux = None # provavelmente é uma linha desnecessária
        # d = sqrt(x² + y²)
        aux = (x_coordinates[i])**2 + (y_coordinates[i])**2
        distance_xy.append(aux)
    # print('distâncias calculadas por xy: {} \n'.format(distance_xy))
    return distance_xy # retorna uma lista

def distance_ct(delta_t):
    # velocidade da luz
    c = 0.3 #300,000 km/s = 0.3 km/micro-s  
    distance_ct = []
    for i in range ( len(delta_t) ):
        aux = None # provavelmente é uma linha desnecessária
        # d = c·delta_t
        aux = c*delta_t[i]
        distance_ct.append(aux)
    print('distâncias calculadas por vel·tempo: {} \n'.format(distance_ct))
    return distance_ct
    # retorna uma lista
        

def C_constants(x_coordinates, y_coordinates, delta_t):
    R = distance_ct(delta_t) # é uma lista com as distâncias (os raios)
    C = []
    for i in range ( len(x_coordinates) ):
        aux = None # provavelmente é uma linha desnecessária
        aux = (R[i])**2 - (distanceSquared_xy(x_coordinates, y_coordinates))[i]
        C.append(aux)
    # print ('valores das constantes C: {} \n'.format(C))
    return C
    # retorna uma lista
    
    
    
    
        
# =============================================================================
# 
# =============================================================================

C = C_constants(data_x, data_y, data_t)



# =============================================================================
# Resolver o sistema
# =============================================================================

'''
Resolver o seguinte sistema  linear: \n
[ (x_1 - x_2)   (y_1 - y_2) ]   [x]   =   [(C_2 - C_1)/2] 
[ (x_2 - x_3)   (y_2 - y_3) ]   [y]       [(C_3 - C_2)/2]

Usarei uma função do numpy, mas a solução analítica se encontra no texto.
'''



A = np.array([  [  data_x[0] - data_x[1] , data_y[0] - data_y[1] ],
                [  data_x[1] - data_x[2] , data_y[1] - data_y[2] ]   ])

B = np.array(   [  (C[1] - C[0])/2 , (C[2] - C[1])/2  ]   )


X = np.linalg.solve(A, B)

# print('Solução do sistema linear: {}. Essa solução foi identificada como {}'.format(
    # X, np.allclose( np.dot(A, X), B )))








# =============================================================================
# Resultados
# =============================================================================
''' O resultado para os dados das linhas 1, 2, 3 foi [170.54626072  50.96973509]
    2, 3, 4: [139.72965282  77.53577639]
    1, 3, 4: [171.14469126 106.62377494]
    1, 2, 4: [141.63512751  29.89890919]
'''

resultados = ( [170.54626072 , 50.96973509], 
               [139.72965282 , 77.53577639],
               [171.14469126 , 106.62377494],
               [141.63512751 , 29.89890919] )
              
def média_xy(result):
    aux_1, aux_2 = 0, 0
    media = []    
    for i in range (len(result)):
        aux_1 += result[i][0]
        aux_2 += result[i][1]
    aux_1 = aux_1 / len(result)
    aux_2 = aux_2 / len(result)
    media = [aux_1, aux_2]
    return media


print ( média_xy(resultados) )

