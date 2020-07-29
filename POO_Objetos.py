# -*- coding: utf-8 -*-
"""
Objetos
-------
- Objetos são instâncias da classe.

- Podemos pensar nos objetos/instâncias de uma classe como sendo variáveis do tipo definido na classe.

"""

class Lampada:
    def __init__(self, cor, voltagem):
        self.cor = cor
        self.voltagem = voltagem
        self.ligada = False

    def checa_lampada(self):
        return self.ligada

    def ligar_desligar(self):
        if self.ligada:
            self.ligada = False
        else:
            self.ligada = True

# Instâncias/Objetos
lamp1 = Lampada('branca', 110)

lamp2 = Lampada('amarela', 220)

print(f'A lâmpada está ligada? {lamp1.checa_lampada()}')

lamp1.ligar_desligar()

print(f'A lâmpada está ligada? {lamp1.checa_lampada()}')


