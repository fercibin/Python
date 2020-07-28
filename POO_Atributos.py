# -*- coding: utf-8 -*-
"""
Atributos
---------
- Representam as características dos objetos, ou seja, pelos atributos nós conseguimos representar computacionalmente
  os estados de um objeto.

- Em Python, por convenção, ficou estabelecido que, todo atributo de uma classe é público, ou seja, pode ser
  acessado em todo projeto.
- Para tornar um atributo privado, ou seja, que só pode ser acessado/utilizado dentro da classe onde está declarado,
  utiliza-se duplo underline (__) no início do nome (Isso é conhecido como Name Mangling).

- Em Python, dividimos os atributos em 3 grupos:
  - Atributos de instância;
  - Atributos de classe;
  - Atributos dinâmicos;

----------------------
Atributos de Instância
----------------------
- São atributos declarados dentro do método construtor.
- Ao criarmos objetos/instâncias de uma classe, todos terão estes atributos. (Os valores poderão ser diferentes)
- Exemplo:

class Produto:

    def __init__(self, nome, descricao, valor):  # Método Construtor
        self.nome = nome
        self.descricao = descricao
        self.valor = valor

-------------------
Atributos de Classe
-------------------
- São atributos declarados fora do construtor, diretamente na classe.
- Ao criarmos objetos/instâncias de uma classe, o valor deste atributo será igual para todos.
- Não precisamos criar um objeto/instância para acessar um atributo de classe.
- Exemplo:

class Produto:

    imposto = 1.05  # Atributo de Classe

    def __init__(self, nome, descricao, valor):  # Método Construtor
        self.nome = nome
        self.descricao = descricao
        self.valor = (valor * Produto.imposto)

-------------------
Atributos Dinâmicos
-------------------
- É um atributo de instância que pode ser criado em tempo de execução.
- O atributo dinâmico é exclusivo da instância que o criou.
- Exemplo:

class Produto:

    def __init__(self, nome, descricao, valor):  # Método Construtor
        self.nome = nome
        self.descricao = descricao
        self.valor = valor

p1 = Produto('PS4', 'Video Game', 2500)
p2 = Produto('XBOX', 'Video Game', 2300)

p1.peso = '2Kg'   # Isso vai criar o atributo 'peso' exclusivo para o objeto p1

"""

# Classes com Atributos Públicos
class Lampada:

    def __init__(self, voltagem, cor):  # Método Construtor
        self.voltagem = voltagem        # Atributo de instância
        self.cor = cor
        self.ligada = False


class ContaCorrente:

    def __init__(self, numero, limite, saldo):  # Método Construtor
        self.numero = numero
        self.limite = limite
        self.saldo = saldo


class Produto:

    imposto = 1.05  # Atributo de Classe
    contador = 0

    def __init__(self, nome, descricao, valor):  # Método Construtor
        self.id = Produto.contador + 1
        self.nome = nome
        self.descricao = descricao
        self.valor = (valor * Produto.imposto)
        Produto.contador = self.id

# Podemos acessar o valor de um atributo de classe diretamente, sem criar uma instância/ objeto
print(Produto.imposto)

p1 = Produto('PS4', 'Video Game', 2500)
p2 = Produto('XBOX', 'Video Game', 2300)

print(p1.id)
print(p2.id)

class Usuario:

    def __init__(self, nome, email, senha):  # Método Construtor
        self.nome = nome
        self.email = email
        self.senha = senha

# Classe com Atributo Privado
class Acesso:

    def __init__(self, email, senha):
        self.email = email
        self.__senha = senha

    def mostra_senha(self):
        print(self.__senha)  # Acessando o atributo privado dentro da própria classe.


user = Acesso('fer@teste.com', 123456)

print(user.email)

# Tentando acessar Atributo Privado
# print(user.__senha)  # AttributeError

print(user._Acesso__senha)  # Temos acesso, mas não deveríamos fazer este acesso. (Name Mangling)

user.mostra_senha()

