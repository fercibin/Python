# -*- coding: utf-8 -*-
'''
FUNCOES
-------
- Uma funcao e um agrupamento de instrucoes que podem ser executadas mais
  de uma vez em um programa.

- Basicamente, criamos funcoes por dois motivos:
  Reutilizacao de codigo
  Modularizacao

Criando Funcoes sem argumentos
------------------------------
- Sintaxe
def <nome_funcao>(argumentos):
    <instrucoes>

Exemplo: funcao para exibir uma mensagem
def mensagem():
    print('Primeira funcao.')

Criando Funcoes com argumentos
------------------------------
-Sintaxe
def <nome_funcao>(argumentos):
    <instrucoes>

Exemplo: funcao para somar dois numeros
def soma(a,b):
    return a+b

Instrucao RETURN
----------------
def <nome_funcao>(argumentos):
    <instrucoes>
    return<valor>

- A instrucao return pode ser declarada em qualquer parte dentro de codigo
  da funcao. Quando executada, finaliza a chamada da funcao e retorna o
  resultado de volta a quem fez a chamada.
- Trata-se de uma instrucao opcional, caso nao seja utilizada, a funcao
  termina quando finalizar a execucao das instrucoes da funcao.

'''
def mensagem():
    print('Teste primeira funcao')
mensagem()
print("**********************************************")

def soma(a,b):
    return a+b

r = 7
s = 3
t = soma(r,s)
print(t)
print("**********************************************")

valores = [1, 2, 3, 4, 5]
print(valores)
def quadrado(val):
    quadrados = []
    for x in valores:
        quadrados.append(x**2)
    return quadrados

resultados = quadrado(valores)
print(resultados)
for y in resultados:
    print(y)
print("**********************************************")
