#linhas = int ( input () ) #número de linhas
#colunas = int ( input () ) #número de colunas
#
#matriz = []
#
#for i in range (0, linhas):
#    matriz.append ( [int(j) for j in input().split()] )

linhas = 3
colunas = 3
a0 = [1, 0, 0]
a1 = [0, 1, 0]
a2 = [0, 0, 1]
matriz = [ a0, a1, a2 ]
#print (matriz)
#inserir espa�adores dentro das matrizes?

borda_horizontal = ( 5 + 4*(colunas - 1) ) * '#'


#numero_elementos_linha = 2 bordas + n numeros + (n + 2 - 1) separadores = 2*n + 3
#numero_elementos_linha = 2*colunas + 3

#qual separado inserir?

linha0 = [ '# ', matriz[0][0], 'separar', matriz[0][1], 'separar', matriz[0][2],' #' ] 
linha2 = [ '# ', matriz[1][0], 'separar', matriz[1][1], 'separar', matriz[1][2],' #' ]
linha4 = [ '# ', matriz[2][0], 'separar', matriz[2][1], 'separar', matriz[2][2],' #' ]
linha_separadora = ['# ', 'separar', '', 'separar', ' ', 'separar', '#']

matriz_0 = [ linha0 , linha_separadora, linha2, linha_separadora, linha4 ]

#inserir separadores nas linhas  
for i in range ( 0, len(matriz_0), 2 ):
    for j in range ( 1, len(matriz_0[0]) - 3, 2 ):
        if matriz_0[i][j] == matriz_0[i][j+2]:
            matriz_0[i][j+1] = '   '
        else: 
            matriz_0[i][j+1] = ' | '

##linhas separadoras
for i in range ( 0, len(matriz_0) - 1, 2 ):
    for j in range ( 1, len (matriz_0[0]) - 1, 2 ):
        if matriz_0[i][j] == matriz_0[i+2][j]:
            print (i, j, matriz_0[i][j], matriz_0[i+2][j], matriz_0[i+1][j])
            matriz_0[i+1][j] = '   '
#        elif matriz_0[i-1][j] != matriz_0[i+1][j]:
        else:
            print (i, j, matriz_0[i][j], matriz_0[i+2][j], matriz_0[i+1][j])
            matriz_0[i+1][j] = '---'
#        print (i, j, matriz_0[i-1][j], matriz_0[i+1][j], matriz_0[i][j])
#        if matriz_0[]
    
print (len(matriz_0))
    
    
#printar cada linha de maneir adequada
print (borda_horizontal)       
for i in range ( len(matriz_0) ):
    for j in range ( len(matriz_0[0]) ): #print cada elemento conforme o indicado
        if j == len( matriz_0[0] ) - 1:
            print (matriz_0[i][j])
        else:
            print (matriz_0[i][j], end = '')
print (borda_horizontal)
