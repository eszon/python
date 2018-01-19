# Define a function
def world():
    print("Hello, World!")

def create_db(param1):
    import sqlite3
    conn = sqlite3.connect(param1)
    conn = conn.close()

def create_schema():
    import sqlite3

    # conectando...
    conn = sqlite3.connect('clientes.db')

    # definindo um cursor
    cursor = conn.cursor()

    # criando a tabela (schema)

    cursor.execute(""" CREATE TABLE clientes (
                        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                        nome TEXT NOT NULL,
                        email TEXT NOT NULL,
                        criado_em DATE NOT NULL); """)

    print('Tabela criada com sucesso!')

    # desconectando...
    conn.close()