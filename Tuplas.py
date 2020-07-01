'''
TUPLAS
------
- Uma tupla e uma especie de lista que nao pode ser alterada - imutavel -
  ou seja, e uma sequencia como uma lista, mas nao pode ser alterada, como
  uma string.
- Sao codificadas entre parenteses, e suportam tipos diferentes de dados,
  aninhamentos e operacoes de sequencias.
Ex:
T = ('abacaxi', 'abacate', 'carambola', 'pitanga', 'goiaba')
U = ('palavra', 7, ['a', 'b', 'c'])
'''
# Operacoes com tuplas

T = ('abacaxi', 'abacate', 'carambola', 'pitanga', 'goiaba')
U = ('palavra', 7, ['a', 'b', 'c'])

print (len(T)) # Retorna o comprimento da tupla
print(len(U))
print("**********************************************")

print(T.index('carambola')) # Retorna a posicao do elemento na tupla
print(T[2])
print(U.index(7))
print(U[2][0])
print("**********************************************")

print(T.count('carambola')) # Retorna a quantidade de ocorrencias do item na tupla
