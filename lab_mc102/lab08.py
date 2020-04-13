#MC102-7 -- LAB 08

# =============================================================================
# 1: Declaração de variáveis; importação dos valores como lista
# =============================================================================
nota_ac = [float(i) for i in input().split()] #será inserido uma sequência de valores
#e estes serão manipulados e, após, dispostos numa lista
#print ("nota_ac =", nota_ac)
nota_lab = [float(i) for i in input().split()]
#print ('nota_lab =', nota_lab)
peso_lab = [float(i) for i in input().split()]
#print ('peso_lab =', peso_lab)
nota_labextra = [float(i) for i in input().split()]
#print ('nota_labextra =', nota_labextra)
peso_labextra = [float(i) for i in input().split()]
#print ('peso_labextra =', peso_labextra)
nota_prova = [float(i) for i in input().split()]
#print ('nota_prova =', nota_prova)
peso_prova = [2 , 3] #uma leitura atenta me mostrou essa informação
Freq = int ( input () ) #Número percentual de presenças; de 0 a 100

#Nota: se colocarmos a variável 'Exame' aqui, do jeito que eu pensei, encontraremos 
#problemas quando for dar input ou não na nota dele. A solução que eu encontrei foi
#criar uma condicional para colocar ou não o exame como input, mediante necessidade.


# =============================================================================
# 2: Calculando as médias com loops
# =============================================================================

# 2.1: Médias-simples das atividades conceituais e das provas

def média_simples (x):
    i = 0 
    soma = 0
    while i <= ( len(x) - 1):
        soma = soma + x[i]
        i = i + 1
#    print ('soma =', soma)
    média = soma / len(x)
#    print ('média simples =', média)
    return (média)
    
MAC = média_simples (nota_ac)

#2.2: Médias-ponderadas das notas de lab com as de lab-extra, do jeito que foi mandado

def soma_dos_produtos (x, y):
    i = 0
    soma = 0
    while i <= ( len(x) - 1 ):
        soma = soma + x[i]*y[i]
        i = i + 1
#    print ('soma dos produtos =', soma)
#    print ('i =', i)
    return (soma)

def somatório (x):
    i = 0 
    soma = 0
    while i <= (len(x) - 1):
        soma = soma + x[i]
        i = i + 1
#    print ('somatório =', soma)
    return (soma)

ML = ( soma_dos_produtos (nota_lab , peso_lab) + soma_dos_produtos (nota_labextra , peso_labextra) ) / somatório (peso_lab)
MP = soma_dos_produtos (nota_prova , peso_prova) / somatório (peso_prova)

# =============================================================================
# 3: Condicional para aprovação ou reprovação
# =============================================================================
vai_pro_exame = False

if Freq >= 75: #aprovado na frequência
    aprovado_frequencia = True
    if MP >= 5 and ML >= 5: #aprovado sem exame
        MElem = 0.6*MP + 0.3*ML + 0.1*MAC
        MFinal = max(5, MElem)
        aprovado_nota = True
    elif MP >= 2.5 and ML >= 2.5: #teve de fazer exame final
        vai_pro_exame = True
        Exame = float ( input () ) #Nota do exame; vide comentário no começo do script
        MFinal = ( min(MP, ML) + Exame) / 2
        if MFinal >= 5.0: #aprovado pelo exame
            aprovado_nota = True
        else: #reprovado pelo exame
            aprovado_nota = False
    elif MP < 2.5 or ML < 2.5: #reprovado já sem exame
        MFinal = min(MP, ML)
        aprovado_nota = False
elif Freq < 75: #reprovado por frequência
    aprovado_frequencia = False
    MFinal = min(MP, ML)


# =============================================================================
# 4: Resultados: aprovação ou reprovação
# =============================================================================

print ( 'Media das atividades conceituais:' , "%.1f" % MAC )
print ( 'Media das tarefas de laboratorio:', "%.1f" % ML )
print ( 'Media das provas:', "%.1f" % MP)

if vai_pro_exame == True:
    print ( 'Nota no exame:', "%.1f" % Exame )

if aprovado_frequencia and aprovado_nota == True: #aprovado por nota e frequência
    print ('Aprovado(a) por nota e frequencia.')
elif aprovado_frequencia == False:
    print ('Reprovado(a) por frequencia.')
elif aprovado_nota == False:
    print ('Reprovado(a) por nota.')


if MFinal <= 10:
    print ( 'Media final:', "%.1f" % MFinal )
elif MFinal > 10:
    print ( 'Media final:', 10.0 )
#eu tô correndo pra terminar ele que eu esqueci de mandar, então tô
#gambiarrando tudo