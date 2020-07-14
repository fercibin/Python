"""
Dictionary Comprehension
------------------------
Pense no seguinte:

- Criar uma lista
lista = [1, 2, 3, 4, 5]

- Criar uma tupla
tupla = (1, 2, 3, 4, 5)

- Criar um conjunto
conjunto = {1, 2, 3, 4, 5}

- Criar um dicionário
dicionario = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}

"""
# Exemplos

dicionario = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}

quadrado = {chave:valor ** 2 for chave, valor in dicionario.items()}
print(quadrado)

print("**********************************************")

chaves = 'abcde'
valores = [1, 2, 3, 4, 5]

mistura = {chaves[i]: valores[i] for i in range(0, len(chaves))}
print(mistura)

# Exemplo condicional
valores = [1, 2, 3, 4, 5]

res = {num: ('par' if num % 2 == 0 else 'impar') for num in valores}
print(res)