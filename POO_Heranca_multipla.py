# -*- coding: utf-8 -*-
"""
Herança Múltipla
----------------
- Herança múltipla nada mais é do que a possibilidade de uma classe herdar de múltiplas classes, fazendo com
  que a classe filha herde todos os atributos e métodos das classes herdadas.

- A Herança Múltipla pode ser feita de duas maneiras:
  - Por Multiderivação Direta
  - Por Multiderivação Indireta

# Exemplo 1 - Multiderivação Direta - Não existe limite para herança em Python, poderia ser mais que as duas classes
-----------------------------------   do exemplo abaixo.

class Base1:
    pass

class Base2:
    pass

class Multiderivada1(Base1, Base2):
    pass


# Exemplo 2 - Multiderivação Indireta
-------------------------------------

class Base1:
    pass

class Base2(Base1):
    pass

class Base3(Base2):
    pass

class Multiderivada2(Base3):
    pass

"""

class Animal:

    def __init__(self, nome):
        self.__nome = nome

    def cumprimentar(self):
        return f'Eu sou {self.__nome}!'

class Aquatico(Animal):

    def __init__(self, nome):
        super().__init__(nome)

    def nadar(self):
        return f'{self._Animal__nome} está nadando.'

    def cumprimentar(self):
        return f'Eu sou {self._Animal__nome} do mar!'

class Terrestre(Animal):

    def __init__(self, nome):
        super().__init__(nome)

    def andar(self):
        return f'{self._Animal__nome} está andando.'

    def cumprimentar(self):
        return f'Eu sou {self._Animal__nome} da terra!'

class Pinguim(Aquatico, Terrestre):

    def __init__(self, nome):
        super().__init__(nome)


# Testando

baleia = Aquatico('Baleia')
print(baleia.nadar())
print(baleia.cumprimentar())

elefante = Terrestre('Lefante')
print(elefante.andar())
print(elefante.cumprimentar())

tux = Pinguim('Tux')
print(tux.andar())
print(tux.nadar())
print(tux.cumprimentar())
print(Animal.cumprimentar(tux))

# Objeto é instância de...

print(f'Tux é instância de Pinguim? {isinstance(tux, Pinguim)}')
print(f'Tux é instância de Aquatico? {isinstance(tux, Aquatico)}')
print(f'Tux é instância de Terrestre? {isinstance(tux, Terrestre)}')
print(f'Tux é instância de Animal? {isinstance(tux, Animal)}')