'''
Dicionarios
-----------
- Nao sao propriamente sequencias, mas mais precisamente MAPEAMENTOS.
- Mapeamentos tbm sao colecoes de objetos.
- Os objetos sao armazenados por CHAVES em vez de posicao relativa.
- Simplesmente mapeiam chaves a valores associados.
- Sao mutaveis.
- Codificados com chaves - {}
- Consistem em uma serie de pares CHAVE:VALOR
- Sao uteis quando precisamos associar um conjunto de valores a chaves
  para descrever as propriedades de algo:
  DIC = {'produto':'tigela', 'cor':'azul', 'preco':7 }

Ordenacao de Dicionarios
------------------------
- Dicionarios nao sao sequencias, logo nao mantem nenhuma ordem especifica
  de seus objetos.
- Se vc imprimir os itens de um dicionario, eles podem aparecer em
  qualquer ordem, sem nenhum tipo de ordenacao.
- E possivel exibir os itens de um dicionario em ordem, usando algumas
  tecnicas.
'''

'''
Uma solucao e obter uma lista das chaves com o metodo KEYS, ordena-la
com o metodo SORT, e entao retornar o resultado com um loop FOR.
'''
D = {'b':2, 'a':1, 'd':4, 'c':3} # Dicionario inicial
ordenada = list(D.keys()) # Lista nao ordenada de chaves
print(ordenada)
ordenada.sort() # Lista ordenada de chaves
print(ordenada)
# Iteracao atraves de chaves ordenadas, retornando o valor mapeado
# em cada chave
for chave in ordenada:
    print(chave, '=', D[chave])
print("**********************************************")
'''
Solucao usando a funcao SORTED
'''
D = {'b':2, 'a':1, 'd':4, 'c':3} # Dicionario inicial

for chave in sorted(D):
    print(chave, '=', D[chave])
