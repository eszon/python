#/usr/bin/env python
from time import sleep
from random import randint

opcao = int(input('''Suas opções:
                    [0] PEDRA 
                    [1] TESOURA
                    [2] PAPEL
                    Qual é a sua jogada?  '''))

if opcao not in [0,1,2]:
    print('Opção inválida! Por favor escolha de 0 - 2')
    exit()

print('JO')
sleep(0.50)
print('KEN')
sleep(0.50)
print('PO!!!')
sleep(0.50)

computador = randint(0,2)
jogador = opcao

print(10 * '=-=')

# Ifs das opções
if computador == 0:
    print('Computador jogou {}PEDRA{}'.format('\033[1;32m', '\033[m'))
elif computador == 1:
    print('Computador jogou {}TESOURA{}'.format('\033[1;32m', '\033[m'))
elif computador == 2:
    print('Computador jogou {}PAPEL{}'.format('\033[1;32m', '\033[m'))

if jogador == 0:
    print('Jogador jogou {}PEDRA{}'.format('\033[1;32m', '\033[m'))
elif jogador == 1:
    print('Jogador jogou {}TESOURA{}'.format('\033[1;32m', '\033[m'))
elif jogador == 2:
    print('Jogador jogou {}PAPEL{}'.format('\033[1;32m', '\033[m'))

print(10 * '=-=')

# Ifs do computador

if jogador == 0 and computador == 1:
    print('JOGADOR VENCE!')
elif jogador == 1 and computador == 2:
    print('JOGADOR VENCE!')
elif jogador == 2 and computador == 0:
    print('JOGADOR VENCE!')

# IFs do computador
if computador == 0 and jogador == 1:
    print('COMPUTADOR VENCE!')
elif computador == 1 and jogador == 2:
    print('COMPUTADOR VENCE!')
elif computador == 2 and jogador == 0:
    print('COMPUTADOR VENCE!')

# IF do empate
if jogador == computador:
    print('{}EMPATE!{}'.format('\033[1;32m', '\033[m'))


#print('Computador {} Jogador {}'.format(computador, jogador))