# -*- coding: utf-8 -*-
"""
Funções de Maior Grandeza - Higher Order Function - HOF
-------------------------

- Quando uma linguagem de programação suporta HOF, indica que podemos ter funções que retornam outras funções
  como resultado, ou que podemos passar funções como parâmetros para outras funções, e até mesmo criar
  variáveis do tipo função nos nossos programas.

"""
# Exemplo - Definindo as funções

def somar(a, b):
    return a + b

def diminuir(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    return a / b

def calcular(num1, num2, funcao):
    return funcao(num1, num2)

# Testando

print(calcular(4, 3, somar))
print(calcular(4, 3, diminuir))
print(calcular(4, 3, multiplicar))
print(calcular(4, 3, dividir))

"""
Funções Aninhadas
-----------------
"""
# Exemplo
from random import choice

def cumprimento(pessoa):
    def humor():
        return choice(('E aí ', 'Suma daqui ', 'Gosto muito de você '))
    return humor() + pessoa

print(cumprimento('Angelina'))
print(cumprimento('Luana'))

def cumprimento(pessoa):
    return choice(('E aí ', 'Suma daqui ', 'Gosto muito de você ')) + pessoa

print(cumprimento('Tonha'))