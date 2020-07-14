# -*- coding: utf-8 -*-
"""
FUNCOES RECURSIVAS
------------------
- Recursao e um metodo de simplificacao que consiste em dividir um
  problema em subproblemas do mesmo tipo.
- Os subproblemas sao resolvidos, e seus resultados combinados.
- Uma funcao recursiva e uma funcao que chama a si propria quando
  invocada.

Exemplo de recursividade: Calculo de Fatorial
- O fatorial de um numero corresponde ao produto desse numero pelo
  fatorial de seu numero antecessor:

fatorial(num) = 1, se num = 0 ou num = 1, e
fatorial(num) = num * fatorial(num-1) para num > 1

Fatorial de 4 (4!):

4*fatorial(3)=
4*3*fatorial(2)=
4*3*2*fatorial(1)=
4*3*2*1 = 24
"""
def fatorial(numero):
    if numero == 0 or numero == 1:
        return 1
    else:
        return numero * fatorial(numero - 1)

x = int(input("Digite um numero para calcular seu fatorial: \n"))
resultado = fatorial(x)
print("O fatorial de %d e %d" % (x, resultado))

print("**********************************************")

'''
Fibonacci recursivo

A sequencia de Fibinacci comeca com os numeros 0 e 1, e os valores
seguintes sao a soma dos anteriores:
0,1,1,2,3,5,8,13,21,34,55,...

Assim, temos a formula geral:

fibo(num) = num, se num <= 1, e
fibo(num) = fibo(num-1) + fibo(num-2) para num > 1
'''
def Fibonacci(num):
    if num <= 1:
        return num
    else:
        return Fibonacci(num-1) + Fibonacci(num-2)

x = int(input("Digite um numero para calcular seu fibonacci: \n"))
res = Fibonacci(x-1)
print("O fibonacci de %d e %d" % (x, res))
