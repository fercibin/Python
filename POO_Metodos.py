# -*- coding: utf-8 -*-
"""
Métodos (funções)
-----------------
- Representam as aes que o objeto pode realizar no sistema.

- Em Python, dividimos os métodos em dois grupos:
  - Métodos de instância;
  - Métodos de classe;

--------------------
Métodos de Instância
--------------------
- Os métodos abaixo são métodos de instância, pois precisamos criar um objeto para usá-los:
  - Produto.desconto(self, porcentagem)
  - Usuario.nome_completo(self)
  - Usuario.checa_senha(self, senha)

-----------------
Métodos de Classe - São conhecidos como 'métodos estáticos' em outras linguagens. Em Python tbm existem os métodos
-----------------   estáticos que são criados pelo Decorator.
- Os métodos de classe são criados pelo decorator:

    @classmethod     # Decorator
    def conta_usuario(cls):   # Método de Classe
        print(f'Temos {cls.contador} usuários no sistema.')

    @staticmethod    # Decorator
    def definicao():
        return 'UXRT3579'

"""


class Lampada:

    def __init__(self, cor, voltagem, luminosidade):  # Método Construtor
        self.__cor = cor  #
        self.__voltagem = voltagem  # Atributos de instância
        self.__luminosidade = luminosidade  #
        self.__ligada = False


class ContaCorrente:
    contador = 4999

    def __init__(self, limite, saldo):
        self.__numero = ContaCorrente.contador + 1
        self.__limite = limite
        self.__saldo = saldo
        ContaCorrente.contador = self.__numero


class Produto:
    contador = 0

    def __init__(self, nome, descricao, valor):
        self.__id = Produto.contador + 1
        self.__nome = nome
        self.__descricao = descricao
        self.__valor = valor
        Produto.contador = self.__id

    def desconto(self, porcentagem):
        """Retorna o valor do produto com o desconto"""
        return (self.__valor * (100 - porcentagem)) / 100

# Lib de criptografia
from passlib.hash import pbkdf2_sha256 as cryp

class Usuario:

    contador = 0     # Atributo de Classe

    @classmethod     # Método de Classe
    def conta_usuario(cls):
        print(f'Temos {cls.contador} usuário(s) no sistema.')

    def __init__(self, nome, sobrenome, email, senha):
        self.__id = Usuario.contador + 1
        self.__nome = nome
        self.__sobrenome = sobrenome    # Atributos de Instância
        self.__email = email
        self.__senha = cryp.hash(senha, rounds=200000, salt_size=16)
        Usuario.contador = self.__id

    def nome_completo(self):
        return f'{self.__nome} {self.__sobrenome}'

    def checa_senha(self, senha):
        if cryp.verify(senha, self.__senha):
            return True
        return False


p1 = Produto('Arroz', 'Rango', 10)
print(p1.desconto(20))  # Valor com o desconto de 20%
print(Produto.desconto(p1, 20))  # self, desconto

user1 = Usuario('Angelina', 'Jolie', 'angelina@teste.com', '123456')
user2 = Usuario('Felicity', 'Smoak', 'felicity@teste.com', '123456')

print(user1.nome_completo())
print(Usuario.nome_completo(user1))  # Para executar usando a classe (Usuario), precisamos passar uma instância
                                     # da classe (user1), pois a classe não tem 'self'
print(user2.nome_completo())

print('*************************************************************')

nome = 'Fernando'
sobrenome = 'Cibin'
email = 'teste@teste.com'
senha = input('Informe a senha: ')
confirma_senha = input('Confirme a senha: ')

if senha == confirma_senha:
    user = Usuario(nome, sobrenome, email, senha)
    print('Usuário cadastrado com sucesso!')
else:
    print('Senha não confere \nUsuário não cadastrado.')
    exit(88)  # Sair do programa com return code 88

senha = input('Informe a senha para acesso: ')

if user.checa_senha(senha):
    print('Acesso permitido.')
else:
    print('Acesso negado.')

print(f'Senha user criptografada: {user._Usuario__senha}')  # Acesso errado de um atributo 'privado'

print('*************************************************************')


# Métodos de Classe
user3 = Usuario('Beowolf', 'Domal', 'beo@teste.com', '777777')

Usuario.conta_usuario()  # Forma correta de acessar um método de classe

user3.conta_usuario()    # Forma incorreta, porém, possível.


