# Import function module
import functions

functions.create_schema('teste')

while True:

    o = int(input('\n [1] - Criar um novo cadastro '
                  '\n [2] - Atualizar um cadastro existente '
                  '\n [3] - Deletar um cadastro '
                  '\n [4] - Visualizar todos os cadastrados'
                  '\n Opção:  '))

    if o == 1:
        functions.create_data('teste')
        wait = ('Aperte ENTER para continuar')

    elif o == 2:
        functions.update_data('teste')
        wait = ('Aperte ENTER para continuar')

    elif o == 3:
        functions.delete_data('teste')
        wait = ('Aperte ENTER para continuar')

    elif o == 4:
        functions.read_data('teste')
        wait = ('Aperte ENTER para continuar')

    elif o == 5:
        break

    else:
        print('Opção Invalida!')



