#!/usr/bin/env python

# variaveis
sexo = ''

# logica
while sexo != 0:
    sexo = str(input('Sexo (M/F): '))

    if sexo in 'MmFf':
        break
    else:
        print('Valor inválido.')
