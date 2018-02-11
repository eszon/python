#!/usr/bin/env python

# modulos globais
from time import sleep
import os

# variaveis
valor1 = 0
valor2 = 0
opcao = 0

print('-----' * 10, 'MENU', '-----' * 10)

valor1 = int(input('Primeiro valor: '))
valor2 = int(input('Segundo valor: '))

while opcao != 5:

    print('''              [1] Somar
              [2] Multiplicar
              [3] Maior
              [4] Novos números
              [5] Sair do programa 
      ''')

    opcao = int(input('>>>> Opção: '))

    if opcao == 1:
        soma = valor1 + valor2
        print('O resultado de {} + {} é {}'. format(valor1, valor2, soma))
        sleep(1)
    elif opcao == 2:
        multiplicar = valor1 * valor2
        print('O resultado de  {} x {} é {}'.format(valor1, valor2, multiplicar))
        sleep(1)
    elif opcao == 3:
        maior = max(valor1, valor2)
        print('O resultado entre {} e {} o maior é {}'.format(valor1, valor2, maior))
        sleep(1)
    elif opcao == 4:
        print('Informe os números novamente:')
        valor1 = int(input('Primeiro valor: '))
        valor2 = int(input('Segundo valor: '))

    elif opcao == 5:
        print('Finalizando...')
        print('Saindo do programa...')
        sleep(1)
        break
    else:
        print('Opção inválida. Tente novamente.')
    print('=-=' * 10)