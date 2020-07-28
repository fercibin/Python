# -*- coding: utf-8 -*-
"""
List Comprehension
------------------
- Utilizando List Comprehension, podemos gerar novas listas com dados processados a partir de outro iterável.

- Pode-se utilizar estruturas condicionais nas List Comprehension - Exemplos abaixo

"""
import math

# Exemplos
from typing import List

numeros = [1, 2, 3, 4, 5]

# Para cada número na lista 'numeros' acima, gerar a lista 'res1' multiplicando cada número por 10:

res1 = [numero * 10 for numero in numeros]
print(res1)

# Para cada número na lista 'numeros' acima, gerar a lista 'res2' elevando cada número ao quadrado:

res2 = [math.pow(numero, 2) for numero in numeros]
print(res2)

amigos = ['andré', 'léo', 'tião']
amiup = [nome.title() for nome in amigos]
print(amiup)

"""
List Comprehension com CONDICIONAIS
"""
numeros = [1, 2, 3, 4, 5, 6, 7]

pares = [numero for numero in numeros if numero % 2 == 0]
impares = [numero for numero in numeros if numero % 2 != 0]
print(pares)
print(impares)


# Pegar os valores divisíveis por 3 e por 8 numa lista

lista = list(range(100))
div3_8 = [v for v in lista if v % 3 == 0 and v % 8 == 0]
print(div3_8)

# Usando ELSE - No exemplo abaixo, vai colocar / nos lugares dos números que não forem divisíveis por  3 e 8
ex7 = [v if v % 3 == 0 and v % 8 == 0 else '/' for v in lista]
print(ex7)

