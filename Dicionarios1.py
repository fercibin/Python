'''
Dicionarios

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

'''

# Criar Dicionarios
D = {}
D['nome'] = 'Fernando'
D['sobrenome'] = 'Cibin'
D['empresa'] = 'Home'
print(D)
print(D['empresa'])
DIC = {'produto' : 'tigela', 'cor' : 'azul', 'preco' : 7 }
print(DIC)
print(DIC['cor'])
print("**********************************************")

'''
Aninhamento em Dicionarios

- Podemos criar uma estrutura de Dicionario por meio de aninhamento para
  que haja suporte a multiplas partes, usando, por exemplo, listas ou
  outros Dicionarios como itens.

'''
R = {'nome':{'primeiro':'Fernando', 'ultimo':'Cibin'},
     'conhecimentos':['Python', 'C++', 'Cobol'],
     'idade':37}
print(R)
print(' ')
print(R['nome']) # Retorna o nome completo
print(R['nome']['primeiro']) # Retorna o primeiro nome
print(' ')
print(R['conhecimentos']) # Retorna a lista completa
print(R['conhecimentos'][0]) # Retorna o elemento da posicao 0
print(R['conhecimentos'][-1]) # Retorna o ultimo elemento da lista
print(' ')
R['conhecimentos'].append('Natural') # Inclui um novo valor na lista
R['conhecimentos'].append('C')
print(R['conhecimentos'])
