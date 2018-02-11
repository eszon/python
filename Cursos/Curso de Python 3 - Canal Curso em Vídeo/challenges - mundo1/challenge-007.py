#!/usr/bin/python
nota1 = float(input('Primeira nota: '))
nota2 = float(input('Segunda nota: '))
nota3 = float(input('Terceira nota: '))
print('Sua média é: {}{:.2f}{}'.format('\033[1;32m', (nota1 + nota2 + nota3)/3, '\033[m'))
