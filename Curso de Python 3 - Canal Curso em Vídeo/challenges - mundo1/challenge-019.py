#!/usr/bin/python
from random import choice
n1 = str(input('Primeiro Aluno: '))
n2 = str(input('Segundo Aluno: '))
n3 = str(input('Terceiro Aluno: '))
n4 = str(input('Quarto Aluno: '))
lista = [n1, n2, n3, n4]
escolhido = choice(lista)
print('Aluno escolhido: {}{}{}'.format('\033[1;32m', escolhido, '\033[m'))
