# -*- coding: utf-8 -*-
"""
# CRUD - CREATE, READ, UPDATE, DELETE

conexao = pymysql.connect(
    host='127.0.0.1',
    user='fernando',
    password='troll00',
    db='db_MeusLivros',  # Posso escolher mandar ou não.
    charset='utf8mb4',
    cursorclass=pymysql.cursors.DictCursor
)

cursor = conexao.cursor()

cursor.execute('select * from tbl_Livros LIMIT 100')
resultado = cursor.fetchall()

for linha in resultado:
    print(linha)

print()

for linha in resultado:
    print(linha['NomeLivro'], linha['PrecoLivro'])

cursor.close()
conexao.close()

"""
import pymysql.cursors
from contextlib import contextmanager

@contextmanager
def conecta():
    conexao = pymysql.connect(
        host='127.0.0.1',
        user='fernando',
        password='troll00',
        db='db_MeusLivros',  # Posso escolher mandar ou não.
        charset='utf8mb4',
        cursorclass=pymysql.cursors.DictCursor
    )
    try:
        yield conexao
    finally:
        print('Conexão fechada')
        conexao.close()


with conecta() as conexao:
    with conexao.cursor() as cursor:
        cursor.execute('select * from tbl_Clientes')
        resultado = cursor.fetchall()

        for linha in resultado:
            print(linha)

        print()

        for linha in resultado:
            print(linha['NomeCliente'], linha['SobrenomeCliente'])

# INSERE UM REGISTRO NA BASE DE DADOS
# with conecta() as conexao:
#     with conexao.cursor() as cursor:
#         sql = 'INSERT INTO clientes (NomeCliente, SobrenomeCliente, IdadeCliente, PesoCliente) VALUES ' \
#               '(%s, %s, %s, %s)'
#         cursor.execute(sql, ('Jack', 'Monroe', 112, 220))
#         conexao.commit()

# INSERE VÁRIOS REGISTROS NA BASE DE DADOS
# with conecta() as conexao:
#     with conexao.cursor() as cursor:
#         sql = 'INSERT INTO clientes (NomeCliente, SobrenomeCliente, IdadeCliente, PesoCliente) VALUES ' \
#               '(%s, %s, %s, %s)'
#
#         dados = [
#             ('MURIEL', 'FIGUEIREDO', 19, 55),
#             ('ROSE', 'FIGUEIREDO', 19, 55),
#             ('JOSE', 'FIGUEIREDO', 19, 55),
#         ]
#
#         cursor.executemany(sql, dados)
#         conexao.commit()

# DELETA UM REGISTRO DA BASE DE DADOS
# with conecta() as conexao:
#     with conexao.cursor() as cursor:
#         sql = 'DELETE FROM clientes WHERE id = %s'
#         cursor.execute(sql, (6,))
#         conexao.commit()

# DELETA QUANTIDADE DETERMINADA DE REGISTROS
# with conecta() as conexao:
#     with conexao.cursor() as cursor:
#         sql = 'DELETE FROM clientes WHERE id IN (%s, %s, %s)'
#         cursor.execute(sql, (7, 8, 9))
#         conexao.commit()

# DELETA REGISTRA ENTRE UM RANGE
# with conecta() as conexao:
#     with conexao.cursor() as cursor:
#         sql = 'DELETE FROM clientes WHERE id BETWEEN %s AND %s'
#         cursor.execute(sql, (10, 12))
#         conexao.commit()

# ATUALIZA UM REGISTRO NA BASE DE DADOS
# with conecta() as conexao:
#     with conexao.cursor() as cursor:
#         sql = 'UPDATE clientes SET NomeCliente=%s WHERE id=%s'
#         cursor.execute(sql, ('JOANA', 5))
#         conexao.commit()

