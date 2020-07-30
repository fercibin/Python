# -*- coding: utf-8 -*-
"""
Abstração e Encapsulamento
--------------------------
- O grande objetivo da POO é encapsular nosso código dentro de um grupo lógico e hierárquico utilizando classes.

- Abstração, em POO, é o ato de expor apenas dados relevantes de uma classe, escondendo atributos e métodos
  privados do usuário.
- No exemplo abaixo, o usuário não precisa saber o que acontece dentro da classe para fazer uma tranferência,
  ele apenas precisa passar dois parâmetros : o valor e a conta de destino. Isso é a abstração.
"""
# Apenas para teste, não estamos fazendo validações de valores.

class Conta:

    contador = 300

    def __init__(self, titular, saldo, limite):
        self.__numero = Conta.contador
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite
        Conta.contador += 1

    def extrato(self):
        print(f"Saldo de {self.__saldo} do titular {self.__titular} com limite de {self.__limite}.")

    def depositar(self, valor):
        self.__saldo += valor

    def sacar(self, valor):
        self.__saldo -= valor

    def transferir(self, valor, conta_destino):
        # 1 - Remover o valor da conta de origem
        self.__saldo -= valor

        # 2 - Adicionar o valor na conta de destino
        conta_destino.__saldo += valor



# Testando

conta1 = Conta('Fernando', 2500.00, 500.00)
conta2 = Conta('Alessandra', 700.00, 100.00)

print(conta1.__dict__)

conta1.depositar(250.00)

print(conta1.__dict__)

conta1.sacar(500.00)

print(conta1.__dict__)
print(conta2.__dict__)

# Transferir da conta2 para conta1
conta2.transferir(500.00, conta1)

print(conta1.__dict__)
print(conta2.__dict__)