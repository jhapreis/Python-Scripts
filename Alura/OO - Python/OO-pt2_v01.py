#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun  6 20:27:43 2020

@author: jorgereis
"""


# class Filme:
#     def __init__(self, nome, ano, duracao):
#         self.__nome = nome.title()
#         self.ano = ano
#         self.duracao = duracao
#         self.__likes = 0

#     @property
#     def likes(self):
#         return self.__likes

#     def dar_likes(self):
#         self.__likes += 1

#     @property
#     def nome(self):
#         return self.__nome

#     @nome.setter
#     def nome(self, nome):
#         self.__nome = nome

# class Serie:
#     def __init__(self, nome, ano, temporadas):
#         self.__nome = nome.title()
#         self.ano = ano
#         self.temporadas = temporadas
#         self.__likes = 0

#     @property
#     def likes(self):
#         return self.__likes

#     def dar_likes(self):
#         self.__likes += 1

#     @property
#     def nome(self):
#         return self.__nome

#     @nome.setter
#     def nome(self, nome):
#         self.__nome = nome

# vingadores = Filme('vingadores - guerra infinita', 2018, 160)
# print(vingadores.nome)

# atlanta = Serie('atlanta', 2018, 2)
# print(f'Nome: {atlanta.nome} - Ano: {atlanta.ano}')


# =============================================================================
# Herança: resolvendo problema de duplicação entre classes
# =============================================================================

'''
Criar uma classe que possui uma generalidade maior, um conceito mais amplo.
A partir disso, a herança passa as informações do mais geral ao mais particular
'''

# class Programa:
#     def __init__(self, nome, ano):
#         self._nome = nome.title()
#         self.ano = ano
#         self.__likes = 0

#     @property
#     def likes(self):
#         return self.__likes

#     def dar_likes(self):
#         self.__likes += 1

#     @property
#     def nome(self):
#         return self._nome

#     @nome.setter
#     def nome(self, nome):
#         self._nome = nome



# class Filme(Programa): # classe filha de 'Programa'
#     def __init__(self, nome, ano, duracao):
#         # chama o inicializador da classe-mãe, a qual passa seus genes adiante
#         super().__init__(nome, ano) 
#         self.duracao = duracao

    

# class Serie(Programa): # classe filha de 'Programa'
#     def __init__(self, nome, ano, temporadas):
#         super().__init__(nome, ano) 
#         self.temporadas = temporadas



# vingadores = Filme('vingadores - guerra infinita', 2018, 160)
# print(vingadores.nome)

# atlanta = Serie('atlanta', 2018, 2)
# print(f'Nome: {atlanta.nome} - Ano: {atlanta.ano}')

'''
Adoção de variávies: 
    Na questão do nome das variáveis 'ocultas', por convenção usamos _nome
em vez de __nome, para que possamos adotar os objetos da classe de ordem geral
    Podemos ainda remover a questão das repetições dos nomes, usando a função
super().__init__(nome) que remove a necessidade de re-declarar os construtores
que já vêm da classe-mãe. Na verdade, super(). acessa 
'''


# =============================================================================
# Polimorfismos: reduzindo if's 
# =============================================================================

# class Programa:
#     def __init__(self, nome, ano):
#         self._nome = nome.title()
#         self.ano = ano
#         self._likes = 0

#     @property
#     def likes(self):
#         return self._likes

#     def dar_likes(self):
#         self.__likes += 1

#     @property
#     def nome(self):
#         return self._nome

#     @nome.setter
#     def nome(self, nome):
#         self._nome = nome



# class Filme(Programa): # classe filha de 'Programa'
#     def __init__(self, nome, ano, duracao):
#         # chama o inicializador da classe-mãe, a qual passa seus genes adiante
#         super().__init__(nome, ano) 
#         self.duracao = duracao
#     # def imprime(self):
#     #     print( f'{self._nome} - {self.ano} - {self.duracao} min - {self._likes} Likes' ) 
#     def __str__(self): # vide nota abaixo
#         return f'{self._nome} - {self.ano} - {self.duracao} min - {self._likes} Likes'
    

# class Serie(Programa): # classe filha de 'Programa'
#     def __init__(self, nome, ano, temporadas):
#         super().__init__(nome, ano) 
#         self.temporadas = temporadas
#     # def imprime(self):
#     #     print( f'{self._nome} - {self.ano} - {self.temporadas} temporadas- {self._likes} Likes' ) 
#     def __str__(self): # vide nota abaixo
#         return f'{self._nome} - {self.ano} - {self.temporadas} temporadas- {self._likes} Likes'
        



# vingadores = Filme('vingadores - guerra infinita', 2018, 160)

# atlanta = Serie('atlanta', 2018, 2)


''' 
1) Uma das vantagens da herança é a questão do polimorfismo, onde conseguimos,,
por exemplo, rodar uma lista com for sem nos preocuparmos se os objetos são de
um tipo ou de outro, pois são todos de uma super-classe específica
'''

# filmes_e_series = [vingadores, atlanta]

# for programa in filmes_e_series: 
#     # fazer separação entre 'filmes' e 'séries' com métodos específicos
#     #das classes filhas
#     programa.imprime()

'''
2) Em linguagem Python, especificamente falando, existe uma forma mais específica
de representar objetos textualmente
'''

# for programa in filmes_e_series:
#     print(programa) 
    # #agora ele vai no objeto específico e exibe a representação textual dele

'''
A ideia do polimorfismo é que uma classe genérica defina alguns métodos e as classes filhas sobrescrevam estes métodos, porque cada uma se comporta de uma maneira, porém, todos tem o mesmo comportamento geral em comum.

Podemos ilustrar melhor isto com uma classe genérica Animal onde a mesma possui o método de fala. E as classes filhas Cachorro e Gato herdam o método de fala da classe Animal, porém, concorda comigo que cada um "fala" de uma maneira? Então em código isto ficaria assim:

class Animal:

    def fala(self):
        print("Animal Falando")

class Cachorro(Animal):

    def fala(self):
        print("Auauau")

class Gato(Animal):

    def fala(self):
        print("Miau miau")
Observe que o método de fala foi sobrescrito nas classes filhas. Qual o benefício de utilizar desta forma? O objetivo é que você possa reutilizar o código(herança) modificando apenas alguns comportamentos da classe herdada(polimorfismo) mediante a necessidade.
'''

# =============================================================================
# Quando não usar herança
# =============================================================================

# class Programa:
#     def __init__(self, nome, ano):
#         self._nome = nome.title()
#         self.ano = ano
#         self._likes = 0

#     @property
#     def likes(self):
#         return self._likes

#     def dar_likes(self):
#         self.__likes += 1

#     @property
#     def nome(self):
#         return self._nome

#     @nome.setter
#     def nome(self, nome):
#         self._nome = nome



# class Filme(Programa): # classe filha de 'Programa'
#     def __init__(self, nome, ano, duracao):
#         super().__init__(nome, ano) 
#         self.duracao = duracao
#     def __str__(self): 
#         return f'{self._nome} - {self.ano} - {self.duracao} min - {self._likes} Likes'
    

# class Serie(Programa): # classe filha de 'Programa'
#     def __init__(self, nome, ano, temporadas):
#         super().__init__(nome, ano) 
#         self.temporadas = temporadas
#     def __str__(self):
#         return f'{self._nome} - {self.ano} - {self.temporadas} temporadas- {self._likes} Likes'

'''
    Na questão da playlist, como precisamos rodar sobre a list e iterar, pode parecer
interessante que a gente se filie à 'list', uma classe built-in do Python. 
    Porém, isso traz muitas complicações, que acabam por não facilitar as coisas,
já que teríamos que tomar cuidado toda vez que fossemos usar alguma funcionalidade
da classe, para não conflitar com a list, de quem não conhecemos tudo. Ou seja, 
NÃO É BOM PEGAR A HERANÇA DE UMA SUPER-CLASSE DA QUAL NÃO CONHECEMOS TUDO
    A solução é pegar o melhor dos dois mundos.
'''

# class Playlist: 
#     def __init__(self, nome, programas):
#         self.nome = nome
#         self._programas = programas
#     @property
#     def listagem(self):
#         return self._programas
#     @property
#     def tamanho(self):
#         return len(self._programas)

# vingadores = Filme('vingadores - guerra infinita', 2018, 160)
# tmep = Filme('todo mundo em pânico', 1999, 100)
# atlanta = Serie('atlanta', 2018, 2)
# demolidor = Serie('demolidor', 2016, 2)

# filmes_e_series = [vingadores, atlanta, demolidor, tmep]
# playlist_fim_de_semana = Playlist('fim de semana', filmes_e_series)

# print(f'\nTamanho da playlist: {len(playlist_fim_de_semana.listagem)} \n')
# for programa in playlist_fim_de_semana.listagem:
#     print(programa) 



# =============================================================================
# Duck Typing & Python Data Model
# =============================================================================

class Programa:
    def __init__(self, nome, ano):
        self._nome = nome.title()
        self.ano = ano
        self._likes = 0

    @property
    def likes(self):
        return self._likes

    def dar_likes(self):
        self.__likes += 1

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, nome):
        self._nome = nome



class Filme(Programa): # classe filha de 'Programa'
    def __init__(self, nome, ano, duracao):
        super().__init__(nome, ano) 
        self.duracao = duracao
    def __str__(self): 
        return f'{self._nome} - {self.ano} - {self.duracao} min - {self._likes} Likes'
    

class Serie(Programa): # classe filha de 'Programa'
    def __init__(self, nome, ano, temporadas):
        super().__init__(nome, ano) 
        self.temporadas = temporadas
    def __str__(self):
        return f'{self._nome} - {self.ano} - {self.temporadas} temporadas- {self._likes} Likes'


class Playlist: 
    def __init__(self, nome, programas):
        self.nome = nome
        self._programas = programas
    '''
    o método __getitem__ transforma a nossa playlist num objeto iterável
    '''
    def __getitem__(self, item):
        return self._programas[item]    
    @property
    def listagem(self):
        return self._programas
    def __len__(self):
        return len(self._programas)

vingadores = Filme('vingadores - guerra infinita', 2018, 160)
tmep = Filme('todo mundo em pânico', 1999, 100)
atlanta = Serie('atlanta', 2018, 2)
demolidor = Serie('demolidor', 2016, 2)

filmes_e_series = [vingadores, atlanta, demolidor, tmep]
playlist_fim_de_semana = Playlist('fim de semana', filmes_e_series)

print(f'\nTamanho da playlist: {len(playlist_fim_de_semana.listagem)} \n')
for programa in playlist_fim_de_semana:
    print(programa) 


'''
    Para usarmos heranças, é bom ter em mente que elas são mais úteis quando falamos
de usar para auxiliar em questões de interface (quando queremos usar o polimorfismo)
ou na questão de remover duplicações. 
    
    O problema das heranças é que uma sub-classe pode acabar herdando complicações
de uma super-classe, porque alguns métodos podem conflitar de pai para filho. 
Nesse caso, é bom deixar a classe com 'aparência' da super-classe, mas sem efetivamente
'ser' uma. 
    Um exemplo é quando nós utilizamos o __getitem__ para fazer nossa classe conter
uma lista (que agora) -- se comportar como uma lista -- em vez de simplesmente ser
uma lista.
    Isso é o que é chamado de duck-typing: acontece quando não precisamos nos 
preocupar 'existencialmente' se alguma coisa é ou não um pato, mas apenas se 
tem bico de pato, se tem pena de pato ou se faz 'quá quá'.
    O mesmo acontece com o __len__ , que, embora não torne o objeto uma lista, 
faz ele reconhecer propriedades de um sized.
'''



# =============================================================================
# Herança múltipla
# =============================================================================

'''
    A gente pode pegar comportamentos mais gerais de duas classes e misturar numa nova:
É muito simples de fazer em Python, porém não são todas as linguagens que dão
suporte à herança múltipla.
'''

# Class (mãe_1, mãe_2, ..., mãe_n):
    #pass

'''
    Ele chama a partir da esquerda para a direita.
    Na verdade, um algoritmo chamado MRO que acaba por selecionar 'adequadamente' 
a ordem de onde se vai tentar buscar tal método. No caso, ele vai atrás da 
primeira que aparece e, em seguida, de seus antecessores. Depois, ele vai para 
a segunda classe.
    Porém, se duas classes tiverem um ancestral em comum, ele é removido da linha
de sucessão naquele ponto e jogado para posteriori.

    MIXINS: Os mixins são classes herdadas que não precisam ser instanciadas e 
contém preocupações comuns a diversas classes.
NÃO ENTENDI BEM COMO USAR!
'''