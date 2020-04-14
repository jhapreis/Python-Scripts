from uncertainties import ufloat
import numpy as np 
import sys
import time

# =============================================================================
# PROPAGAÇÃO DE INCERTEZAS PARA F 229: LAB 2
# =============================================================================

# =============================================================================
# Importando os dados
# =============================================================================

if ( len (sys.argv) ) == 1:
    sys.exit('Por favor, insira o nome do arquivo dos dados como parâmetro')

n = [] #sem unidades
m = [] #em g
u_m = [] #incertezas de m, em g
L = [] #em cm
u_L = [] #incertezas de L, em cm

#   Se passou-se um parâmetro para o plot,
if ( len (sys.argv) ) > 1:
    for i in range ( 1, len(sys.argv) ):
        file = sys.argv [i]
        N, M, u_M, l, u_l = np.loadtxt( file, delimiter = ' ', unpack = True)
        n.extend(N)
        m.extend(M)
        u_m.extend(u_m)
        L.extend(l)
        u_L.extend(u_l)
#   Do jeito que está, basicamente apenas os valores de L são utilizados

for i in range ( len(n) ):
    L[i] = ufloat ( L[i] , u_L [i] )

# =============================================================================
# Valores com incertezas
# =============================================================================

#f = 120 #em Hz
#g = 9.8 #em m/s²

# =============================================================================
# Propagando as incertezas
# =============================================================================

L_2 = []
for i in range ( len(n) ):
    L_2.append ( (L[i])**2 )

# =============================================================================
# Gerar arquivo de saída com os resultados
# =============================================================================

date = str ( round ( float (time.time()) ) )
file = open('incertezas' + date + '.txt', 'w')

file.write ('Valores de L² com incertezas \n')
for i in range ( len (n) ):
    file.write( str(L_2[i]) )
    file.write('\n')
file.write('\n')
file.write('\n')

file.write('fim')
file.close()

print ('Propagações de incertezas concluídas. \nCheque seu diretório.')