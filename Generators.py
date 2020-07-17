"""
Generators

Em aulas anteriores estudamos:
- List Comprehension
- Dictionary Comprehension

Não vimos:
- Tuple Comprehensions... porque elas são Generators

"""
nomes = ['Carlos', 'Camila', 'Carla', 'Cristina', 'Vanessa']

# List Comprehension
res = [nome[0] == 'C' for nome in nomes]
print(type(res))
print(res)

# Generator
res = (nome[0] == 'C' for nome in nomes)
print(type(res))
print(tuple(res))