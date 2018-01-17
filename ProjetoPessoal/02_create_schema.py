#!/usr/bin/env python

import sqlite3

# conectando...
conn = sqlite3.connect('clientes.db')

# definindo um cursor
cursor = conn.cursor()

# criando a tabela (schema)

cursor.execute(""" CREATE TABLE clientes (
                    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                    nome TEXT NOT NULL,
                    email,
                    criado_em DATE NOT NULL); """)

print('Tabela criada com sucesso!')

# desconectando...
conn.close()
