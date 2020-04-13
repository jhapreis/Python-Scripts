#MC102 7 -- LAB05

import math 

#10% para EP
#5% para PP
#5% para EP`e PPI

curso = input ()
vagas_enem = int ( input () )

EP = math.floor (50/100 * vagas_enem)
#print ('EP =', EP)
PP = math.floor (25/100 * vagas_enem)
#print ('PP =', PP)
EP_PPI = math.floor (25/100 * vagas_enem)
#print('EP+PPI =', EP_PPI)

vagas_excendentes = vagas_enem - EP - PP - EP_PPI
#print ('vagas excedentes =', vagas_excendentes)

#Avaliando parte fracionária:
#Se a parte fracionária de 10% das vagas for maior do que a de 5% haverá apenas uma vaga excedente, que será destinada ao segmento EP.
#Se a parte fracionária de 5% for maior do que a de 10%:
#Se tivermos duas vagas excedentes, uma delas será destinada ao segmento EP+PPI e a outra ao segmento PP.
#Se tivermos apenas uma vaga excedente, esta será direcionada ao segmento EP+PPI.

if (50/100*vagas_enem - math.floor(50/100 * vagas_enem)) > (25/100*vagas_enem - math.floor (25/100 * vagas_enem)):
    EP = EP + 1
elif (25/100*vagas_enem - math.floor (25/100 * vagas_enem)) > (50/100*vagas_enem - math.floor(50/100 * vagas_enem)):
    if vagas_excendentes == 2:
        PP = PP + 1
        EP_PPI = EP_PPI + 1
    elif vagas_excendentes == 1:
        EP_PPI = EP_PPI + 1
#else:
#    print ('condicioanl não deu certo')

#print () #pula uma linha
print ('Curso:', curso)
print ('Vagas Enem:', vagas_enem)
print ('EP:', EP)
print ('PP:', PP)
print ('EP+PPI:', EP_PPI)
#vagas_excendentes = vagas_enem - EP - PP - EP_PPI #verifica se as vagas foram todas preenchidas
#print ('vagas excedentes =', vagas_excendentes)