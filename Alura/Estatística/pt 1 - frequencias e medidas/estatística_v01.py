# -*- coding: utf-8 -*-
"""
Created on Sat Sep 12 18:12:11 2020

@author: jhapr
"""

import pandas as pd
import numpy as np
import seaborn as sns
import scipy as sci


#%% CONHECENDO OS DADOS
dados = pd.read_csv( "Curso_de_Estatistica/dados.csv" )

'''
Qualitativos: ordinais vs nominais
Quantitativos: discretos vs contínuos
'''

dados['Sexo'].value_counts()
dados['Sexo'].value_counts(normalize=True) # para normalizar em 0 < x < 1

'''
Para criar um novo df a partir desses dados, podemos utilizar o recurso dos
DICIONÁRIOS Python
'''
distFreq_qualitativas = pd.DataFrame({ 'Frequência': dados['Sexo'].value_counts() , 
                                      'Percentual (%)': dados['Sexo'].value_counts(normalize=True) * 100 })

#%% DISTRIBUIÇÃO DE FREQUÊNCIAS
'''
Mudar o nome dos labels e da coluna dos índices
'''
distFreq_qualitativas.rename( index = {0: 'Masculino' , 1: 'Feminino'} , inplace = True )
distFreq_qualitativas.rename_axis( 'Sexo', axis = 'columns', inplace=True )

'''
Criar tabela com cruzamento de dados
'''
pd.crosstab(dados.Sexo , dados.Cor)



'''
Dividindo as variáveis por uma categorização específica
'''
classes = [0, 1576, 3152, 7880, 15760, 200000] #200.000 é o max
labels = ['E', 'D', 'C', 'B', 'A']

pd.cut( x = dados.Renda,
        bins = classes,
        labels = labels,
        include_lowest = True)

# podemos ordenar pela categoria
pd.value_counts( 
        pd.cut( x = dados.Renda,
               bins = classes,
               labels = labels,
               include_lowest = True)
        ).sort_index(ascending = False)

'''
Regra de Sturges:
    Número de classes/categorias quando não temos um valor já previamente definido
k = 1 + 10/3 log(n)
'''

n = dados.shape[0]
k = 1 + 10/3 * np.log10(n)

frequencia = pd.value_counts(
    pd.cut(
        x = dados.Renda,
        bins = 17, 
        include_lowest = True
        ),
    sort = False
    )

k = int(k.round())

'''
Histograma
'''
ax = sns.distplot(dados.Altura , kde = False, bins = k)


#%% Medidas de tendência central
'''
Média
    Obs.: cuidado com o que se está sendo calculado como média
'''
dados.Renda.mean()
dados.groupby( ['Sexo'] )['Renda'].mean() #dados.groupby( [agrupar por] )[agrupado]


'''
Mediana
    Dá pra calcular na mão, usando (n ou n+1) / 2 para achar a posição e 
usando o dados.loc[X - 1] -- python começa contando do zero
'''
dados.groupby(['Sexo'])['Renda'].median()


#-----------------
# dados.Renda.median?
# isso aqui te dá as descrições da função
#-----------------


'''
Moda
    É bastante utilizado em variáveis qualitativas, ou, de preferência, categóricas
'''
dados.Sexo.mode()


'''
Relações de simetria entre média, moda e mediana
    O deslocamento da média (u) e da moda (m) em relação à mediana (M) mostram desequilíbrio
nos dados. Acaba que os dados podem ser simétricos (u = m = M), assimétricos à direita (m < M < u)
ou asssimétricos à esquerda (u < M < m)
'''


#%% Medidas separatrizes

'''
Quartis
'''
dados.Renda.quantile()
dados.Renda.quantile([ i/10 for i in range(1,10) ])
dados.Renda.quantile([ i/100 for i in range(1,100) ])

# distribuição de frequência ACUMULADA
sns.distplot(dados.Idade,
             hist_kws={'cumulative':True},
             kde_kws ={'cumulative':True},
             bins = 10
             )

dados.Idade.quantile([ i/10 for i in range(1,10) ])


'''
Box plot
    Quartis, medianas e CANDIDATOS a outliers
'''
sns.boxplot(dados.Altura) #variável montada para ser simétrica
sns.boxplot(x = dados.Altura , y = dados.Sexo , orient = 'h')
# OU 
# sns.boxplot(x = 'Altura ', y = 'Sexo' , data = dados, orient = 'h'),
# passando o parâmetro 'dados'

# violentamente DISCREPANTE
sns.boxplot(x = dados.Renda , y = dados.Sexo , orient = 'h')
sns.boxplot(x = dados.Renda[dados.Renda < 10000] , y = dados.Sexo , orient = 'h')
# OU usando
# dados.query('Renda < 10000')



#%% Medidas de dispersão

'''
Desvio médio absoluto:
    1/n * SUM(|X_i - u|)
    É o total(soma) de desvios de cada valor em relação à média
'''
dados.Renda.mad()

'''
Variância:
    1/n * SUM( (X_i - u)^2 ); dados POPULACIONAIS
Variância amostral: correção de Bessel; variância AMOSTRAIS (uma amostra da população?)
    1/(n-1) * SUM( (X_i - u)^2 )
'''
dados.Altura.var() #variância amostral

'''
Desvio padrão: #amostral vs populacional
    Tira a raiz para resolver o problema da unidade de medida,
que deixa de estar ao quadrado
'''
dados.Altura.std() #desvio-padrão amostral