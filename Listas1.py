'''
- Lista e um tipo de objeto que representa uma colecao ordenada.
- As listas podem conter qualquer tipo de objetos (strings, boolean, etc)
- Seu conteudo pode ser modificado - nao sao imutaveis como strings.
- Seus objetos sao acessados a partir de um indice.
- Uma lista pode crescer e diminuir de tamanho.
- Uma lista pode conter outras listas como objetos.
- Suporta metodos que nao sao suportados pelas strings.
'''
# Criar listas
l = []
l = [0, 1, 2, 3, 4]
l = ["a", "b", "c"]
l = ["a", ["b", "c"]]

# Metodos suportados por listas

# L1 + L2   Concatenacao
L1 = [0, 1, 2, 3, 4]
L2 = [5, 6, 7, 8, 9]
L3 = L1 + L2
print(L1 + L2)

# L * 5     Repeticao
L = [1, 2, 3]
print(L * 5)

# <valor> in L      Verificacao de existencia
if 2 in L:
    print("O numero esta na lista")
else:
    print("O numero nao esta na lista")

# L.append(x)       Acrescentar itens
L = [1, 2, 3]
L.append(7)
print(L)

#  L.insert(POS,x)    Acrescentar item na posicao
L.insert(3, 5)
print(L)

# L.index(x)    Busca posicao de valor x
L = [11, 22, 33, 35, 57, 11, 77, 79]
print(L.index(35))

# L.count(x)    Conta a quantidade de ocorrencias do valor x
print(L.count(11))
