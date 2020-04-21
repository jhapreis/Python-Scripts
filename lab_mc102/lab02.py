#2019.03.26
#Jorge Henrique Reis
#RA: 237966
#
#MC102 7: LAB 02 -- Pagamento com atraso
#
valor = float ( input () ) #Valor da fatura
dias_atraso = int ( input () ) #Dias de atraso no pagamento

multa = 2/100 * valor #Multa: 2% do valor da fatura.

juros = 0.033/100 * valor * dias_atraso #Juros: 0.033% do valor da fatura 
#                                       multiplicado pelo número de dias em atraso.

total = valor + multa + juros #Valor total: soma do valor inicial 
#                              com valor da multa e dos juros.

print ('Valor: R$', format (valor, '.2f') ) #Valor: o valor lido da entrada;
print ('Multa: R$', format (multa, '.2f') )
print ('Juros: R$', format (juros, '.2f') )
print ('Valor total: R$', format (total, '.2f') )