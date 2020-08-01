# -*- coding: utf-8 -*-
"""
Properties - Getters e Setters
----------------------------
- Em Linguagens de programação como o Java, ao declararmos atributos privados nas classes, costumamos criar métodos
  públicos para manipulação desses atributos. Esses métodos são conhecidos por GETTERS e SETTERS.

"""
class Produto:
    def __init__(self, nome, preco):
        self.__nome = nome
        self.__preco = preco

    # Getter
    def get_preco(self):         # Em Java criaríamos assim
        return self.__preco

    # Setter
    def set_preco(self, preco):  # Em Java criaríamos assim
        self.__preco = preco

    # Aqui criamos uma propriedade chamada preco
    @property
    def preco(self):             # Em Python usamos assim
        return self.__preco

    # Aqui criamos um SETTER para a propriedade preco criada acima
    @preco.setter
    def preco(self, novo_preco):
        self.__preco = novo_preco


    def desconto(self, percentual):
        self.__preco = self.__preco - (self.__preco * (percentual / 100))

# Exemplo usando das duas formas

p1 = Produto('Camiseta', 50)
print(p1.preco)
print(p1.get_preco())

p1.preco = 70
print(p1.preco)

p1.set_preco(90)
print(p1.get_preco())


