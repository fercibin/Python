"""
Recebendo dados de usuário
--------------------------

input() -> Todo dado recebido via input é do tipo String

"""
# Entrada de dados
#print("Qual o seu nome?")
nome = input("Qual o seu nome?")  # Input -> Entrada

print("Bem vindo(a) %s" % nome)

#print("Qual a sua idade?")
idade = input("Qual a sua idade?")


# Saídas

# Exemplo de print 'antigo' 2.x
print("%s tem %s anos" %(nome, idade))

# Exemplo de print 'moderno' 3.x
print("{0} tem {1} anos".format(nome, idade))

# Exemplo de print 'mais atual' 3.7
print(f"{nome} tem {idade} anos")

"""
int(idade) -> Cast

Cast é a 'conversão' de um tipo de dado para outro
"""
print(f'{nome} nasceu em {2020 - int(idade)}')

# Fazer o cast direto na entrada:

idade2 = int(input("Qual a sua idade?"))
print(type(idade2))


