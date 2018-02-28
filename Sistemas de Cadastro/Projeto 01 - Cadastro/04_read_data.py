#/usr/bin/env python

import sqlite3

conn = sqlite3.connect('clientes.db')
cursor = conn.cursor()

# lendo dados
cursor.execute(""" SELECT * FROM clientes;""")

# retorna o resultado do select
for linha in cursor.fetchall():
    print(linha)

conn.close()

