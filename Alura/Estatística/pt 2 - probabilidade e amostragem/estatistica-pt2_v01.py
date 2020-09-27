# -*- coding: utf-8 -*-
"""
Created on Sat Sep 19 02:29:13 2020

@author: jhapr
"""

import numpy as np
import pandas as pd
import seaborn as sns
from scipy.special import comb
from scipy.stats import binom, poisson, norm


dados = pd.read_csv('dados.csv')


#%% Binomial
# P(X = x) = Comb(n, x)*p^x*(1-p)^n-x
# Eventos independentes, com dois resultados possíveis

comb(25, 20)
1/ comb(25, 20)

'''Probabilidade de o candidato tirar 5'''
binom.pmf(5, 10, 1/3)

'''P (X >= 5)'''
binom.pmf( [i for i in range(5,10)], 10, 1/3 ).sum()
1 - binom.cdf(4, 10, 1/3) # total - acumulado até 4
binom.sf(4, 10, 1/3) # idem, mas condensado


#%% Poisson
# P(X = x) = e^(-u) * u^x / x!
# Não tem como prever insucessos

'''Probabilidade de receber 15 dado que, em média, recebe 20 por hora'''
poisson.pmf(15, 20)



#%% Normal
'''   
    Teorema do limite central: aumentando o tamanho da amostra, nos aproximamos
de uma dist. normal 
'''
x = 1.8 # valor da variável de valor superior/inferior
u = 1.7
sigma = 0.1
Z = (x - u) / sigma

'''
    Para consultar a tabela padronizada, calculamos o Z e somamos linha com coluna
a fim de encontrar a probabilidade da variável padronizada
'''
norm.cdf(Z) # calcular a probabilidade para a variável padronizada Z
norm.cdf( (1.8 - 1.7) / 0.1 ) - norm.cdf( (1.6 - 1.7) / 0.1 ) # prob. num intervalo
1 - norm.cdf(2) # ter mais de 1,90 m
# OU
# norm.cdf(-2)


#%% Amostragem
'''
Seleção aleatória para amostra
'''
dados.sample(n = 100 , random_state = 101)
dados.Sexo.value_counts(normalize = True)
dados.sample(n = 100, random_state=101).Sexo.value_counts(normalize = True)
# os valores são bem parecidos


#%% Estimação
'''
    Parâmetros da população com base numa amostra
    
    Teorema do limite central:
        incerteza = sigma / raiz(n)
'''

n = 2000 # tamanho total
total_de_amostras = 1500

amostras = pd.DataFrame()

for i in range(total_de_amostras):
    _ = dados.Idade.sample(n)
    _.index = range( len(_) )
    amostras[ 'Amostra_' + str(i) ] = _
    
    
amostras.mean() 
# comparar com
dados.Idade.mean()

amostras.mean().std()
# comparar com 
dados.Idade.std() / np.sqrt(n)

sns.distplot( amostras.mean() )


#%% Intervalos de confiança
'''
    Na distribuição normal, podemos querer encontrar qual a probabilidade de
um determinado valor estar dentro de um intervalo dado.
Acabamos por usar essa questão dos intervalos de confiança justamente por isso:
Definimos uma probabilidade P com a qual queremos garantir que o valor esteja
dentro de um intervalo que comporte essa probabilidade.

    Por exemplo, podemos pensar em encontrar o intervalo de confiança com
P = 0.95. Com esse valor, encontramos z (a variável normalizada) que dá essa
probabilidade (em torno da média, sempre). No caso, z = 1,96.

    Conhecido o z, fazemos u = x_medio +/- z * sigma/raiz(n), [ou z*s/raiz(n)]
onde acabamos por encontrar o intervalo de confiança.
'''

#   para encontrar o valor de z, simétrico em relação a u,
# com probabilidade P:
# z = norm.ppf(P)
norm.ppf(0.5 + 0.99/2)

# norm.interval(alpha = alpha , loc = media , scale =  sigma / raiz(n))
# com alpha, ele calcula internamente o z
norm.interval(0.95 , 5050, 150/np.sqrt(20) )

'''
    Conhecendo o valor de erro máximo que queremos ter, juntamente com o
intervalo de confiança, podemos simplesmente inverter a ordem da equação
e calcular o tamanho da amostra necessária para garantir uma 
representatividade da população.
'''

media = 45.5
sigma = 15
significancia = 0.10
confianca = 1 - significancia

'''
    É importante ter em mente que z = norm.ppf(P) nos retorna o z que vem desde
o -inf. Daí, precisamos nos atentar em achar os z_sup e z_inf que, simetricamente,
dão a probabilidade. Por isso, fazemos z = norm.ppf( 0.5 + P/2 )
'''

z = norm.ppf(0.5 + (confianca / 2)) 
erro_percentual = 0.10
e = media * erro_percentual

n = (z * (sigma / e)) ** 2
n.round()

'''
Tamanho de amostra populacional finita
'''
# n = (z**2 * s**2 * N) / ( z**2 * s**2 + e**2 * (N-1) )