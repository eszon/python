#Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir
# qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu ou perdeu.
from random import randint
from time import sleep

numero_computador = randint(0,5)

numero_pessoa = int(input('Digite um número: '))

print('Processando...')
sleep(1)
print('Quase lá!')
sleep(1)

if numero_computador == numero_pessoa:
    print('Parabens! Você conseguiu me vencer.')
else:
    print('Você errou! Eu pensei no número {} e você no número {}.'.format(numero_computador, numero_pessoa))