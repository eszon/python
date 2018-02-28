#!/usr/bin/python
from random import randint
n1 = int(input('Estou pensando em um número de 0 à 5... Qual será? '))
computador = randint(0, 5)
if n1 == computador:
    print('Parabens! Você acertou!')
else:
    print('Você errou! O número que eu pensei foi {} e você digitou {}{}{}.'.format(computador, '\033[1;33m', n1, '\033[m'))
