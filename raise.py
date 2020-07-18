# -*- coding: utf-8 -*-
"""
RAISE - Levantando os próprios erros com raise
-----

raise -> Lança exceções, não é uma função, é uma palavra reservada.

A forma geral de utilização é:

raise TipoDoErro('Mensagem de erro')

"""
# Exemplo

def colore(texto, cor):
    cores = ('verde', 'azul', 'vermelho', 'preto', 'amarelo')
    if type(texto) is not str:
        raise TypeError ('texto precisa ser string')
    if type(cor) is not str:
        raise TypeError ('cor precisa ser string')
    if cor.lower() not in cores:
        raise ValueError(f'A cor {cor} não pode ser utilizada.')
    print(f'O texto {texto} será impresso na cor {cor}')

colore('Fernando', 'Preto')
#colore(95, 'azul')


