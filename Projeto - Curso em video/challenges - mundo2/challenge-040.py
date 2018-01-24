#!/usr/bin/python3.5
from datetime import date
hoje = date.today()

nasc = int(input('Ano de Nascimento: '))

idade = hoje.year - nasc

print('Você tem {} anos'.format(idade))

if idade <= 9:
    print('Categoria: MIRIN.')
elif idade <= 14:
    print('Categoria: INFANTIL.')
elif idade <= 19:
    print('Categoria: JUNIOR.')
elif idade <= 25:
    print('Categoria: SÊNIOR.')
else:
    print('Categoria: MASTER.')
