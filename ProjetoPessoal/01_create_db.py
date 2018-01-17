#!/usr/bin/env python

# Importa biblioteca do banco de dados

import sqlite3

# Criando o banco de dados
conn = sqlite3.connect('clientes.db')
conn.close()

