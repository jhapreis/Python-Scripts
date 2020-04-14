#MC102 7 -- LAB 03

#1) Condições da Universidade de destino
aceito = input () #indica se foi ou não aceito; SIM ou NAO
fluente = input () #indica se é ou não fluente; SIM ou NAO

if aceito == 'SIM' and fluente == 'SIM':
    global universidade
    universidade = True
else: 
    universidade = False


#2) Coeficientes de progressão e de rendimento da Unicamp: CP > 0.5 e CPR > 0
CP = float ( input () ) #valor do coeficiente de progressão
CRP = float ( input () ) #valor do coeficiente de rendimento padronizado
reprovações = int ( input () ) #número de reprovações não pode ser maior que 2

if CP > 0.5 and CRP > 0 and reprovações < 3:
    global unicamp
    unicamp = True  
else:
    unicamp = False
    

#3) Condições financeiras: deverá possuir qualquer uma das quatro (uma é suficiente)
loteria = input () #possui dinheiro de loteria? SIM ou NAO
família = input () #possuiu auxílio familiar? SIM ou NAO
créditos = input () #possui créditos? SIM ou NAO
bolsa = input () #recebe bolsa? SIM ou NAO

if loteria == 'SIM' or família == 'SIM' or créditos == 'SIM' or bolsa == 'SIM':
    global financeiro
    financeiro = True
else:
    financeiro = False


#4) Aprovado em todos os critérios?
if universidade == True and unicamp == True and financeiro == True:
    aprovação = True
else:
    aprovação = False
    
print ('Atende condicoes da universidade destino:', universidade)
print ('Atende condicoes da Unicamp:', unicamp) #se aprovado em ambos os critérios de (2)
print ('Atende condicoes financeiras:', financeiro) #se possui qualquer um dos critérios em (3)
print ('Intercambio:', aprovação) #aprovação em todas as condicionais; aprovado em (4)