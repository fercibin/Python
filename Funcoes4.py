# -*- coding: utf-8 -*-
'''
FUNCOES
-------
Empacotamento e Desempacotamento de parametros

- Observe que a funcao abaixo exige quatro parametros de entrada
'''

# DESEMPACOTAMENTO

# Funcao para listar os itens
def listar_itens(w, x, y, z):
    print(w, x, y, z)

lista = [13, 15, 17, 19]

# Tentando listar os itens diretamente desta forma da erro
# listar_itens(lista)

# Tentando listar os itens com o operador. O asterisco sinaliza para a
# funcao que o elemento 'lista' precisa ser desempacotado antes de ser
# passado para os parametros da funcao
listar_itens(*lista)
print("**********************************************")

# EMPACOTAMENTO - Desta forma consegue-se passar um numero indeterminado
                # de parametros

def somar(*args):
    soma = 0
    for i in range (0, len(args)):
        soma += args[i]
    return soma

print(somar(1,2,3,4,5,6,7,8,9,10))
print(somar(77,23))

lista = [11, 13, 15, 17, 19]
print(somar(*lista))
