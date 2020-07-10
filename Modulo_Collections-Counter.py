"""
Módulo Collections - Counter

High-performance Conteiner Datetypes

Counter -> Recebe um iterável como parâmetro e cria um objeto do tipo Collections Counter, contendo como chave o
           elemento da lista passada como parâmetro e como valor a quantidade de ocorrências desse elemento.
"""

from collections import Counter

# Podemos usar qualquer iterável, aqui usamos uma lista

lista = [1, 1, 1, 2, 2, 3, 3, 3, 1, 1, 5, 5, 5, 5, 5, 3, 45, 77, 99, 77]

res1 = Counter(lista)
print(type(res1))
print(res1)

# Usando uma string
str = 'Fernando Cibin'
res2 = Counter(str)
print(res2)

texto = """Linux é um termo popularmente empregado para se referir a sistemas operativos (português europeu) ou 
sistemas operacionais (português brasileiro) que utilizam o Kernel Linux.[5] O núcleo (ou kernel, em Alemão) foi 
desenvolvido pelo programador finlandês Linus Torvalds, inspirado no sistema Minix. O seu código fonte está disponível 
sob a licença GPL (versão 2) para que qualquer pessoa o possa utilizar, estudar, modificar e distribuir livremente 
de acordo com os termos da licença. A Free Software Foundation e seus colaboradores recomenda[6] o nome GNU/Linux 
para descrever o sistema operacional, como resultado de uma disputa controversa entre membros da comunidade de 
software livre e código aberto.[7][8]"""

palavras = texto.split()

res3 = Counter(palavras)
print(res3)

# Encontrando as 5 palavras com mais ocorrências
print(res3.most_common(5))