import matplotlib.pyplot as plt
import numpy as np 
import sys
import time

M = [111.8 ,214.8 ,94.3 ,161.8 ,58.8 ,111.8 ,214.8 ,94.3 ,161.8 ,58.8 ,111.8 ,94.3 ,161.8 ,58.8]

U_M = [0.09 ,0.09 ,0.09 ,0.09 ,0.09 ,0.09 ,0.09 ,0.09 ,0.09 ,0.09 ,0.09 ,0.09 ,0.09 ,0.09]

L_2 = [3422 ,6162 ,5776 ,4556 ,1764.0 ,1332.2 ,14161 ,2704 ,10000 ,3721 ,10712 ,10201 ,18632 ,6642]

U_L_2 = [5 ,6 ,6 ,5 ,3.4 ,2.9 ,10 ,4 ,8 ,5 ,8 ,8 ,11 ,7]

for i in range ( len(M) ):
    M[i] = M[i]
    U_M[i] = U_M[i]
    L_2[i] = L_2[i] / 10000
    U_L_2[i] = U_L_2[i] / 10000

A = [25.705607535142747, 59.351704490253546, 109.05631407343822]
U_A = [0.03934458646279381, 0.06100617739378663, 0.12129532383022192 ]
B = [767.9934094927876, -3164.9148427196474, -193.44768759681102]
U_B = [4.850407329713131, 6.779562549292077, 12.349559774093304 ]

for i in range ( len(A) ):
    A[i] = A[i] / 10000
    U_A[i] = U_A[i] / 10000
    B[i] = B[i] / 10000
    U_B[i] = U_B[i] / 10000

# =============================================================================
# Plotar pontos e reta pela equação regredida
# =============================================================================

for i in range ( len(M) ):
#    plt.errorbar(x[i], y[i], yerr=u_y[i], xerr=u_x[i], fmt='.k')
    plt.errorbar(M[i], L_2[i], xerr = U_M[i], yerr = U_L_2[i], fmt='.k', ecolor = 'green')
    
#setting the x - coordinates 
x_pred = np.arange(0, 500, 0.1) #gerar um conjunto de pontos para o plot

colors = [ 'blue', 'red', 'green']

for i in range ( len (A) ):
    #setting the corresponding y - coordinates 
    y_pred = A[i]*x_pred + B[i]
    
    #Precisamos traçar as retas mais acima e mais abaixo 
    #e preencher a região de incerteza.
    #Lembrando que u_a e u_b são > 0, sempre,
    #e que A e B podem ter valores positivos ou negativos, tomamos os que dão
    #o maior e o menor valor de A e B, respectivamente.
    y_high = max ( (A[i] + U_A[i]), (A[i] - U_A[i]) ) * x_pred + max ( (B[i] + U_B[i]), (B[i] - U_B[i]) ) 
    #y_mid_1 = max ( (A + u_a), (A - u_a) ) * x + min ( (B + u_b), (B - u_b) )
    #y_mid_2 = min ( (A + u_a), (A - u_a) ) * x + max ( (B + u_b), (B - u_b) )
    y_low = min ( (A[i] + U_A[i]), (A[i] - U_A[i]) ) * x_pred + min ( (B[i] + U_B[i]), (B[i] - U_B[i]) )
    
    #plotting the curves 
    plt.plot(x_pred, y_pred, label='n =' + str(i+2), color=colors[i], linewidth=2)
    #plt.plot(x_pred ,y_high, color='gray', linestyle='dashed', linewidth=0.5)
    #plt.plot(x_pred ,y_low, color='gray', linestyle='dashed', linewidth=0.5)
    
    #fill between
    #plt.fill_between(x_pred, y_high, y_low, color='gray')

# x-axis label 
plt.xlabel('Massa - em gramas') 
# frequency label 
plt.ylabel('Quadrado do comprimento - em m²') 
# plot title 
plt.title('Linearização: Propagação de ondas') 
# show a legend on the plot 
plt.legend() 
#insere uma grade quadriculada
plt.grid()
#ajeita os valores máximo e mínimo de cada eixo
plt.xlim( [0, 250] )
plt.ylim( [0, 2] )
# function to show the plot 
plt.show() 
#save
#plt.savefig(format='png')
#acrescentar data e hora do pc

print ('Regressão linear concluída')