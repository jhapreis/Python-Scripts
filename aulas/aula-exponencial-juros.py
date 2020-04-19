#C = C_0*(1+i)**t
#Repartir um mesmo intervalo de um ano em diferentes pedaços
#Não se preocupe se a divisão der resultado inteiro

#1. Selecionar o número de partições, a unidade e o capital inicial
print ('Qual o intervalo de tempo decorrido?')
value = float( input () )
print ('Tempo em anos [a], meses [m], dias [d] ou horas [h]?')
unit = input ()
C_0 = 1000

#2. Calcular o tempo e a taxa
if unit == 'a':
    t = 1
elif unit == 'm':
    t = 12 / value
elif unit == 'd':
    t = 365 / value
elif unit == 'h':
    t = 8760 / value
else:
    print('erro de seleção')
    exit()
i = 1 / t

#3. Calcular os juros e printar
C = C_0*(1+i)**t
print ( 'Taxa =', str( round(i*100,2) )+ '%' )
print ( 'Capital final = R$', round(C,2) )
print ( 'Comparação', C / C_0, 'vezes' )