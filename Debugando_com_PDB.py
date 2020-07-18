# -*- coding: utf-8 -*-
"""
PDB - Python Debugger

Para utilizar o Python Debugger, precisamos* importar a biblioteca pdb, e então utilizar a função set_trace()

* A partir do Python 3.7, não é mais necessário importar a biblioteca pdb, pois o comando de debug foi
  incorporado como função built-in, chamada breakpoint()

Comandos básicos do PDB
-----------------------
- l (listar onde estamos no código)
- n (próxima linha)
- p (imprime variável)
- c (continua a execução - finaliza o debug)
"""
import pdb

nome = 'Angelina'
sobrenome = 'Jolie'
#pdb.set_trace()
#breakpoint()
nome_completo = nome + ' ' + sobrenome
curso = 'Programção em Python'
final = nome_completo + ' faz o curso: ' + curso
print(final)