"""
Loop FOR
--------

- C ou C++
----------
for (int i=0, 1< 10, i++) {
    // bloco de instruções
}

Python
------
for x in iterável:
    // bloco de instrução

Utilizamos loops para iterar sobre sequências ou sobre valores iteráveis.
Exemplos de iteráveis:
- String
- Lista
- Range

"""
string = 'Curso Python'
lista = [1, 3, 5, 7, 9]
index = range(0, 10)

# Iterando em uma String
for letra in string:
    print(letra)

for letra in string:
    print(letra, end='')

print("\n----------------------------------------")

# Iterando em uma lista
for numero in lista:
    print(numero)
print("----------------------------------------")

# Iterando sobre um range - Vai de zero até 10-1 (9)
for index in range(0, 10):
    print(index)
print("----------------------------------------")

asteristico = '*'
for x in range(1, 16):  # rodar 15 vezes, de 1 a 15
    print(asteristico * x)

"""
Tabela de emoji unicode: https://apps.timwhitlock.info/emoji/tables/unicode
Exemplo de um emoji convertido (trocar o sinal de '+' por '000' (3 zeros)
Original  : U+1F60D
Convertido: U0001F60D
"""
for _ in range(3):  # Vai executar esse loop 3 vezes
    for num in range(1, 4):
        print('\U0001F61D' * num)

qtd = int(input("Quantas vezes rodar o loop?"))

for num in range(1, qtd + 1):
    print('\U0001F60D' * num)

var = 'Python'
for x in var:
    print(x)
print("**********************************************")

frutas = ['laranja', 'morango', 'guarana', 'melancia', 'mamao']
for y in frutas:
    print("Fruta: %s" % y)
print("**********************************************")

'''
Loop FOR com contador
--------
- Funcao range() - Gera uma lista contendo uma progressao aritmetica
- Sintaxe
range(inicio, fim, salto)

- Inicio e salto sao opcionais
'''
for x in range(1, 11):
    print(x)

for w in range(0, 51, 5):
    print(w)

for w in range(1, 51, 5):
    print(w)
