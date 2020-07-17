# -*- coding: utf-8 -*-
"""
LAMBDAS
-------
Expressões lambdas são funções anônimas, ou seja, sem nome.

"""
# Exemplo Função
def funcao(x):
    return 3 * x + 1

print(funcao(6))

# Expressão Lambda
lambda x: 3 * x + 1

calc = lambda x: 3 * x + 1

print(calc(6))

print("**********************************************")


# Podemos ter expressões lambdas com múltiplas entradas
nome_completo = lambda nome, sobrenome: nome.strip().title() + ' ' + sobrenome.strip().title()

print(nome_completo('angelina', 'JOLIE'))
print(nome_completo(' FELICITY ', ' jones'))

print("**********************************************")

"""
Função Quadrática
F(x) = a * x ** 2 + b * x + c
"""
# Definindo a função

def funcao_quadratica(a, b, c):
    return  lambda x: a * x ** 2 + b * x + c

teste = funcao_quadratica(2, 3, -5)

print(teste(0))
print(teste(1))
print(teste(2))

# Outra forma de utilizar, passando o x 

print(funcao_quadratica(2, 3, -5)(2))


