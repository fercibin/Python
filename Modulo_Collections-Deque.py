"""
Módulo Collections - Deque

Deque é uma lista de alta performance.
"""
from collections import deque

# Criando
deq = deque('Fernando')
print(type(deq))
print(deq)

# Adicionando elementos
deq.append('s')  # Adiciona no final
print(deq)

deq.appendleft('K') # Adiciona no começo
print(deq)

# Remover elementos
print(deq.pop())
print(deq)  # Remove do final

print(deq.popleft())  # Remove do início
print(deq)

