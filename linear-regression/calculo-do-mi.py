from uncertainties import ufloat
import time


#Valores [A, incerteza de A]
resultados = [ [25.705607535142747, 0.03934458646279381],
            [59.351704490253546, 0.06100617739378663],
            [109.05631407343822, 0.12129532383022192] ]

for i in range ( len(resultados) ):
    for j in range ( len(resultados[0]) ):
        resultados[i][j] = resultados[i][j] / 10000

f = 120
g = 9.8

A = []
µ = []

for i in range ( len(resultados) ):
    a = ufloat ( resultados[i][0], resultados[i][1] )
    A.append (a)
    µ.append ( (g*(i+2)**2) / (4*a*f**2) )
    
print (A)
print (µ)

# =============================================================================
# Gerar arquivo de saída com os resultados
# =============================================================================

date = str ( round ( float (time.time()) ) )
file = open('calculo-mi' + date + '.txt', 'w')

file.write ('Valores (A, incerteza de A)\n')
for i in range ( len (A) ): #descarta os valores de n = 1 e n = 5
    file.write( str(A[i]) )
    file.write('\n')
file.write('\n')
file.write('\n')

file.write ('Valores (µ, incerteza de µ)\n')
for i in range ( len (µ) ): #descarta os valores de n = 1 e n = 5
    file.write( str(µ[i]) )
    file.write('\n')
file.write('\n')
file.write('\n')

file.write ('Valor médio de µ\n')
µ_soma = 0
for i in range ( len(µ) ):
    µ_soma = µ_soma + µ[i]

file.write ( str( 0.3333333333*µ_soma) )

file.write('fim')
file.close()

print ('Cálculos concluídos. \nCheque seu diretório.')