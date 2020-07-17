# -*- coding: utf-8 -*-
"""
Função Filter
-------------

filter() - Serve para filtrar dados de uma determinada coleção.

- A função filter() recebe dois parâmetros:
  - Primeiro uma função
  - Segundo um iterável

"""
# Biblioteca para trabalhar com dados estatísticos
import statistics

dados = [1.3, 2.7, 0.8, 4.1, 4.3, -0.1]

# calculando a média dos dados com a função mean()
media = statistics.mean(dados)
print(media)

# Filtrando os valores acima da média

res = filter(lambda x: x > media, dados)
print(type(res))
print(list(res))

# Filtrando valores diferentes de vazio ou espaço

paises = ('', 'Argentina', ' ', 'Brasil', 'Chile', '', 'Equador', '', ' ', 'Venezuela')
res = filter(lambda pais: len(pais) > 1, paises)
print(list(res))


# Exemplo mais complexo - 

usuarios = [
    {'username': 'Samuel', 'tweets': ['Eu adoro bolos', 'Eu adoro pizza']},
    {'username': 'Carla', 'tweets': ['Eu amo meu gato']},
    {'username': 'jeff', 'tweets': []},
    {'username': 'bob123', 'tweets': []},
    {'username': 'Doggo', 'tweets': ['Eu gosto de cachorro', 'Vou pra zona hoje']},
    {'username': 'gal', 'tweets': []}
]
# Filtrar os usuários que estão inativos

inativos = list(filter(lambda usr: len(usr['tweets']) == 0, usuarios))

print(inativos)