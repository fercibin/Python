# -*- coding: utf-8 -*-
"""
Herança - (Inheritance)
-----------------------
- A idéia de herança é reaproveitar código, e também extender nossas classes, que passam a herdar atributos e
  métodos das outras classes.

Cliente
    - nome
    - sobrenome
    - cpf
    -renda

Funcionario
    - nome
    - sobrenome
    - cpf
    - matricula

class Cliente:

    def __init__(self, nome, sobrenome, cpf, renda):
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__cpf = cpf
        self.__renda = renda

    def nome_completo(self):
        return f'{self.__nome} {self.__sobrenome}'


class Funcionario:

    def __init__(self, nome, sobrenome, cpf, matricula):
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__cpf = cpf
        self.__matricula = matricula

    def nome_completo(self):
        return f'{self.__nome} {self.__sobrenome}'

*****************
Pergunta: Existe alguma entidade genérica o suficiente para encapsular os atributos e métodos comuns
          a outras entidades?
*****************
Pessoa
    - nome
    - sobrenome
    - cpf

class Pessoa:

    def __init__(self, nome, sobrenome, cpf):
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__cpf = cpf

    def nome_completo(self):
        return f'{self.__nome} {self.__sobrenome}'

*******************
Podemos simplificar as entidades(Classes) Cliente e Funcionario da seguinte forma, usando herança:
*******************

class Cliente(Pessoa):

    def __init__(self, renda):
        self.__renda = renda


class Funcionario(Pessoa):

    def __init__(self, matricula):
        self.__matricula = matricula

*******************
- Quando uma classe herda de outra, ela herda TODOS os atributos e métodos da classe herdada.

- Quando uma classe herda de outra, a classe herdada é conhecida como:
  (Pessoa)
  - Super Classe
  - Classe Mãe / Pai
  - Classe Base
  - Classe Genérica

- A classe que herda, é conhecida como:
  (Cliente, Funcionario)
  - Sub Classe
  - Classe Filha
  - Classe específica

*******************
"""

class Pessoa:

    def __init__(self, nome, sobrenome, cpf):
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__cpf = cpf

    def nome_completo(self):
        return f'{self.__nome} {self.__sobrenome}'


class Cliente(Pessoa):
    """Cliente herda de Pessoa"""

    def __init__(self, nome, sobrenome, cpf, renda):
        Pessoa.__init__(self, nome, sobrenome, cpf)  # Forma NÃO comum de acessar dados da super classe
        self.__renda = renda


class Funcionario(Pessoa):
    """Funcionario herda de Pessoa"""

    def __init__(self, nome, sobrenome, cpf, matricula):
        super().__init__(nome, sobrenome, cpf)      # Forma mais comum de acessar dados da super classe
        self.__matricula = matricula

    def nome_completo(self):
        return f'{self._Pessoa__nome} {self.__matricula}'



cliente1 = Cliente('Angelina', 'Jolie', '123.456.789-00', 5000)
funcionario1 = Funcionario('Felicity', 'Smoak', '987.654.321-11', 1234)

print(cliente1.nome_completo())
print(funcionario1.nome_completo())        # Aqui estamos acessando o método que foi sobrescrito em Funcionario
print(Pessoa.nome_completo(funcionario1))  # Aqui acessamos o método da classe Pessoa

print(cliente1.__dict__)
print(funcionario1.__dict__)

