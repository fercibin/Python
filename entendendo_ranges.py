"""
Ranges
------
Ranges são utilizados para gerar sequências numéricas, não aleatória, de forma específica.

Formas Gerais:

# Forma 1

range(valor_fim)

Obs: valor_fim não inclusive (início padrão 0, incremento de 1 em 1)


# Forma 2

range(valor_início, valor_fim)

Obs: valor_fim não inclusive (início especificado pelo usuário, incremento de 1 em 1)


# Forma 3

range(valor_início, valor_fim, valor_incremento)

Obs: valor_fim não inclusive (início especificado pelo usuário, incremento especificado pelo usuário)
"""

# Forma 1
for num in range(9):
    print(num, end=' ')
print("\n----------------------------------------")

# Forma 2
for num in range(1, 8):
    print(num, end=' ')
print("\n----------------------------------------")

# Forma 3
for num in range(1, 12, 2):
    print(num, end=' ')
print("\n----------------------------------------")


