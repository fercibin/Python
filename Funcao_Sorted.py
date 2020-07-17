# -*- coding: utf-8 -*-
"""
SORTED()
--------
- sorted() pode ser utilizado com qualquer iterável, serve para ordenar.
- SEMPRE retorna como resultado uma LISTA com os elementos ordenados, não altera a coleção original

- sort() só funciona em lista.
  Altera a lista original
"""
numeros = [9, 1, 7, 3, 12]
print(numeros)
print(sorted(numeros))

# Adicionando parâmetros ao sorted()

print(sorted(numeros, reverse=True))  # Ordena do maior para o menor

# Podemos utilizar sorted() para coisas mais complexas

usuarios = [
    {'username': 'Samuel', 'tweets': ['Eu adoro bolos', 'Eu adoro pizza']},
    {'username': 'Carla', 'tweets': ['Eu amo meu gato']},
    {'username': 'jeff', 'tweets': []},
    {'username': 'bob123', 'tweets': []},
    {'username': 'Doggo', 'tweets': ['Eu gosto de cachorro', 'Vou pra zona hoje']},
    {'username': 'gal', 'tweets': []}
]

print(usuarios)

# Ordenando por username
print(sorted(usuarios, key=lambda usr: usr['username']))

# Ordenando pela quantidade de tweets
print(sorted(usuarios, key=lambda usr: len(usr['tweets'])))
