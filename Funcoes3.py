# -*- coding: utf-8 -*-
'''
FUNCOES
-------
Parametros Opcionais e Obrigatorios

- Nesse caso abaixo, ambos os parametros sao opcionais, se nao forem
  passados, a funcao usa o valor padrao declarado na funcao.
- Se nenhum valor fosse declarado como padrao, a passagem dos parametros
  se tornaria obrigatoria.
'''
def contar(valor=11, caractere = "+"):
    for i in range (1, valor):
        print(caractere)

contar()

print("Passando um caractere diferente: ")
contar(caractere="&")

print("Passando um valor diferente: ")
contar(valor=8)

print("Passando valor e caractere diferentes: ")
contar(4, "*" )

'''
O codigo abaixo, com os parametros fora de ordem retorna erro:

print("Passando valor e caractere diferentes: ")
contar("*", 4 )
'''
print("Passando os parametros fora de ordem, nomeados: ")
contar(caractere="*", valor=4 )

print("**********************************************")
