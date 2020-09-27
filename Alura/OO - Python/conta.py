#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 30 20:03:10 2020

@author: jorgereis
"""

# =============================================================================
# 
#                      PYTHON 3: INTRODUÇÃO A ORIENTAÇÃO A OBJETOS
#
# =============================================================================


# =============================================================================
# Classes e atributos
# =============================================================================

# receita de bolo = 'classe'

# class Conta:
#     # __init__ é uma função chamada construtora
#     def __init__(self, numero, titular, saldo, limite): 
#     #'self' é a referência que sabe onde encontrar o objeto na memória
#         print(  "Construindo objeto... {}".format(self)  )
#         self.numero = numero
#         self.titular = titular
#         self.saldo = saldo
#         self.limite = limite
#     #esses são os 'Atributos'; atributos são parâmetros que especificam uma classe
        

# criar bolo vazio
# class Conta:
#     pass
        
# conta = Conta(123, 'Nico', 55.5, 1000.0)


# =============================================================================
# Construtores com valores padrão
# =============================================================================
        
'''podemos supor que apenas as contas com limites especiais precisariam passar tal argumento 
(no exemplo acima apenas conta3 tem um limite especial). 
Isso é feito colocando na declaração da função construtora __init__ um 
valor padrão para o limite.'''

# class Conta:
#     def __init__(self, numero, titular, saldo, limite = 1000.0): 
#         print(  "Construindo objeto... {}".format(self)  )
#         self.numero = numero
#         self.titular = titular
#         self.saldo = saldo
#         self.limite = limite
#         # daí, não passamos parâmetro
        
# c_104 = Conta(1, "J", 0.0)
# c_341 = Conta(2, "JJ", 0.0, 2000.0)


# =============================================================================
# Acessando os atributos
# =============================================================================

# para acessar os atributos, basta usar um '.', como segue
# print (conta.saldo)


# =============================================================================
# Usando os métodos (a.k.a. 'funções')
# =============================================================================

# class Conta:
    
#     # __init__ é uma função chamada construtora
#     def __init__(self, numero, titular, saldo, limite): 
#     #'self' é a referência que sabe onde encontrar o objeto na memória; 
#     # sempre presente, é o endereço
#         print(  "Construindo objeto... {}".format(self)  )
#         self.numero = numero
#         self.titular = titular
#         self.saldo = saldo
#         self.limite = limite
#     #esses são os 'Atributos'; atributos são parâmetros que especificam uma classe
        
#     def extrato(self):
#         print( "Saldo {} do titular {}".format(self.saldo, self.titular) )
#     # para acessar a função de dado objeto, usamos 'objeto.função()'
#     # ex.: conta.extrato()
    
#     def deposita(self, valor):
#         self.saldo += valor
    
#     def saque(self, valor):
#         self.saldo -= valor
        
'''Cada um desses métodos é implementado de maneira 'oculta', 'encapsulada', pois acontece de
não termos que usar nem nos preocupar com o que está acontecendo ao redor. 
É um bloco que funciona e que usamos quando necessário.'''


# =============================================================================
# Encapsulamento
# =============================================================================

'''1) Atributos privados: atributo --> __atributo
desse modo, só é possível acessar (e portanto modificar)
os atributos por meio da classe! No caso, ele ainda permite que você modifique os valores,
mas somente através de uma clarificação de que o está fazendo por meio da classe.
Ex:. conta._Classe__saldo  exibe o saldo (passando por cima do método conta.extrato()' '''

# class Conta:
    
#     # __init__ é uma função chamada construtora
#     def __init__(self, numero, titular, saldo, limite): 
#     #'self' é a referência que sabe onde encontrar o objeto na memória; 
#     # sempre presente, é o endereço
#         print(  "Construindo objeto... {}".format(self)  )
#         self.__numero = numero
#         self.__titular = titular
#         self.__saldo = saldo
#         self.__limite = limite
#     #esses são os 'Atributos'; atributos são parâmetros que especificam uma classe
        
#     def extrato(self):
#         print( "Saldo {} do titular {}".format(self.__saldo, self.__titular) )
#     # para acessar a função de dado objeto, usamos 'objeto.função()'
#     # ex.: conta.extrato()
    
#     def deposita(self, valor):
#         self.__saldo += valor
    
#     def saque(self, valor):
#         self.__saldo -= valor


# 2) ESSÊNCIA DO MUNDO O.O.: ORGANIZAÇÃO
# ex.: nova operação (novo método): 'transferência'

# class Conta:
    
#     # __init__ é uma função chamada construtora
#     def __init__(self, numero, titular, saldo, limite): 
#     #'self' é a referência que sabe onde encontrar o objeto na memória; 
#     # sempre presente, é o endereço
#         print(  "Construindo objeto... {}".format(self)  )
#         self.__numero = numero
#         self.__titular = titular
#         self.__saldo = saldo
#         self.__limite = limite
#     #esses são os 'Atributos'; atributos são parâmetros que especificam uma classe
        
#     def extrato(self):
#         print( "Saldo {} do titular {}".format(self.__saldo, self.__titular) )
#     # para acessar a função de dado objeto, usamos 'objeto.função()'
#     # ex.: conta.extrato()
    
#     def deposito(self, valor):
#         self.__saldo += valor
    
#     def saque(self, valor):
#         self.__saldo -= valor
    
#     def transferencia(self, valor, destino):
#         self.saque(valor) 
#         # com esse 'self', podemos acessar a mesma conta de origem 
#         # (que é chamada quando chamamos o método de 'transferencia')
#         destino.deposito(valor)
        
'''as classes devem ter somente uma única 'responsabilidade', somente uma única razão de trabalho
misturar as responsabilidades causa confusão no código'''


# =============================================================================
# Para saber mais: SOLID
# =============================================================================

'''Falamos nessa aula sobre a coesão que é ligado ao principio de responsabilidade única. 
Aprendemos que uma classe deve ter apenas uma responsabilidade 
(ou deve ter apenas uma razão para existir). 
Em outras palavras, ela não deve assumir responsabilidades que não são delas.

Além desse princípio de responsabilidade única existem outras que foram definidos 
através do Robert C. Martin no início dos anos 2000 e são conhecidos pelo acrônimo SOLID:

S - Single responsibility principle
O - Open/closed principle
L - Liskov substitution principle
I - Interface segregation principle
D - Dependency inversion principle
Na Alura temos cursos específicos sobre o SOLID, mas fique tranquilo, 
na medida que você avança no mundo OO esses princípios ficam mais claros e 
fáceis de se entender.'''


# =============================================================================
# Usando propriedades (getters e setters; @property e @nome_getter)
# =============================================================================

'''Se você quer fazer algo com seu objeto, USE UM MÉTODO; essa é sempre a resposta'''

# adicionando o método 'saldo'

# class Conta:
    
#     '''__init__ é uma função chamada construtora'''
#     def __init__(self, numero, titular, saldo, limite): 
#         # 'self' é a referência que sabe onde encontrar o objeto na memória; 
#         # sempre presente, é o endereço
#         print(  "Construindo objeto... {}".format(self)  )
#         self.__numero = numero
#         self.__titular = titular
#         self.__saldo = saldo
#         self.__limite = limite
#     '''esses são os 'Atributos'; atributos são parâmetros que especificam uma classe'''
        
#     def extrato(self):
#         print( "Saldo {} do titular {}".format(self.__saldo, self.__titular) )
#     # para acessar a função de dado objeto, usamos 'objeto.função()'
#     # ex.: conta.extrato()
    
#     def deposito(self, valor):
#         self.__saldo += valor
    
#     def saque(self, valor):
#         self.__saldo -= valor
    
#     def transferencia(self, valor, destino):
#         self.saque(valor) 
#         # com esse 'self', podemos acessar a mesma conta de origem 
#         # (que é chamada quando chamamos o método de 'transferencia')
#         destino.deposito(valor)
    
#     # para dar um 'return' sobre os valores do objeto, podemos usar essas funções 'getters'
#     # def get_saldo(self):
#     #     return (self.__saldo)
#     @property 
#     # é usado para mostrar ACESSAR os valores como se fossem propriedades do objeto,
#     # acessando diretamente com 'conta.limite'
#     def limite(self):
#         return (self.__limite)
#     @property
#     def saldo(self):
#         return (self.__saldo)
#     @property
#     def titular(self):
#         return (self.__titular)
    
#     # para fazer uma alteração nos valores, é comum nomear as funções como 'setters'
#     @limite.setter
#     # nesse caso, podemos simplismente, em vez de chamar a função por 'setter', indexar que
#     # esse valor pode ser ALTERADO diretamente fazendo 'conta.limite = 2000.0', por ex.
#     def limite(self, limite):
#         self.__limite = limite
        
''' Usar os métodos com esses '@' na frente facilita pois torna mais fácil o reconhecimento
quando estamos falando de execução. Nesse caso, simplesmente acessar/redefinir os valores 
'manualmente'. No caso, parece que estamos alterando os valores, mas por baixo dos panos
estamos acessando os métodos
'''


# =============================================================================
# Métodos privados e estáticos
# =============================================================================

# modificando os critérios de saques mediante o limite (máximo)

class Conta:
    
    '''__init__ é uma função chamada construtora'''
    def __init__(self, numero, titular, saldo, limite): 
        # 'self' é a referência que sabe onde encontrar o objeto na memória; 
        # sempre presente, é o endereço
        print(  "Construindo objeto... {}".format(self)  )
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite
        
    '''esses são os 'Atributos'; atributos são parâmetros que especificam uma classe'''
        
    def extrato(self):
        print( "Saldo {} do titular {}".format(self.__saldo, self.__titular) )
    # para acessar a função de dado objeto, usamos 'objeto.função()'
    # ex.: conta.extrato()
    
    def deposito(self, valor):
        self.__saldo += valor
    
    def __pode_sacar(self, valor_a_sacar):
        # com o '__' na frente, ele privatiza o método para usar somente na classe
        valor_disponivel_para_saque = self.__saldo + self.__limite
        return valor_a_sacar <= valor_disponivel_para_saque
    # retorna 'True' or 'False'
            
    def saque(self, valor):
        if self.__pode_sacar(valor):
            self.__saldo -= valor
        else:
            print('O valor {} passou o limite.'.format(valor))
    
    def transferencia(self, valor, destino):
        self.saque(valor) 
        # com esse 'self', podemos acessar a mesma conta de origem 
        # (que é chamada quando chamamos o método de 'transferencia')
        destino.deposito(valor)
    
    # para dar um 'return' sobre os valores do objeto, podemos usar essas funções 'getters'
    # def get_saldo(self):
    #     return (self.__saldo)
    @property 
    # é usado para mostrar ACESSAR os valores como se fossem propriedades do objeto,
    # acessando diretamente com 'conta.limite'
    def limite(self):
        return (self.__limite)
    @property
    def saldo(self):
        return (self.__saldo)
    @property
    def titular(self):
        return (self.__titular)
    
    # para fazer uma alteração nos valores, é comum nomear as funções como 'setters'
    @limite.setter
    # nesse caso, podemos simplismente, em vez de chamar a função por 'setter', indexar que
    # esse valor pode ser ALTERADO diretamente fazendo 'conta.limite = 2000.0', por ex.
    def limite(self, limite):
        self.__limite = limite

    
    # Métodos estáticos: 
    # são métodos que existem sempre, independentemente de existir ou não um objeto
    # devem ser usados com bastante cautela
    @staticmethod
    def codigo_banco():
        return '001'
        