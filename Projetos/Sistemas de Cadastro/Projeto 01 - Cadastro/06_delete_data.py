#!/usr/bin/env python


import sqlite3

conn = sqlite3.connect('Clientes.db')
cursor = conn.cursor()

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