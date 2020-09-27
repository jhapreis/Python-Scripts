#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd


# # Seja $C ∈ R^ {n×n}$, tal que $c_{ij} = 0$ sempre que $i \not \in (j, j + 3)$.

# ## 1. Dê um exemplo de uma matriz não nula $C$ que se encaixa na definição acima, para $n = 7$. Onde podem aparecer elementos não nulos em $C$?
# 
# Uma matriz 7x7. As entradas são $0$ toda vez que $i\neq j$ ou que $i \neq j + 3$.

# In[2]:


# Fazendo manualmente:

matriz = {'Indexing': [1, 2, 3, 4, 5, 6, 7], # O 'indexing' aqui é só para começar a contar as linhas a partir do 1.
          '1': ['a', 0, 0, 'b', 0, 0, 0],
          '2': [0, 'c', 0, 0, 'd', 0, 0],
          '3': [0, 0, 'e', 0, 0, 'f', 0],
          '4': [0, 0, 0, 'g', 0, 0, 'h'],
          '5': [0, 0, 0, 0, 'i', 0, 0],
          '6': [0, 0, 0, 0, 0, 'j', 0],
          '7': [0, 0, 0, 0, 0, 0, 'k'],}
df_matriz = pd.DataFrame(matriz)
df_matriz.set_index('Indexing', inplace=True)
C = df_matriz
#print(C, '\n')


# In[6]:


# Fazendo com loops que substituem o resultado:

C = np.zeros([7,7])
counter = 0
for i in range ( len(C) ):
    for j in range( len(C[0]) ):
        counter += 1
        if (i==j) or (i==j+3):
            C[i][j] = counter # Esse valor aqui é só para diferenciar dos zeros.
print('Matriz C =','\n', C, '\n')


# ## 2. Compute o produto de $y = Cx$, com a matriz $C$ do item anterior e o vetor $x = (1, −1, 1, −1, 1, −1, 1)$. Observe quais elementos de $C$, contribuem para o cálculo de cada elemento do vetor $y$. 

# In[4]:


# Contruindo a função:

X = np.array([ [1], [-1], [1], [-1], [1], [-1], [1] ]) # Matriz-coluna

def product_mtrcol (A, B): # Produto matriz & matriz-coluna
    # A must be a  matrix (n x n) and B, a column vector (n x 1). The result is a matrix element (n x 1)
    product_mtrcol = np.zeros( [len(A), 1] ) # len(A) = n
    for i in range ( len(A) ):
        element = []
        for j in range  ( len(A[0]) ):
            element.append ( A[i][j]*B[j] )
        product_mtrcol[i] = np.array(sum(element))
                
    return product_mtrcol


print( 'Resultado do produto C x X:','\n', product_mtrcol(C,X), '\n' )       


# In[5]:


# Usando a função de produto de matrizes do numpy:

X = np.array([ [1], [-1], [1], [-1], [1], [-1], [1] ]) # Matriz-coluna
Y = np.dot(C, X)
#print(Y, '\n')


# ## 3. Quantas operações de ponto flutuante são necessárias para computar o produto $Y = CX$, no caso geral descrito no enunciado do exercício, ou seja, quando $C ∈ R^{ n×n }$?
# 
# No caso, cada elemento $y_{ij}$ é determinado pelo 'produto escalar' do vetor linha $C_{i}$ com o vetor coluna $X$.
# Tal operação traz consigo um produto para cada $n$ pares de elementos e também $n - 1$ somas (porque estamos somando $n$ termos -- ex: $a + b + c$ tem duas somas). 
# 
# Ou seja, para um vetor $C_{i_{1 \times n}} \times X_{n \times 1}$, temos que são feitos $n$ produtos e $n - 1$ somas dos resultados desses produtos. Portanto, $2n - 1$ flops. 
# 
# Mas esse é o resultado de cada um dos $n$ vetores-linha da matriz original $C_{n \times n}$. Portanto, se temos $2n - 1$ flops por linha, com $n$ linhas, teremos $n \cdot (2n - 1) = 2n² - n$ flops.
# 
print('Resposta: 2n² - n flops.')
