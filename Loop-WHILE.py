'''
Loop while
----------
- Estrutura de repeticao que permite executar um bloco de codigo enquanto
  a condicao de teste retornar verdadeiro.
- Sintaxe:
while (condicao):
    Bloco de codigo.
'''
contador = 1
while (contador <= 9):
    print('O valor do contador e %d' %contador)
    contador+=1
print('Loop encerrado')

# WHILE com variavel de controle
controle = ''
while (controle != 's'):
    print('a. Pagar')
    print('b. Receber')
    print('c. Consultar')
    print('s. Sair')
    controle = input('Digite a opcao desejada:')
print('Loop encerrado')

'''
WHILE com BREAK
---------------
- O comando BREAK termina o loop atual e prossegue a execucao na proxima
  declaracao apos o Loop.
- O comando BREAK pode ser usado em loops WHILE e for.
 '''
var = 20
while (var > 0):
    print('O valor de var e %d' %var)
    var-=1
    if (var == 11):
        break
print('Loop interrompido no valor %d' %var)
