# -*- coding: utf-8 -*-
"""
Created on Tue Sep  8 22:23:13 2020

@author: jhapr
"""

#%% Imports

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


#%% NOTAS EM GERAL
notas = pd.read_csv("aula0/ml-latest-small/ratings.csv")

'''
Daqui, temos um df com as notas
'''

# notas.rating.mean()
# notas.rating.median()

# notas.rating.plot()
# notas.rating.plot(kind='hist')

# notas.rating.describe()
# sns.boxplot(notas.rating)


#%% NOTAS POR FILME ESPECÍFICO
filmes = pd.read_csv("aula0/ml-latest-small/movies.csv")

# 1 = Toy Story
# notas.rating[notas.movieId == 1]
# notas.rating[notas.movieId == 1].mean()

# Para fazer todos os filmes, agrupamos e calculamos a media 
# notas.groupby('movieId')
# notas.groupby('movieId').rating.mean()
# # ou notas.groupby('movieId').mean()['rating'] , mas eu prefiro o primeiro jeito

# notas.groupby('movieId').rating.mean().plot(kind='hist')
# sns.boxplot( notas.groupby('movieId').rating.mean() )
# sns.distplot( notas.groupby('movieId').rating.mean() )
# plt.hist( notas.groupby('movieId').rating.mean() ) 

'O Pandas e o Seaborn utilizam o matplotlib.pyplot para gerar os gráficos'


#%% TMDB - The Movie Data Base
tmdb = pd.read_csv("bundle_archive/tmdb_5000_movies.csv")

# tmdb.original_language.unique()
# tmdb['original_language'].value_counts()
# tmdb['original_language'].value_counts().to_frame().reset_index()
# sns.barplot(x = 'index' , y = 'original_language' , data = tmdb['original_language'].value_counts().to_frame().reset_index())

'''
    Plot categórico (o mais simples é o gráfico de barras)
    
    É interessante transformar de um series em um df para que tenhamos 
dois eixos para o plot
    
    Podemos fazer isso em mais alto nível, utilizando uma função mais direta do 
Seaborn: 'sns.catplot'
'''

# sns.catplot(x = 'original_language' , kind = 'count', data = tmdb)

'''
Separando inglês vs o resto das línguas
'''

# tmdb['original_language'].value_counts().loc["en"]
# tmdb['original_language'].value_counts().sum()
# print( tmdb['original_language'].value_counts().loc["en"] , 
#       tmdb['original_language'].value_counts().sum() - tmdb['original_language'].value_counts().loc["en"] )
# dados = {
#     'lingua' : ['ingles', 'outros'],
#     'total'  : [ tmdb['original_language'].value_counts().loc["en"],
#                 tmdb['original_language'].value_counts().sum() - tmdb['original_language'].value_counts().loc["en"] ]}

# dados = pd.DataFrame(dados)
# sns.barplot(x = 'lingua' , y = 'total' , data = dados)

'''
    Podemos ainda gerar um gráfico com os valores das outras línguas que
não inglês
'''
# tmdb.query("original_language != 'en'")
# sns.catplot(x = 'original_language' , kind = 'count', data = tmdb.query("original_language != 'en'") )

''' 
e também podemos ordenar pelos de maior valor
'''
# sns.catplot(  x = 'original_language' , kind = 'count', data = tmdb.query("original_language != 'en'"),
#             aspect = 2, 
#             order =  tmdb.query(" original_language != 'en' ").original_language.value_counts().index,
#             palette = "GnBu_d"  )


#%% Estatística e etc

# round ( notas.rating[notas.movieId == 1].mean() , 2 )
# round ( notas.rating[notas.movieId == 2].mean() , 2 )
# plt.boxplot([ notas.rating[notas.movieId == 1],
#              notas.rating[notas.movieId == 2] ])
# notas.rating[notas.movieId == 1].std()
# notas.rating[notas.movieId == 2].std()