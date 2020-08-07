"""
Módulo Collections - Deque

FILA (queue) - FIFO - Fist in, first out
- O primeiro elemento a entrar é o primeiro a sair

Deque é uma FILA de alta performance.

"""
from collections import deque
from time import sleep

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

# Exemplo em que mostra o primeiro elemento sendo substituído

fila = deque(maxlen=10)

for i in range(100):
    fila.append(i)
    sleep(.5)
    print(fila)