# -*- coding: utf-8 -*-
"""
Função Map
----------
Mapeamento de valores para função.

- Map é uma função que recebe dois parâmetros:
  - Primeiro, a função
  - Segundo, um iterável (lista, tupla, conjunto, etc...)

"""
import  math

# Calcular área do círculo de raio r

def area(r):
    return math.pi * (r ** 2)

raios = [2, 5, 7, 1, 0.7, 10.5]

# Forma comum
areas = []
for r in raios:
    areas.append((area(r)))

print(areas)

# Usando map
areas = map(area, raios)

print(type(areas))
print(areas)
print(list(areas))  # Conversão de areas para lista, tupla, etc...

# Map com lambda

areas = map(lambda r: math.pi * (r ** 2), raios)
print(tuple(areas))

# Outro exemplo

cidades = [('Berlim', 29), ('Cairo', 36), ('Buenos Aires', 19), ('Los Angeles', 23), ('Tokio', -3)]

# Converter de Celsius para Fahrenheit
# Lambda

c_to_f = lambda dado: (dado[0], (9 / 5) * dado[1] + 32)

print(list(map(c_to_f, cidades)))
