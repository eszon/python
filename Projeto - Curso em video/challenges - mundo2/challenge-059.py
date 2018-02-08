#!/usr/bin/env python

# modulos globais
from time import sleep
import os

# variaveis
valor1 = 0
valor2 = 0
opcao = 0

print('-----' * 10, 'MENU', '-----' * 10)

valor1 = int(input('Digite um valor: '))
valor2 = int(input('Digite outro valor: '))

while opcao != 5:

    print(''' [1] Somar
              [2] Multiplicar
              [3] Maior
              [4] Novos números
              [5] Sair do programa 
      ''')

    opcao = int(input('Opção: '))

    if opcao == 1:
        soma = valor1 + valor2
        print('A soma entre {} e {} é {}'. format(valor1, valor2, soma))
        sleep(1)
    elif opcao == 2:
        multiplicar = valor1 * valor2
        print('A multiplicação entre {} e {} é {}'.format(valor1, valor2, multiplicar))
        sleep(1)
    elif opcao == 3:
        maior = max(valor1, valor2)
        print('O maior número entre {} e {} é {}'.format(valor1, valor2, maior))
        sleep(1)
    elif opcao == 4:
        valor1 = int(input('Digite um valor: '))
        valor2 = int(input('Digite outro valor: '))

    elif opcao == 5:
        print('Ssindo do programa...')
        sleep(1)
        break
    else:
        print('Opção inválide, escolha 1 À 5.')