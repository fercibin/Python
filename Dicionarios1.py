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
  DIC = {'produto':'tijela', 'cor':'azul', 'preco':7 }

'''

# Criar Dicionarios
D = {}
D['nome'] = 'Fernando'
D['sobrenome'] = 'Cibin'
D['empresa'] = 'Home'
print(D)
print(D['empresa'])
DIC = {'produto' : 'tijela', 'cor' : 'azul', 'preco' : 7 }
print(DIC)
print(DIC['cor'])
