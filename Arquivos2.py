# -*- coding: utf-8 -*-
"""
Escrever em arquivo
-------------------
- Abrir o arquivo com a funcao open()

- Depois de aberto, usamos a funcao write() para escrever
  arquivo.write(texto_a_ser_escrito)

"""

# Criando e escrevendo em arquivos de texto (modo 'w')

arquivo = open('arq01.txt', 'w')
arquivo.write("Arquivo criado para teste\n")
arquivo.write("Criando arquivo de texto com Python\n")
arquivo.write("Arquivo criado por Fernando\n")
arquivo.write("E isso ai pessoal!\n")
arquivo.close()

# Lendo o arquivo criado:
arquivo = open('arq01.txt', 'r')
for linha in arquivo:
    linha = linha.rstrip()
    print(linha)
arquivo.close()

# Acrescentando texto ao arquivo criado (modo 'a')

print("\n")
texto = input("Digite uma frase para acrescentar ao arquivo: ")
arq = open('arq01.txt', 'a')
arq.write(texto + "\n")
print("Operacao concluida no arquivo " + arq.name + "\n")
arq.close()

print("Texto alterado:\n")
arquivo = open('arq01.txt', 'r')
for linha in arquivo:
    linha = linha.rstrip()
    print(linha)
arquivo.close()