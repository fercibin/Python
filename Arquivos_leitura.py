# -*- coding: utf-8 -*-
"""
Abrindo um arquivo
------------------
- A funcao open() retorna um objeto manipulador de arquivo, que e um objeto iteravel usado para realizar operacoes
  sobre um arquivo.
- Sintaxe
  manipulador = open(arquivo,modo)
  arquivo -  e uma string que indica o nome / caminho do arquivo
  modo - e opcional

Ler um arquivo
--------------
- read()
  Retorna o conteudo do arquivo como uma unica string

- readline()
  Retorna uma linha do texto a cada chamada, na ordem em que aparecem no arquivo

- readlines()
  Retorna uma lista de valores de string do arquivo, sendo que cada string corresponde a uma linha do arquivo

Fechar o arquivo
----------------
- arquivo.close()

"""

# Testando os metodos read(), readline() e readlines()

manipulador = open('arquivo.txt', 'r')

print("\nMetodo read() :\n")
print(manipulador.read())

manipulador.seek(0) # Volta para o inicio do arquivo

print("\nMetodo readline() :\n")
print(manipulador.readline())
print(manipulador.readline())

manipulador.seek(0) # Volta para o inicio do arquivo

print("\nMetodo readlines() :\n")
print(manipulador.readlines())

manipulador.close()

# 01
print("\nUsando rstrip()\n")
arq = open('arquivo.txt', 'r')
for linha in arq:
    linha = linha.rstrip()
    print(linha)
arq.close()


# 02
print("\nContando a quantidade de linhas de um arquivo de texto")
contador = 0
arq = open('arquivo.txt', 'r')
for linha in arq:
    contador = contador + 1
print("Numero de linhas no arquivo:", contador)
arq.close()

# 03
print("\nRetornando somente as linhas que possuem a palavra Python:")
arq = open('arquivo.txt', 'r')
contador = 0
for linha in arq:
    linha = linha.rstrip()
    if 'Python' in linha:
        contador = contador + 1
        print(linha)
print("\nForam encontradas %d linhas " %contador)
arq.close()

# 04
print("\nRetornando somente as linhas que possuem a palavra especificada:")
arq = open('arquivo.txt', 'r')
palavra = input("Digite a palavra para busca: ")
contador = 0
for linha in arq:
    linha = linha.rstrip()
    if palavra in linha:
        contador = contador + 1
        print(linha)
print("\nForam encontradas %d linhas " %contador)
arq.close()