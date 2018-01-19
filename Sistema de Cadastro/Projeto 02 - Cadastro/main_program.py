# Import function module
import functions


#functions.create_db('teste')

#functions.create_schema('teste')

functions.create_data('teste')

functions.read_data('teste')

#functions.update_data('teste')

print('Escolha um usuário para ser excluído')

functions.delete_data('teste')

print('{}Usuário excluído com sucesso!{}'.format('\033[1;32m]', '\033[m'))
print()
print('Lendo dados na tabela cliente...')

functions.read_data('teste')