# Define a function
def world():
    print("Hello, World!")


def create_db(param1):
    import sqlite3
    conn = sqlite3.connect(param1)
    conn = conn.close()


def create_schema(param1):
    import sqlite3

    # conectando...
    conn = sqlite3.connect(param1)

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

def create_data(param1):
    import sqlite3

    conn = sqlite3.connect(param1)
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

def read_data(param1):
    import sqlite3

    conn = sqlite3.connect(param1)
    cursor = conn.cursor()

    # lendo dados
    cursor.execute(""" SELECT * FROM clientes;""")

    # retorna o resultado do select
    for linha in cursor.fetchall():
        print(linha)

    conn.close()

def update_data(param1):
    import sqlite3

    conn = sqlite3.connect(param1)
    cursor = conn.cursor()

    print(5 * '---*---', 'Escolha o que vai ser atualizado!', 5 * '---*---')

    # Opção a ser escolhida pelo usuario
    o = int(input('\n 1 - Atualizar o nome \n 2 - Atualizar o E-mail \n 3 - Atualizar a data de criação do registro \n'
                  ' Opção:  '))

    if o == 1:
        id_cliente = str(input('Digite o ID do Cliente: '))
        c_nome = str(input('Digite o novo nome: '))
        cursor.execute(""" UPDATE clientes SET nome = ? WHERE id = ? """, (c_nome, id_cliente))
        conn.commit()
        print('Nome atualizado com sucesso!')

    elif o == 2:
        id_cliente = str(input('Digite o ID do Cliente: '))
        c_email = str(input('Digite o novo E-mail: '))
        cursor.execute(""" UPDATE clientes SET email = ? WHERE id = ? """, (c_email, id_cliente))
        conn.commit()
        print('E-mail atualizado com sucesso!')
    elif o == 3:
        id_cliente = str(input('Digite o ID do Cliente: '))
        c_criado_em = str(input('Digite a nova data (dd-mm-yyyy): '))
        cursor.execute(""" UPDATE clientes SET criado_em = ? WHERE id = ? """, (c_criado_em, id_cliente))
        conn.commit()
        print('Data de criação atualizada com sucesso!')
    else:
        print('Opção Invalida!')

def delete_data(param1):
    import sqlite3

    conn = sqlite3.connect(param1)
    cursor = conn.cursor()

    print(5 * '---*---', 'Escolha qual usuário será deletado', 5 * '---*---')

    # Opção a ser escolhida pelo usuario
    id_cliente = int(input('\n Digite o ID do usuário: '))
    if id_cliente == 1 or 2 or 3 or 5 or 6 or 7 or 8:
        # excluindo um registro da tabela
        cursor.execute("""
           DELETE FROM clientes
           WHERE id = ?
           """, (id_cliente,))
        conn.commit()
        print('Registro excluido com sucesso.')
        conn.close()
    else:
        print('Opção invalida!')








