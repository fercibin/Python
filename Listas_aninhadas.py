"""
Listas Aninhadas

- Algumas linguagens de programação (C, C++, Java, etc...) possuem uma estrutura de dados chamadas de arrays:
    - Unidimensionais (Arrays/Vetores)
    - Multidimensionais (Matrizes)

- Em Python temos Listas

"""
# Exemplos

listas = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# Acesso aos dados

print(listas[0][1])  # número 2
print(listas[2][0])  # número 7

print("**********************************************")

# Iterando com loops em uma lista aninhada

for lista in listas:
    for num in lista:
        print(num)

# List Comprehension

listas2 = [[valor * 3 for valor in lista] for lista in listas]
print(listas2)

print("**********************************************")

# Gerando uma matriz 3x3

Matriz = [[numero for numero in range(1, 4)] for valor in range(1, 4)]
print(Matriz)

# Gerando valores iniciais
print([['*' for i in range(1, 4)] for j in range(1, 4)])