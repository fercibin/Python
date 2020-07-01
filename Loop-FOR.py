'''
Loop FOR
--------
- O loop FOR em Python pode iterar pelos itens de qualquer sequencia,
  como uma lista ou string.
- Sintaxe
for variavel in sequencia:
    Bloco de codigo
'''
var = 'Python'
for x in var:
    print(x)
print("**********************************************")

frutas = ['laranja', 'morango', 'guarana', 'melancia', 'mamao']
for y in frutas:
    print("Fruta: %s" %y)
    print("Fruta: " + y)
print("**********************************************")

'''
Loop FOR com contador
--------
- Funcao range() - Gera uma lista contendo uma progressao aritmetica
- Sintaxe
range(inicio, fim, salto)

- Inicio e salto sao opcionais
'''
for x in range(1,11):
    print(x)

for w in range(0,51,5):
    print(w)

for w in range(1,51,5):
    print(w)
