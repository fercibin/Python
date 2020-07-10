"""
Módulo Collections - Named Tuple - namedtuple()

Named Tuple -> São tuplas diferenciadas, onde especificamos nome e parâmetros.
"""
from collections import namedtuple

# Recap tupla
tupla = (1, 2, 3)
print(tupla[1])
print(type(tupla))
# Named Tuple
# Forma 1
cachorro = namedtuple('cachorro', 'idade raca nome')

# Forma 2
cachorro = namedtuple('cachorro', 'idade, raca, nome')

# Forma 3
cachorro = namedtuple('cachorro', ['idade', 'raca', 'nome'])

# Usando
ray = cachorro(idade=2, raca='Lazarento', nome='Ray')
print(ray)
print(type(cachorro))
print(type(ray))
print("**********************************************")

# Acessando 1
print(ray[0])  # idade
print(ray[1])  # raca
print(ray[2])  # nome
print("**********************************************")

# Acessando 2
print(ray.idade)
print(ray.raca)
print(ray.nome)

# Recap verificando o index e a quantidade de ocorrências

print(ray.index('Lazarento'))

print(ray.count('Lazarento'))