"""
Conjuntos
---------
- Conjuntos, em linguagem de programação, estamos fazendo referência à Teoria dos Conjuntos da Matemática.

- No Python, os conjuntos são chamados de Sets.

- Sets (conjuntos) não possuem valores duplicados;
- Sets (conjuntos) não possuem valores ordenados;
- Os elementos não são acessados via índice, conjuntos não são indexados;

- Os conjuntos (sets) são referenciados com chaves {}

- Diferença entre Conjuntos (Sets) e Mapas (Dicionários) em Python:
  - Um dicionário possui chave/valor;
  - Um conjunto possui apenas valor;

"""
# Definindo um conjunto

# Forma 1
s = set({1, 2, 3, 4, 5, 6, 7, 2, 3})  # Repare que temos valores repetidos
print(s)
print(type(s))

# Obs: Ao criar um conjunto, caso seja adicionado um valor já existente, o mesmo será ignorado
# sem gerar erroe não fará parte do conjunto.

# Forma 2 - mais comum
s = {1, 2, 3, 4, 5, 7, 5, 7}  # Repare que temos valores repetidos
print(s)
print(type(s))

# Adicionando elementos em um conjunto
s1 = {1, 2, 3}
s1.add(5)
print(f'Adicionando elemento: {s1}')

# Removento elementos de um conjunto

# Forma 1
s2 = {1, 2, 77, 5}
s2.remove(77)
print(f'Removendo elemento: {s2}')

# Forma 2
s2 = {1, 2, 77, 5}
s2.discard(77)
print(f'Removendo elemento: {s2}')

if 7 in s:
    print('Tem o número')
else:
    print('Não tem o número')

for valor in s:
    print(valor, end=' ')

# Importante lembrar que, além de não termos valores duplicados, não temos ordem

lista = [99, 2, 35, 23, 2, 12, 1, 47, 9, 23]
print(f'\nLista: {lista}')

tupla = (99, 2, 35, 23, 2, 12, 1, 47, 9, 23)
print(f'Tupla: {tupla}')

set = {99, 2, 35, 23, 2, 12, 1, 47, 9, 23}
print(f'Conjunto : {set}')

# Remover todos os itens de um conjunto
set = {99, 2, 35, 23, 2, 12, 1, 47, 9, 23}
set.clear()
print(set)

"""
Métodos matemáticos de Conjuntos

"""
print('Métodos matemáticos de Conjuntos')

# Estudantes de cursos de programação

estudantes_python = {'Marcos', 'Patricia', 'Ellen', 'Pedro', 'Julia', 'Guilherme'}
estudantes_java = {'Allana', 'Fernando', 'Marina', 'Julia', 'Ana', 'Patricia'}

print(f'Estudantes Python: {estudantes_python}')

print(f'Estudantes Java: {estudantes_java}')

# Alguns alunos que estudam Python tbm estudam Java.

"""
Gerar um conjunto com nomes únicos ( eliminar duplicidade)
"""
# Forma 1 - Utilizando Union
unicos1 = estudantes_python.union(estudantes_java)
print(f'Únicos1: {unicos1}')

# Forma 2 - Utilizando o caractere pipe |
unicos2 = estudantes_python | estudantes_java
print(f'Únicos2: {unicos2}')

"""
Gerar um conjunto com nomes que estão em ambos os cursos
"""
# Forma 1 - Utilizando Intersection
ambos1 = estudantes_python.intersection(estudantes_java)
print(f'Ambos1: {ambos1}')

# Forma 1 - Utilizando caractere &
ambos2 = estudantes_python & estudantes_java
print(f'Ambos2: {ambos2}')

"""
Gerar um conjunto com nomes que estão em um curso e não está no outro
"""
so_python = estudantes_python.difference(estudantes_java)

so_java = estudantes_java.difference(estudantes_python)

print(f'Só estudantes Python: {so_python}')
print(f'Só estudantes Java: {so_java}')