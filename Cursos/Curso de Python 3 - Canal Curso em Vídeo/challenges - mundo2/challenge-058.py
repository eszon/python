#!/usr/bin/env python

from random import randint
from time import sleep

# variaveis
sucess = False
palpites = 0

# logica

computador = randint(1, 11)

while not sucess:
    jogador = int(input('Estou pensando em um número de 0 à 10... Qual será? '))

    palpites += 1

    if jogador == computador:
        print('Parabens! Você acertou!')
        sucess = True
    else:
        print('Você errou! Tente mais uma vez.')
        if jogador > computador:
            print('Pra menos...')
        elif jogador < computador:
            print('Pra mais...')

# resultado
print('Foram necessários {} palpites para você acertar!'.format(contador_palpites))
