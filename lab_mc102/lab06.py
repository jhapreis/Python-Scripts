lance_minimo = float ( input('lance minimo: ') ) 
print ('Lance minimo: R$', format ( (lance_minimo), ".2f") )
print ('Alguem oferece o lance minimo?')

leilao = True
lance = 1
tentativa = 1

while leilao == True:
    ofertante = input ('ofertante: ')
    global oferta
    oferta = float ( input ('oferta: ') )
    if oferta >= lance_minimo and lance == 1:
        print ('Maior oferta ate agora: ' +  'R$ {v}'.format( v = format (oferta, ".2f") ) + '. Alguem oferece mais?')
#        print ('ofertante: ', ofertante)
        lance_minimo = oferta
        lance = lance + 1
    elif oferta > lance_minimo and lance > 1:
        print ('Maior oferta ate agora: ' +  'R$ {v}'.format( v = format (oferta, ".2f") ) + '. Alguem oferece mais?')
#        print ('ofertante: ', ofertante)
        lance_minimo = oferta
        lance = lance + 1 
    elif oferta < lance_minimo and lance == 1:
        print ('Alguem oferece o lance minimo?')
#    print ('lance numero', lance)
    if lance > 3 or tentativa > 5:
        'FIM'
        break
    tentativa = tentativa + 1
#    print ('tentativa numero', tentativa)

leilao = False
if leilao == False:
    print ('Dou-lhe uma, dou-lhe duas, dou-lhe tres!')
    if lance == 1:
        print ('O item nao foi vendido. Anunciaremos novo leilao em breve.')
    elif lance > 1:
        print ('Vendido para' + ' ' + ofertante + ' ' + "por R$ {v}".format( v = format (oferta, ".2f") + '!' ) )
        
        
        