#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 16 21:51:58 2020

@author: jorgereis
"""


class ExtratorArgumentosUrl:
    
    def __init__(self, url):
        if self.urlEhValida(url):
            self.url = url
        else:
            raise LookupError("Url inválida!!!")
    
    @staticmethod        
    def urlEhValida(url):
        if url:
            return True
        else:
            return False
        
    def retornaMoedas(self):
        buscaMoedaOrigem = "moedaorigem="
        buscaMoedaDestino = "moedadestino="

        inicioSubstringMoedaOrigem = self.encontraIndiceInicioSubstring(
            buscaMoedaOrigem)
        finalSubstringMoedaOrigem = self.url.find("&")
        moedaOrigem = self.url[inicioSubstringMoedaOrigem:
                               finalSubstringMoedaOrigem]

        inicioSubstringMoedaDestino = self.encontraIndiceInicioSubstring(
            buscaMoedaDestino)
        finalSubstringMoedaDestino = self.url.find("&valor")
        moedaDestino = self.url[inicioSubstringMoedaDestino:
                                finalSubstringMoedaDestino]

        return moedaOrigem, moedaDestino

    def encontraIndiceInicioSubstring(self, moedaOuValor):
            return self.url.find(moedaOuValor) + len(moedaOuValor)
        
        
        
        
        
url = "https://bytebank.com/cambio?moedaorigem=real&moedadestino=dolar&valor=700"
argumento = ExtratorArgumentosUrl(url)
moedaOrigem , moedaDestino = argumento.retornaMoedas()
# print(argumento)
print(moedaDestino, moedaOrigem)

# print(ExtratorArgumentosUrl(None))


# =============================================================================
# Método Replace
# =============================================================================

'''
O replace busca todos os elementos que são iguais ao alvo de busca e substitui todos.
É possível indicar quantoas vezes você quer que substitua.
'''
string = 'bytebank'
stringNova = string.replace('byte', 'pimba', 1)
print(stringNova)