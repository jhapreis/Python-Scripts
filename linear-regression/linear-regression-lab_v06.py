import sys
import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt

# =============================================================================
# REGRESSÃO LINEAR E PLOT COM INCERTEZAS (em andamento)
# =============================================================================

#   Diga o nome do arquivo que deseja plotar como um argumento;
#deve estar no mesmo diretório
if ( len (sys.argv) ) == 1:
    sys.exit('Por favor, insira o nome do arquivo como parâmetro')


#   Do jeito que está, é necessário lançar o nome de cada arquivo
#(no caso, do arquivo gerador)
elif ( len (sys.argv) ) > 1:
    file = sys.argv[1]
    data = pd.read_csv (file, sep=" ", header=None)
    data.columns = ['x', 'y', 'u_y', 'z' 'u_z'] #divide os imports em sub-listas
#   Primeiro a locação das sub-listas e depois as dos elementos; [coluna][linha]
#print (data)
#print (data['y'][7])
#print ( len(data['y']) )

#for i in range ( len( data['x'] ) ):
#    print (i)

n = []
m = []
u_m = []
l_2 = []
u_l_2 = []

for i in range ( len (data['x']) ):
    n.append ( data['x'][i] )
    print ( data['x'][i] )
    m.append ( data['y'][i] )
    u_m.append ( data['u_y'][i] )
    l_2.append ( data['z'][i] )
    u_l_2.append ( data['u_z'][i])

L_2 = [] #matriz dos comprimentos ao quadrado discretizados por n

for i in range ( len(n) ):
    if n == 1:
        L_2.append (l_2[i])
    if n == 2:
        L_2.append (l_2[i])
        

# =============================================================================
# Regressão linear com incertezas (bloco finalizado, mas não testado)
# =============================================================================

def linear_regression (X, Y, u_Y):
# f(x) = Ax + B; A = slope and B = linear coefficient
# w, wx, wy, wx², wxy
#   Para resolver a questão da regressão linear de incerteza nas duas variáveis,
# podemos escrever (y +/- u_y) = k·(x +/- u_x) como ( y +/- (u_y + k·u+x) ) = k·x    
    
    w = []
    wx = []
    wy = []
    wx2 = []
    wxy = []
    for i in range ( len (X) ):
        w.append ( 1 / u_Y[i]**2 )
        wx.append ( w[i]*X[i] )
        wy.append ( w[i]*Y[i] )
        wx2.append ( w[i]*X[i]**2 )
        wxy.append ( w[i]*X[i]*Y[i] )

    sum_w = sum (w)
    sum_wx = sum (wx)
    sum_wy = sum (wy)
    sum_wx2 = sum (wx2)
    sum_wxy = sum (wxy)        
    delta = sum_w*sum_wx2 - (sum_wx)**2
    
    A = ( sum_w*sum_wxy - sum_wx*sum_wy ) / delta
    u_a = ( sum_w / delta )**0.5
    B = ( sum_wy*sum_wx2 - sum_wxy*sum_wx ) / delta
    u_b = ( sum_wx2 / delta )**0.5

#    print ('pimba')
    return (A, u_a, B, u_b)
    
#print ( linear_regression( data['x'], data['y'] ) )
#print (A)

#for i in range ( len(n) ):
#    if n == 1:
#        

# =============================================================================
# Plotar pontos e reta pela equação regredida (corrigir as escritas)
# =============================================================================

for i in range ( len(n) ):
#    plt.errorbar(x[i], y[i], yerr=u_y[i], xerr=u_x[i], fmt='.k')
    plt.errorbar(m[i], L_2[i], xerr = u_m[i], yerr=u_l_2[i], fmt='.k')

    
# x-axis label 
plt.xlabel('Massa m do conjunto') 
# frequency label 
plt.ylabel('Comprimento ao quadrado L²') 
# plot title 
plt.title('Linearização: propagação de ondas') 

#setting the x - coordinates 
x_pred = np.arange(0, 100, 0.1) #gerar um conjunto de pontos para o plot
#setting the corresponding y - coordinates 

#y_pred = A*x_pred + B

#Precisamos traçar as retas mais acima e mais abaixo 
#e preencher a região de incerteza.
#Lembrando que u_a e u_b são > 0, sempre,
#e que A e B podem ter valores positivos ou negativos, tomamos os que dão
#o maior e o menor valor de A e B, respectivamente.

#y_high = max ( (A + u_a), (A - u_a) ) * x_pred + max ( (B + u_b), (B - u_b) ) 
#y_mid_1 = max ( (A + u_a), (A - u_a) ) * x + min ( (B + u_b), (B - u_b) )
#y_mid_2 = min ( (A + u_a), (A - u_a) ) * x + max ( (B + u_b), (B - u_b) )
#y_low = min ( (A + u_a), (A - u_a) ) * x_pred + min ( (B + u_b), (B - u_b) )

#plotting the curves 
#plt.plot(x_pred, y_pred, label='curve fit', color='black', linewidth=2)
#plt.plot(x_pred ,y_high, color='gray', linestyle='dashed', linewidth=0.5)
#plt.plot(x_pred ,y_low, color='gray', linestyle='dashed', linewidth=0.5)

#fill between
#plt.fill_between(x_pred, y_high, y_low, color='gray')

# show a legend on the plot 
plt.legend() 
#insere uma grade quadriculada
plt.grid()
#ajeita os valores máximo e mínimo de cada eixo
plt.xlim( [0, 0.2] )
plt.ylim( [0.55, 1.4] )
# function to show the plot 
plt.show() 
#save
#plt.savefig(format='png')
#acrescentar data e hora do pc

print ('Regressão linear concluída')

# =============================================================================
# PARA IMPLEMENTAR, AINDA FALTA
# =============================================================================
#   1) Melhorar a parte do plot
#   2) Fazer a gambiarra de ajeitar a incerteza do y combinando com o x. 
#Lembre-se de que o n não varia, porque foi discretizado. Isso requer uma
#mudança no código da propagação de incertezas, para colocar, também, essa gambiarra.