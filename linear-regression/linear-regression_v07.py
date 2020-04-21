import numpy as np 
import sys
import time


## =============================================================================
## Importando e apresentando os dados dados
## =============================================================================
#
##Os dados são importados diretamente das tabelas repassadas a um arquivo txt,
##devidamente formatado. 
#
#if ( len (sys.argv) ) == 1:
#    sys.exit('Por favor, insira o nome do arquivo dos dados como parâmetro')
#
#n = []
#m = []
#l_2 = []
#u_l_2 = []
#
##se passou-se um parâmetro para o plot
#if ( len (sys.argv) ) > 1:
#    for i in range ( 1, len(sys.argv) ):
#        file = sys.argv [i]
#        X, Y, W, K = np.loadtxt( file, delimiter = ' ', unpack = True)
#        n.extend(X)
#        m.extend(Y)
#        l_2.extend(W)
#        u_l_2.extend(K)

M = [ [111.8 ,214.8 ,94.3 ,161.8 ,58.8] , [111.8 ,214.8 ,94.3 ,161.8 ,58.8] , [111.8 ,94.3 ,161.8 ,58.8] ]

U_M = [ [0.09 ,0.09 ,0.09 ,0.09, 0.09], [0.09 ,0.09 ,0.09, 0.09 , 0.09] , [0.09 ,0.09 ,0.09 ,0.09] ]

L_2 = [ [3422 ,6162 ,5776 ,4556 ,1764.0] , [1332.2 ,14161 ,2704 ,10000 ,3721] , [10712 ,10201 ,18632 ,6642] ]

U_L_2 = [ [5 ,6 ,6 ,5 ,3.4] , [2.9 ,10 ,4 ,8 ,5] , [8 ,8 ,11 ,7] ]

for i in range ( len(M) ):
    if i != 2:
        for j in range ( len(M[0]) ):
#            M[i][j] = M[i][j] / 10
#            U_M[i][j] = U_M[i][j] / 10
            L_2[i][j] = L_2[i][j] / 10000
            U_L_2[i][j] = U_L_2[i][j] / 10000
    elif i == 2:
         for j in range ( len(M[2]) ):
#            M[i][j] = M[i][j] / 10
#            U_M[i][j] = U_M[i][j] / 10
            L_2[i][j] = L_2[i][j] / 10000
            U_L_2[i][j] = U_L_2[i][j] / 10000

#L_2 = [ [], [], [], [] ] #matriz dos comprimentos ao quadrado discretizados por n
#U_L_2 = [ [], [], [], [] ]
#M = [ [], [], [], [] ]
#
#for i in range ( len(n) ):
#    if n[i] == 1:
#        L_2[0].append (l_2[i])
#        U_L_2[0].append (u_l_2[i])
#        M[0].append (m[i])
#    if n[i] == 2:
#        L_2[1].append (l_2[i])
#        U_L_2[1].append (u_l_2[i])
#        M[1].append (m[i])
#    if n[i] == 3:
#        L_2[2].append (l_2[i])
#        U_L_2[2].append (u_l_2[i])
#        M[2].append (m[i])
#    if n[i] == 4:
#        L_2[3].append (l_2[i])
#        U_L_2[3].append (u_l_2[i])
#        M[3].append (m[i])
#        
#print (L_2)
#print (U_L_2)
#print (M)


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
        w.append ( 1 / (u_Y[i]**2) )
        wx.append ( w[i]*X[i] )
        wy.append ( w[i]*Y[i] )
        wx2.append ( w[i]*(X[i]**2) )
        wxy.append ( w[i]*X[i]*Y[i] )

    sum_w = sum (w)
#    print (sum_w)
    sum_wx = sum (wx)
    sum_wy = sum (wy)
    sum_wx2 = sum (wx2)
    sum_wxy = sum (wxy)        
    delta = sum_w*sum_wx2 - (sum_wx)**2
#    print (delta)
    
#    global A, u_a, B, u_b
    A = ( sum_w*sum_wxy - sum_wx*sum_wy ) / delta
    if (sum_w / delta) > 0:
        u_a = ( sum_w / delta )**0.5
    elif (sum_w / delta) < 0:
        u_a = ( (-1)*sum_w / delta )**0.5
    B = ( sum_wy*sum_wx2 - sum_wxy*sum_wx ) / delta
    if (sum_wx2 / delta) > 0:
        u_b = ( sum_wx2 / delta )**0.5
    elif (sum_wx2 / delta) < 0:
        u_b = ( (-1)*sum_wx2 / delta )**0.5
#    u_b = ( sum_wx2 / delta )**0.5

#    print ('pimba')
    return ( [A, u_a, B, u_b] )
    
#print ( linear_regression( data['x'], data['y'] ) )
#print (A)

#for i in range ( len(n) ):
#    if n == 1:


# =============================================================================
# Gerar arquivo de saída com os resultados
# =============================================================================

valores = []

for i in range ( len (M) ):
    valores.append ( linear_regression(M[i], L_2[i], U_L_2[i]) )
#valores.append ( linear_regression(m, l_2, u_l_2) )

#print (valores)

date = str ( round ( float (time.time()) ) )
file = open('regressão' + date + '.txt', 'w')

file.write ('Valores [A, incerteza de A, B, incerteza de B]\n')
for i in range ( 1, len (M) ): #descarta os valores de n = 1 e n = 5
    file.write( str(valores[i]) )
    file.write('\n')
file.write('\n')
file.write('\n')

file.write('fim')
file.close()

print ('Regressões lineares concluídas. \nCheque seu diretório.')