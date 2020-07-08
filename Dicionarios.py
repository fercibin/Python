"""
Dicionários

- Não são propriamente sequências, mas mais precisamente MAPEAMENTOS.

- Dicionários são coleções do tipo CHAVE:VALOR

- Os objetos são armazenados por CHAVES em vez de posição relativa.

- Simplesmente mapeiam chaves a valores associados.

- São mutáveis.
- Codificados com chaves - {}

- Tanto CHAVE quanto VALOR podem ser de qualquer tipo de dados.

- Sao uteis quando precisamos associar um conjunto de valores a chaves
  para descrever as propriedades de algo:
  DIC = {'produto':'tigela', 'cor':'azul', 'preco':7 }

"""

# Criar Dicionário vazio
D = {}

# Adicionar elementos ao dicionário 1
D['nome'] = 'Fernando'
D['sobrenome'] = 'Cibin'
D['empresa'] = 'Home'

# Adicionar elementos ao dicionário 2
D.update({'Tel': '9999-7777'})

cpf = {'CPF': '111.333.555-77'}
D.update(cpf)

print(D)
print(D['empresa'])

DIC = {'produto': 'tigela', 'cor': 'azul', 'preco': 7}
print(DIC)
print(DIC['cor'])  # Acessando o elemento pela chave

paises = {'br': 'Brasil', 'eua': 'Estados Unidos', 'py': 'Paraguai'}
print(paises)
print(paises.get('br'))  # Acessando o elemento via GET - RECOMENDADO

print("**********************************************")

# Remover dados de um dicionário 1 - mais comum
print('Removendo o preço ')
DIC = {'produto': 'tigela', 'cor': 'azul', 'preco': 7}
DIC.pop('preco')
print(DIC)

# Remover dados de um dicionário 2
print('Removendo a cor ')
del DIC['cor']
print(DIC)

"""
Aninhamento em Dicionarios

- Podemos criar uma estrutura de Dicionario por meio de aninhamento para
  que haja suporte a multiplas partes, usando, por exemplo, listas ou
  outros Dicionarios como itens.

"""
print('\nAninhamento de dicionário')
R = {'nome': {'primeiro': 'Fernando', 'ultimo': 'Cibin'},
     'conhecimentos': ['Python', 'C++', 'Cobol'],
     'idade': 37}
print(R)
print(' ')
print(R['nome'])  # Retorna o nome completo
print(R['nome']['primeiro'])  # Retorna o primeiro nome
print(' ')
print(R['conhecimentos'])  # Retorna a lista completa
print(R['conhecimentos'][0])  # Retorna o elemento da posicao 0
print(R['conhecimentos'][-1])  # Retorna o ultimo elemento da lista
print(' ')
R['conhecimentos'].append('Natural')  # Inclui um novo valor na lista
R['conhecimentos'].append('C')
print(R['conhecimentos'])

"""
Ordenacao de Dicionarios
------------------------
- Dicionarios nao sao sequencias, logo nao mantem nenhuma ordem especifica
  de seus objetos.
- Se vc imprimir os itens de um dicionario, eles podem aparecer em
  qualquer ordem, sem nenhum tipo de ordenacao.
- E possivel exibir os itens de um dicionario em ordem, usando algumas
  tecnicas.

Uma solucao e obter uma lista das chaves com o metodo KEYS, ordena-la
com o metodo SORT, e entao retornar o resultado com um loop FOR.

"""

D = {'b': 2, 'a': 1, 'd': 4, 'c': 3}  # Dicionario inicial
ordenada = list(D.keys())  # Lista nao ordenada de chaves
print(ordenada)
ordenada.sort()  # Lista ordenada de chaves
print(ordenada)
# Iteracao atraves de chaves ordenadas, retornando o valor mapeado
# em cada chave
for chave in ordenada:
    print(chave, '=', D[chave])
print("**********************************************")
'''
Solucao usando a funcao SORTED
'''
D = {'b': 2, 'a': 1, 'd': 4, 'c': 3}  # Dicionario inicial

for chave in sorted(D):
    print(chave, '=', D[chave])

print("**********************************************")

"""
Métodos de Dicionários
----------------------
"""
d = dict(a=1, b=2, c=3)  # Outra forma de criar dicionário - pouco usada
print(d)
print(type(d))

# Limpar o dicionário ( Zerar dados)
d.clear()
print(d)

# Copiando um dicionário
d1 = dict(a=1, b=2, c=3)

# Forma 1 # Deep copy
print('Copiando - Deep copy')
novo = d1.copy()
print(novo)
novo['d'] = 4
print(novo)
print(d1)

# Forma 2 # Shallow copy
print('Copiando - Shallow copy')
novo = d1
print(novo)
novo['d'] = 4
print(novo)
print(d1)

# Acessando as chaves de um dicionário
print(d1.keys())

# Acessando os valores de um dicionário
print(d1.values())

# Acessando os itens de um dicionário
print(d1.items())

print("**********************************************")

"""
Iteração de Dicionários
----------------------
"""
receita = {'jan': 100, 'fev': 270, 'mar': 350}
print(receita)

for chave in receita:
    print(chave)


for chave in receita:
    print(receita[chave])

# Formatado
for chave in receita:
    print(f'Em {chave} recebi {receita[chave]} bozos ')

for chave, valor in receita.items():
    print(f'Chave={chave} e valor={valor}')

print("**********************************************")

"""
Soma, Valor Máximo, Valor Mínimo, Tamanho

"""

# Se os valores forem inteiros e reais
receita = {'jan': 100, 'fev': 270, 'mar': 350}

print(sum(receita.values()))
print(max(receita.values()))
print(min(receita.values()))
print(len(receita))

