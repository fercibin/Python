# -*- coding: utf-8 -*-
"""
Bloco try / except / else / finally
-----------------------------------
Dica:

TODA ENTRADA DE DADOS DEVE SER TRATADA

O finally geralmente é utilizado para fechar ou deslocar recursos (conexão com banco de dados, fechar arquivos...)

"""

# ELSE - o bloco else é executado somente se não ocorrer o erro.
try:
    num = int(input('Informe um número:'))
except ValueError:
    print('Valor incorreto.')
else:
    print(f'Você digitou: {num}')

# FINALLY - o bloco finally é SEMPRE executado, indiferente se houve exceção.
try:
    num = int(input('Informe um número:'))
except ValueError:
    print('Valor incorreto.')
else:
    print(f'Você digitou: {num}')
finally:
    print('Executando o finally')
