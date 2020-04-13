numero_times = int ( input() )

numero_partidas = numero_times * (numero_times - 1) - 1 #número total até agora; combinação. fatorial

dados_partida = []
for i in range (numero_partidas): #falta uma partida
    dados_partida.append ( input().split() )

times_em_casa = []
em_casa = []
for i in range (len(dados_partida)):
    times_em_casa.append(dados_partida[i][0])
for i in range (len(times_em_casa)):
    em_casa.append(times_em_casa.count(dados_partida[i][0])) 
if len(times_em_casa) > 1:
    meu_time = times_em_casa[em_casa.index( min(em_casa) )]
else:
    meu_time = dados_partida[0][3]

times_fora = []
fora = []
for i in range (len(dados_partida)):
    times_fora.append(dados_partida[i][3])
for i in range (len(times_fora)):
    fora.append(times_fora.count(dados_partida[i][3]))
if len(times_fora) > 1:
    meu_time_adversario = times_fora[fora.index( min(fora) )]
else: meu_time_adversario = dados_partida[0][0]
    
print ( meu_time, '10', 'x', meu_time_adversario, '0' )

dados_partida.append([meu_time, '10', 'x', meu_time_adversario, '0'])

#a1 = ['Araguaia', '3', 'x', 'Cascavel', '0']
#a2 = ['Cascavel', '10', 'x', 'Araguaia', '0']
#
#numero_times = 2
#
#dados_partida = [a1, a2]

# =============================================================================
# 1. Lista com nomes dos times
# =============================================================================

times = []
for i in range(len (dados_partida) ):
    times.append ( dados_partida[i][0] )
times.sort()
#print(times)
nome_times = []
for i in range (0, len(times), numero_times):
    if len(times) - numero_times == i:
        nome_times.append(times[i+(int(len(times)/numero_times))])
    nome_times.append(times[i])
#    print (i)    
nome_times.sort()
#print (nome_times)

# =============================================================================
# 2. Vitórias
# =============================================================================
vitorias = []
empates = []
#danem-se as derrotas
for i in range ( len (dados_partida) ):
    
    if dados_partida[i][1] > dados_partida[i][4]:
        vitorias.append(dados_partida[i][0])        
    elif dados_partida[i][4] > dados_partida[i][1]:
        vitorias.append(dados_partida[i][3])
        
    elif dados_partida[i][1] == dados_partida[i][4]:
        empates.append(dados_partida[i][0])
        empates.append(dados_partida[i][3])
#print (vitorias)
#print (empates)

# =============================================================================
# 3. Contagem da pontuação: vitórias, empates e derrotas e; do nº de vitórias
# =============================================================================
pontos = []
vitorias_times = []
for i in range ( len(nome_times) ):
    pontos.append ( 3*vitorias.count(nome_times[i]) + empates.count(nome_times[i]) )
    vitorias_times.append ( vitorias.count(nome_times[i]) )
#print (nome_times, pontos, vitorias_times)

# =============================================================================
# 4. Número de gols feitos
# =============================================================================
gols_pro = ['']*numero_times #vou usar o fato de que a colocação dos resultados está ordenada
for k in range ( len (nome_times) ):
    gols_pro[k] = []
    for i in range ( len(dados_partida) ):
        for j in range ( len (dados_partida[0]) ): #mais linhas do que colunas
            if dados_partida[i][j] == nome_times [k]:
                gols_pro[k].append (int(dados_partida[i][j+1]))
#print (nome_times, gols_pro)
soma_gols_pro = ['']*numero_times
for i in range ( len(nome_times) ):
   soma_gols_pro[i] = (sum (gols_pro[i]) )
#print (nome_times, soma_gols_pro)

# =============================================================================
# 5. Saldo de gols
# =============================================================================
saldo_positivo = []
saldo_negativo = []
saldo_times = []
#para o saldo de gols, empates são irrelevantes
#o extend aqui resolve o problema de colocar todo mundo em diferentes listas
for i in range ( len(dados_partida) ):
    if dados_partida[i][1] > dados_partida[i][4]:
        saldo_positivo.extend  ( ( int(dados_partida[i][1]) - int(dados_partida[i][4]) ) * [ (dados_partida[i][0]) ]  )
        saldo_negativo.extend  ( ( int(dados_partida[i][1]) - int(dados_partida[i][4]) ) * [ (dados_partida[i][3]) ]  )
#print (saldo_positivo)
for i in range ( len(dados_partida) ):
    if dados_partida[i][1] < dados_partida[i][4]:
        saldo_positivo.extend  ( ( int(dados_partida[i][4]) - int(dados_partida[i][1]) ) * [ (dados_partida[i][3]) ]  )
        saldo_negativo.extend  ( ( int(dados_partida[i][4]) - int(dados_partida[i][1]) ) * [ (dados_partida[i][0]) ]  )
#print (saldo_negativo)
for i in range ( len(nome_times) ):
    saldo_times.append ( int(saldo_positivo.count(nome_times[i])) - int(saldo_negativo.count(nome_times[i])) )
#print (saldo_times)

# =============================================================================
# 6. Resultados
# =============================================================================

campeoes = []
if pontos.count( max(pontos) ) > 1:
#    print ('pudim')
    if vitorias_times.count ( max(vitorias_times) ) > 1:
#        print ('pudim2')
        if saldo_times.count ( max(saldo_times) ) > 1:
#            print ('pudim3')
            if soma_gols_pro.count ( max(soma_gols_pro) ) > 1:
                for i in range (len(soma_gols_pro)):
                    if soma_gols_pro[i] == max (soma_gols_pro):
                        campeoes.append (nome_times[i])
            else: 
                campeoes.append( nome_times [soma_gols_pro.index( max(soma_gols_pro) )] )
        else:
            campeoes.append( nome_times [saldo_times.index( max(saldo_times) )] )
    else:
        campeoes.append( nome_times [vitorias_times.index( max(vitorias_times) )] )
else:
    campeoes.append( nome_times [pontos.index( max(pontos) )] )


for i in range ( len(nome_times) ):
    print ( nome_times[i] , pontos[i] , vitorias_times[i], saldo_times[i], soma_gols_pro[i] )

if (len(campeoes)) > 1:
    print ( 'Campeoes: ',end = '' )
    for i in range (len(campeoes)):
        if i == (len(campeoes) - 1):
            print (campeoes[i])
            i += 1
        else:
            print (campeoes[i], end = ' ')

#    print () #print linha em branco
else:
    print ('Campeao:', campeoes[0])

if campeoes.count(meu_time) > 0:
        print ('Meu time pode ser campeao!!!')