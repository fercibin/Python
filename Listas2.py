'''
- Lista e um tipo de objeto que representa uma colecao ordenada.
- As listas podem conter qualquer tipo de objetos (strings, boolean, etc)
- Seu conteudo pode ser modificado - nao sao imutaveis como strings.
- Seus objetos sao acessados a partir de um indice.
- Uma lista pode crescer e diminuir de tamanho.
- Uma lista pode conter outras listas como objetos.
- Suporta metodos que nao sao suportados pelas strings.
'''
import math

# Criar listas
l = []
l = [0, 1, 2, 3, 4]
l = ["a", "b", "c"]
l = ["a", ["b", "c"]]

# len(L)        Retorna o tamanho da lista
l = [0, 1, 2, 3, 4]
print(len(l)) # vai retornar o valor 5

# L[i] = x      Atribui o valor x a posicao i da listas
L = [7, 5, 9, 12, 3, 5]
print(L)
L[3] = 17
print(L)
print("**********************************************")

# L[i:j] = [x1, x2, x3...]  Atribui valores ao intervalo
L = [7, 5, 9, 12, 3, 5, 77, 99]
print (L)
L[1:3] = ["a, b, c", 1024, 7.00]
print(L)
print("**********************************************")

# L2 = [x+n for x in L] Criar a lista L2 com os elementos de L
#                       inclrementados em n
#                       Pode ser qualquer outro calculo
L = [5, 7, 9, 12, 15, 25]
print(L)
L2 = [x+1 for x in L]
print(L2)

L = [5, 7, 9, 12, 15, 25]
print(L)
L2 = [x * 3 for x in L]
print(L2)

L = [5, 7, 9, 12, 15, 25]
print(L)
L2 = [x ** 2 for x in L]
print(L2)

L3 = [math.sqrt(x) for x in L2 ]
print(L3)
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
