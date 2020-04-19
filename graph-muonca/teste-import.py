import sys
import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt

# =============================================================================
# TESTE PARA IMPORTAÇÃO DOS VALORES COM PANDAS (concluído)
# =============================================================================


#Diga o nome do arquivo que deseja plotar como um argumento;
#deve estar no mesmo diretório
if ( len (sys.argv) ) == 1:
    sys.exit('Por favor, insira o nome do arquivo como parâmetro')


#Do jeito que está, é necessário lançar o nome de cada arquivo
#(no caso, do arquivo gerador)
elif ( len (sys.argv) ) > 1:
    file = sys.argv[1]
    data = pd.read_csv (file, sep=" ", skiprows = [9, 19], header=None)
    data.columns = ['x', 'y'] #divide os imports em sub-listas
#Primeiro a locação das sub-listas e depois as dos elementos; [coluna][linha]
#print (data)
#print (data['y'][7])
#print ( len(data['y']) )

#for i in range ( len( data['x'] ) ):
#    print (i)

u = []
v = []
for i in range ( len (data['x']) ):
    u.append ( data['x'][i] )
#    print ( data['x'][i] )

# =============================================================================
# Split aos pares de contagem e pressão para cada um dos tipos
# =============================================================================



# =============================================================================
# Regressão linear
# =============================================================================

def linear_regression (X, Y):
#    f(x) = Ax + B
#    n, sum_x, sum_y, sum_xy, sum_x²
    n = len (X)
#    print (n)
    
    xy = []
    x_2 = []
    for i in range (n):
        xy.append (X[i] * Y[i])
        x_2.append ( (X[i])**2 )
        
    sum_x = sum (X)
#    print ('sum_x =', sum_x)
    sum_y = sum (Y)
#    print ('sum_y =', sum_y)
    sum_xy = sum (xy)
#    print ('sum_xy =', sum_xy)
    sum_x_2 = sum (x_2)
#    print ('sum_x² =', sum_x_2)
    delta = n*sum_x_2 - (sum_x)**2
    
    A = ( n*sum_xy - sum_x*sum_y ) / delta
    B = ( sum_y*sum_x_2 - sum_xy*sum_x ) / delta
    

#    print ('pimba')
    return ( A, B )
    


print ( linear_regression( data['x'], data['y'] ) )
#print (A)



##setting the x - coordinates 
#x_pred = np.arange(0, 100, 0.1) #gerar um conjunto de pontos para o plot
##setting the corresponding y - coordinates 
#y_pred = A*x_pred + B



## x-axis label 
#plt.xlabel('Eixo x') 
## frequency label 
#plt.ylabel('Eixo y') 
## plot title 
#plt.title('P L O T') 
## show a legend on the plot 
#plt.legend() 
##insere uma grade quadriculada
#plt.grid()
##ajeita os valores máximo e mínimo de cada eixo
#plt.xlim( [0, 10] )
#plt.ylim( [0, 10] )
## function to show the plot 
#plt.show() 
##save
##plt.savefig(format='png')
##acrescentar data e hora do pc
#
#

plt.scatter(  data['x'][1], data['y'][1], color='blue', alpha=0.5)
for i in range ( len(data['x']) ):
    plt.errorbar( data['x'][i], data['y'][i], fmt='.k')
plt.title('Scatter plot pythonspot.com')
plt.xlabel('x')
plt.ylabel('y')
plt.show()
    