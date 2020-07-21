# -*- coding: utf-8 -*-
"""
Sistemas de Arquivos - Manipulação

"""
import os

# Descobrir se um arquivo existe
print(os.path.exists('arquivo.txt'))  # Retorna True ou False

# Descobrir se um diretorio existe
# Path relativo
print(os.path.exists('diretorio'))  # Retorna True ou False

# Path absoluto
print(os.path.exists('/home/fernando/Cursos/Python'))  # Retorna True ou False

"""
Criando Arquivos
----------------
-  mknod() cria um arquivo se ele não existir, retorna erro se existir. 
"""
# Forma 1
open('arquivo-teste1.txt', 'w').close()

# Forma 2
with open('arquivo-teste2.txt', 'w') as arq:
    pass

# Forma 3
# Path relativo
os.mknod('arquivo-teste3.txt')

# Path absoluto
# os.mknod('/home/fernando/arquivo-teste.txt')

"""
Criando Diretórios
- mkdir() cria um diretório se ele não existir, retorna erro se existir.
------------------
"""
# Path relativo
os.mkdir('diretorio1-teste')

os.makedirs('diretorio2-teste2/outro-diretorio/mais-um-diretorio')

# Path absoluto
# os.mkdir('/home/fernando/diretorio-teste')

"""
Renomear Arquivos / Diretórios
"""
os.rename('diretorio1-teste', 'diretorio-renomeado')
os.rename('arquivo-teste3.txt', 'arquivo-renomeado.txt')

"""
Apagar Arquivos / Diretórios
"""
os.remove('arquivo-teste1.txt')
os.remove('arquivo-teste2.txt')
os.remove('arquivo-renomeado.txt')
os.removedirs('diretorio-renomeado')
os.removedirs('diretorio2-teste2/outro-diretorio/mais-um-diretorio')
