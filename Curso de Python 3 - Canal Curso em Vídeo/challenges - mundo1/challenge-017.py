#!/usr/bin/python
from math import hypot
n1 = float(input('Comprimento do cateto oposto: '))
n2 = float(input('Comprimento do cateto adjacente: '))
hi = (n1 ** 2 + n2 ** 2) ** (1/2)
print('A hipotenusa vai medir: {}{:.2f}{}'.format('\033[1;32m', hypot(n1, n2), '\033[m'))
print('A hipotenusa vai medir: {}{:.2f}{}'.format('\033[1;33m', hi, '\033[m'))


