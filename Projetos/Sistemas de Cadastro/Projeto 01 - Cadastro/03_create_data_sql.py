#!/usr/bin/env python
import sqlite3

conn = sqlite3.connect('clientes.db')
cursor = conn.cursor()

# solitando dados ao usuario
p_nome = input('Nome: ')
p_email = input('Email: ')
p_criado_em = input('Criado em (dd-mm-yyyy): ')

# inserindo dados na tabela
cursor.execute(""" INSERT INTO clientes (nome, email, criado_em) VALUES (?, ?, ?)
               """, (p_nome, p_email, p_criado_em))

conn.commit()

print('Dados inseridos com sucesso')

conn.close()
