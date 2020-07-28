# -*- coding: utf-8 -*-
"""
Classes
-------
Em POO, CLASSES nada mais são que modelos dos objetos do mundo real sendo representados computacionalmente.

Classes podem conter:
  - Atributos -> Representam as características do objeto, ou seja, pelos atributos conseguimos representar
                 computacionalmente os estados de um objeto.No caso da lâmpada, se é 110 ou 220 volts, se é luz branca,
                 amarela ou outra cor, qual a luminosidade dela, etc...

  - Métodos (funções) -> Representam os comportamentos do objeto, ou seja, as ações que este objeto pode realizar no
                         sistema. No caso da lâmpada, ligar e desligar a mesma.
"""

class Lampada:
    pass

lamp = Lampada()

print(lamp)
print(type(lamp))