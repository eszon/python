import sqlite3, time

conectar = sqlite3.connect('agenda.db')
c = conectar.cursor()

def criar_db():
    c.execute('CREATE TABLE cadastro VALUES (nome text, telefone varchar, email text, data text)')

def inserir(n,t,e):
    d = time.strftime('%d/%m/%Y')
    c.execute('INSERT INTO cadastro VALUES(?,?,?,?)',(n,t,e,d))
    conectar.commit()

def listar(p):
    sql = 'SELECT * FROM cadastro WHERE nome = ?'
    for row in c.execute(sql,(p,)):
        print(row)

       
'''
try:
    criar_db()
except:
    print('Erro ao criar banco de dados!')
else:
    print('Banco de dados criado com sucesso!')
'''  

fc = int(input('1 - Cadastrar\n2 - Pesquisar\nO que você deseja fazer?: '))
if fc == 1:
    try:
        print('Cadastro Agenda')
        time.sleep(2)
        n = str(input('Digite um nome: '))
        t = int(input('Digite um telefone: '))
        e = str(input('Digite seu e-mail: '))

        inserir(n,t,e)
    except:
        print('Erro ao cadastrar!')
    else:
        print('Cadastrado com sucesso!')

elif fc == 2:
    try:
        print('Pesquisar Agenda')
        time.sleep(2)
        p = str(input('Digite o nome: '))
        listar(p)
    except:
        print('Erro ao Pesquisar!')
else:
    print('...')
    

