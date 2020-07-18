# -*- coding: utf-8 -*-
"""
Bloco try / except
------------------

- Utilizamos o bloco try/except para tratar erros que podem ocorrer no nosso código.

A forma geral mais simples é:

try:
    //execução problemática
except:
    //o que deve ser feito em caso de problema

"""
# Exemplo 1 - Tratando um erro genérico
# Tratar erros de forma genérica não é a melhor forma de tratamento de erros. O ideal é SEMPRE tratar de
# forma específica.

try:
    teste()
except:
    print('Deu pau no teste!')


# Exemplo 2 - Tratando um erro específico

try:
    teste()
except NameError:
    print('Função Inexistente!')


# Exemplo 3 - Tratando um erro específico com detalhes do erro
# Podemos fazer diversos tratamentos de uma vez

try:
    len(7)
except TypeError as erro1:
    print(f'A aplicação gerou o erro: {erro1}')
except NameError as erro2:
    print(f'A aplicação gerou o erro: {erro2}')
except ValueError as erro3:
    print(f'A aplicação gerou o erro: {erro3}')
except:
    print('Deu um erro diferente.')


