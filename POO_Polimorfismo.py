# -*- coding: utf-8 -*-
"""
Polimorfismo
------------

"""
class Animal:

    def __init__(self, nome):
        self.__nome = nome

    def falar(self):
        raise NotImplementedError('A classe filha precisa implementar este método.')

    def comer(self):
        print(f'{self.__nome} está rangando.')

class Cachorro(Animal):

    def __init__(self, nome):
        super().__init__(nome)

    def falar(self):
        print(f'Cachorro falante de merda!')


class Gato(Animal):

    def __init__(self, nome):
        super().__init__(nome)

    def falar(self):
        print(f'Gato falante de merda!')


class Rato(Animal):

    def __init__(self, nome):
        super().__init__(nome)


cachorro = Cachorro('Pluto')
cachorro.comer()
cachorro.falar()

gato = Gato('Bichano')
gato.comer()
gato.falar()

rato = Rato('Bichano')
rato.comer()
# rato.falar()

