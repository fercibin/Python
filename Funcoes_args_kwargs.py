# -*- coding: utf-8 -*-
"""
*args e **kwargs NÃO SÃO OBRIGATÓRIOS
-------------------------------------

- Observe que a funcao abaixo exige quatro parametros de entrada
"""


# DESEMPACOTAMENTO

# Funcao para listar os itens
def listar_itens(w, x, y, z):
    print(w, x, y, z)


lista = [13, 15, 17, 19]

# Tentando listar os itens diretamente desta forma da erro
# listar_itens(lista)

# O asterisco sinaliza para a funcao que o elemento 'lista' precisa ser desempacotado antes de ser
# passado para os parametros da funcao

listar_itens(*lista)

# Outro exemplo

lista2 = [1, 2, 3, 4, 5]
n1, n2, *n = lista2  # O *n vai receber o restante da lista
print(n1, n2, n)  # Vai mostrar:  1 2 [3, 4, 5]

print("**********************************************")

"""
*args
-----
Os argumentos passados são convertidos em uma TUPLA, sendo possível realizar todas as operações, 
e utilizar todas as funções e métodos disponíveis quando trabalhamos com tuplas.

"""


def somar(*args):
    soma = 0
    for i in range(0, len(args)):
        soma += args[i]
    return soma


print(somar(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))
print(somar(77, 23))

lista = [11, 13, 15, 17, 19]

print(somar(*lista))  # DESEMPACOTAMENTO utilizando o asterisco

print("**********************************************")

"""
**kwargs
-----
Este é só mais um parâmetro, mas diferente do *args, que coloca os argumentos extras em uma tupla, o **kwargs
exige que utilizemos parâmetros nomeados, e converte estes parâmetros extras em um DICIONÁRIO.

"""


# Exemplo 1

def cores_favoritas(**kwargs):
    for pessoa, cor in kwargs.items():
        print(f'A cor favorita de {pessoa.title()} é {cor}')


cores_favoritas(marcos='verde', julia='vermelho', fernando='preto')

print("**********************************************")


# Exemplo 2

def cumprimento_especial(**kwargs):
    if 'geek' in kwargs and kwargs['geek'] == 'Python':
        return 'Você recebeu um cumprimento Pythonico'
    elif 'geek' in kwargs:
        return f"{kwargs['geek']} chato pra kct!"
    else:
        return 'Não tenho certeza quem vc é...'


print(cumprimento_especial())

print(cumprimento_especial(geek='Python'))

print(cumprimento_especial(geek='Oi'))


# Exemplo 3

def mostra_nomes(**kwargs):
    return f"{kwargs['nome']} {kwargs['sobrenome']}"


nomes = {'nome': 'Fernando', 'sobrenome': 'Cibin'}

print(mostra_nomes(**nomes))  # DESEMPACOTAMENTO utilizando o duplo asterisco
