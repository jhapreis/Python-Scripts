import matplotlib.pyplot as plt
import numpy as np 
import sys


# =============================================================================
# Importando e apresentando os dados dados
# =============================================================================

#Os dados são importados diretamente das tabelas repassadas a um arquivo txt,
#devidamente formatado. 

if ( len (sys.argv) ) == 1:
    sys.exit('Por favor, insira o nome do arquivo dos dados como parâmetro')

x = []
u_x = []
y = []
u_y = []
#se passou-se um parâmetro para o plot
if ( len (sys.argv) ) > 1:
    for i in range ( 1, len(sys.argv) ):
        file = sys.argv [i]
        X, U_X, Y, U_Y = np.loadtxt( file, delimiter = ' ', unpack = True)
        x.extend(X)
        u_x.extend(U_X)
        y.extend(Y)
        u_y.extend(U_Y)

#print ('x =', x)
#print ('y =', y)
#print ('u_y =', u_y)

# =============================================================================
# Cálculo dos coeficientes angular e linear 
# =============================================================================

#Função: y_i = a*x_i + b 
#T²·D = 4·pi²/g · D² + 4·pi²/g·k

#Incerteza reescrita: w_i = 1 / u_i²
#Esse valor corresponde à incerteza de y;
#nada é dio sobre a incerteza de x, ignorada.
w = []
for i in range ( len(y) ):
   w.append( 1 / (u_y[i])**2 )
#print ('w =', w)

#Termos para o cálculo da regressão linear, numa caso geral 
#(incerteza podendo ser diferente)
wx = [] #wx
wy = [] #wy
wxy = [] #wxy
wx_2 = [] #wx²
for i in range ( len(y) ):
    wx.append ( w[i]*x[i] )
    wy.append ( w[i]*y[i] )
    wxy.append ( w[i]*x[i]*y[i] )
    wx_2.append ( w[i]*( (x[i])**2 ) )
#print ('wx =', wx)
#print (wy)
#print (wxy)
#print (wx_2)
sum_w = np.sum(w)
sum_wx = np.sum(wx)
sum_wy = np.sum(wy)
sum_wxy = np.sum(wxy)
sum_wx_2 = np.sum(wx_2)
delta = sum_w * sum_wx_2 - (sum_wx)**2

#Coeficiente angular:
A = ( ( sum_w * sum_wxy ) - ( sum_wx * sum_wy ) ) / delta 
u_a = np.sqrt ( sum_w / delta )
print ('A =', A, '+/-', u_a)

#Coeficiente linear:
B = ( ( sum_wy * sum_wx_2 ) - ( sum_wxy * sum_wx ) ) / delta
u_b = np.sqrt ( sum_wx_2 / delta )
print ('B =', B, '+/-', u_b)

# =============================================================================
# Plotar pontos e reta pela equação regredida
# =============================================================================

for i in range ( len(w) ):
#    plt.errorbar(x[i], y[i], yerr=u_y[i], xerr=u_x[i], fmt='.k')
    plt.errorbar(x[i], y[i], xerr = u_x[i], yerr=u_y[i], fmt='.k')

    
# x-axis label 
plt.xlabel('Eixo x -- D²') 
# frequency label 
plt.ylabel('Eixo y -- D·T²') 
# plot title 
plt.title('Linearização: pêndulo físico') 

#setting the x - coordinates 
x_pred = np.arange(0, 100, 0.1) #gerar um conjunto de pontos para o plot
#setting the corresponding y - coordinates 
y_pred = A*x_pred + B

#Precisamos traçar as retas mais acima e mais abaixo 
#e preencher a região de incerteza.
#Lembrando que u_a e u_b são > 0, sempre,
#e que A e B podem ter valores positivos ou negativos, tomamos os que dão
#o maior e o menor valor de A e B, respectivamente.
y_high = max ( (A + u_a), (A - u_a) ) * x_pred + max ( (B + u_b), (B - u_b) ) 
#y_mid_1 = max ( (A + u_a), (A - u_a) ) * x + min ( (B + u_b), (B - u_b) )
#y_mid_2 = min ( (A + u_a), (A - u_a) ) * x + max ( (B + u_b), (B - u_b) )
y_low = min ( (A + u_a), (A - u_a) ) * x_pred + min ( (B + u_b), (B - u_b) )

#plotting the curves 
plt.plot(x_pred, y_pred, label='curve fit', color='black', linewidth=2)
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