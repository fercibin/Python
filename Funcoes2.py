# -*- coding: utf-8 -*-
'''
FUNCOES - Escopos de Variaveis
------------------------------
- O escopo de uma variavel define sua visibilidade-onde, no codigo, a
  variavel e acessivel. Temos dois escopos em Python:

- Escopo Local
  ------------
  - Uma variavel LOCAL (criada dentro de uma funcao) existe apenas dentro
    da funcao onde foi declarada
  - É inicializada a cada chamada da funcao
  - Nao e possivel acessar seu valor fora da funcao onde ela foi declarada.

- Escopo Global
  -------------
  - Uma variavel GLOBAL e declarada fora das funcoes e pode ser acessada
    por todas as funcoes do modulo onde foi definida.
  - Variaveis globais tbm podem ser acessadas por outros modulos, caso eles
    importem o modulo onde a variavel foi definida.

'''
VAR_GLOBAL = 'Curso de Python'
def escreve_texto():
    VAR_GLOBAL = 'Planeta Linux'
    VAR_LOCAL = 'Fernando Cibin'
    print('Variavel global: ', VAR_GLOBAL)
    print('Variavel local: ', VAR_LOCAL)
print('Executando a funcao escreve_texto:')
escreve_texto()
print('Tentando acessar as variaveis diretamente:')
print('Variavel global: ', VAR_GLOBAL)

print("**********************************************")

VAR_GLOBAL = 'Curso de Python'
def escreve_texto():
    global VAR_GLOBAL # Alteracao feita na funcao reflete na variavel externa
    VAR_GLOBAL = 'Planeta Linux'
    VAR_LOCAL = 'Fernando Cibin'
    print('Variavel global: ', VAR_GLOBAL)
    print('Variavel local: ', VAR_LOCAL)
print('Executando a funcao escreve_texto:')
escreve_texto()
print('Tentando acessar as variaveis diretamente:')
print('Variavel global: ', VAR_GLOBAL)
