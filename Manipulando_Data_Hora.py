# -*- coding: utf-8 -*-

"""
Manipulando Data e Hora
-----------------------

- Python tem um módulo integrado para se trabalhar com data e hora chamado DATETIME

"""

import datetime
from locale import  setlocale, LC_ALL

# Usar data em português
#setlocale(LC_ALL, 'pt_BR.utf-8')  # Usa um local especificado
setlocale(LC_ALL, '')  # Pega o local do computador

dat = datetime.datetime.now()
formatacao = dat.strftime('%A, %d de %B de %Y')
print(formatacao)

print(dir(datetime))

# O módulo datetime possui uma Classe datetime
# Retorna a data e hora corrente - TIMESTAMP
timestamp = datetime.datetime.now()
print(timestamp.year)
print(timestamp.month)
print(timestamp.day)

print(timestamp)
evento = datetime.datetime(2020, 1, 7, 5)
print(evento)

# Alterando uma data recebida como STRING para um objeto DATETIME
print('***************************************************************')

nascimento = '04/06/1976'
#nascimento = input('Informe sua data de nascimento (dd/mm/yyyy): ')

nascimento = nascimento.split('/')  # Usando o SPLIT para fazer a conversão em uma lista separado pelo /
print(type(nascimento))
print(nascimento)
print()
nascimento = datetime.datetime(int(nascimento[2]), int(nascimento[1]), int(nascimento[0]))
print(type(nascimento))
print(nascimento)

print('***************************************************************')

data_hoje = datetime.datetime.now()

data_futura = datetime.datetime(2021, 6, 6, 12)

# Calculando o delta

tempo_para_evento = data_futura - data_hoje

print(type(tempo_para_evento))
print(repr(tempo_para_evento))
print(tempo_para_evento)

print('***************************************************************')

# Simulando criar um boleto com data de vencimento 3 dias apos a data da compra

data_compra = datetime.datetime.now()
regra_boleto = datetime.timedelta(days=3)
print(regra_boleto)
vencimento_boleto = data_compra + regra_boleto
print(vencimento_boleto)

print('***************************************************************')