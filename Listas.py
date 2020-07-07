"""
LISTAS
------
- Listas em Python funcionam como vetores/matrizes em outras linguagens, com a diferenca de serem DINAMICAS,
  e tambem podermos colocar QUALQUER tipo de objetos(strings, boolean, etc).

- Uma lista pode conter outras listas como objetos.

- Seu conteudo pode ser modificado - nao sao imutaveis como strings.

- Seus objetos sao acessados a partir de um indice.

- Suporta metodos que nao sao suportados pelas strings.

- Listas sao representadas por colchetes []

"""
import math

# Criar listas
L = []
L = [0, 1, 2, 3, 4]
L = ["a", "b", "c"]
L = ["a", ["b", "c"]]

# Metodos suportados por listas

# L1 + L2   Concatenacao
L1 = [0, 1, 2, 3, 4]
L2 = [5, 6, 7, 8, 9]
L3 = L1 + L2
print('L1 + L2:', L1 + L2)

# L * 5     Repeticao
L = [1, 2, 3]
print('L * 5:', L * 5)

# <valor> in L      Verificacao de existencia
if 2 in L:
    print("O numero esta na lista")
else:
    print("O numero nao esta na lista")

# L.append(x)       Acrescentar itens
L = [1, 2, 3, 7]
print(L)
L.append(9)
print(L)

#  L.insert(POS,x)    Acrescentar item na posicao especificada. Nao substitui o valor inicial,
#                     o mesmo sera deslocado para a direita.
L.insert(3, 5)
print(L)

# L.index(x)    Busca posicao de valor x
L = [11, 22, 33, 35, 57, 11, 77, 79]
print(L.index(35))

# L.count(x)    Conta a quantidade de ocorrencias do valor x
print(L.count(11))

# len(L)        Retorna o tamanho da lista
L = [0, 1, 2, 3, 4]
print(len(L))  # vai retornar o valor 5

# L[i] = x      Atribui o valor x a posicao i da listas
L = [7, 5, 9, 12, 3, 5]
print(L)
L[3] = 17
print(L)
print("**********************************************")

# L[i:j] = [x1, x2, x3...]  Atribui valores ao intervalo
L = [7, 5, 9, 12, 3, 5, 77, 99]
print(L)
L[1:3] = ["a, b, c", 1024, 7.00]
print(L)
print("**********************************************")

# L2 = [x+n for x in L] Criar a lista L2 com os elementos de L
#                       incrementados em n
#                       Pode ser qualquer outro calculo
L = [5, 7, 9, 12, 15, 25]
print(L)
L2 = [x + 1 for x in L]
print(L2)

L = [5, 7, 9, 12, 15, 25]
print(L)
L2 = [x * 3 for x in L]
print(L2)

L = [5, 7, 9, 12, 15, 25]
print(L)
L2 = [x ** 2 for x in L]
print(L2)

L3 = [math.sqrt(x) for x in L2]
print(L3)
print("**********************************************")

# Desempacotamento de listas
# A quantidade de variáveis devem ser iguais à quantidade de elementos da lista
print('Desempacotamento de listas')
lista = [1, 2, 3]

num1, num2, num3 = lista

print(num1, num2, num3)
print("**********************************************")
# Metodos suportados por listas

# L.sort()      Ordenar listas
L = [0, 1, 2, 12, 3, 4, 9, 11, 2, 7, 2]
L2 = [7, 5, 9, 12, 3]
L.sort()
print(L)
print(sorted(L2))
print("**********************************************")

# L.reverse()   Reverter a listas
L = [0, 1, 2, 12, 3, 4, 9, 11, 2, 7, 2]
L.reverse()
print(L)
print("**********************************************")

# L.remove(x)   Remover a primeira ocorrencia do item
L2 = [7, 5, 9, 12, 3, 5]
L2.remove(5)
print(L2)
print("**********************************************")

# L.pop(POS)    Remove o item na posicao de INDICE especificado
L2 = [7, 5, 9, 12, 3, 5]
L2.pop(3)
print(L2)
print("**********************************************")

# del L[POS]    Remove o item na posicao de INDICE especificado
L2 = [7, 5, 9, 12, 3, 5]
del L2[3]
print(L2)
print("**********************************************")

# del L[i:j]     Remove os itens da posicao i ate j-1
L = [0, 1, 2, 12, 3, 4, 9, 11, 2, 7, 2]
del L[1:4]
print(L)
print("**********************************************")

# Converter uma lista em string
L3 = ['Programacao', 'em', 'Python:', 'Essencial']
print(L3)
curso = ' '.join(L3)  # Aqui estamos usando o espaço para formar a string, poderia ser outro caractere.
print(curso)
print("**********************************************")

# Converter uma string em lista
string = 'Programacao em Python: Essencial'
print(string)
lista = string.split(' ')  # Estamos usando o espaço como separador de string, poderia ser outro caractere qualquer.
print(lista)

cores = ['azul', 'preto', 'verde', 'amarelo', 'vermelho']

indice = 0
while indice < len(cores):
    print(cores[indice])
    indice = indice + 1

# Gerar indice em um laço FOR

for (indice, cor) in enumerate(cores):
    print(indice, cor)