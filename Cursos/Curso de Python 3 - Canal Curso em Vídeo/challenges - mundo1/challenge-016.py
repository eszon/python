#!/usr/bin/python
from math import trunc
n1 = float(input('Digite um número quebrado: '))
print('O valor digitado foi: {}{}{}'.format('\033[1;32m', int(n1), '\033[m'))
print('O valor digitado foi {} e sua porção inteira é: {}{}{}'.format(n1, '\033[1;32m', trunc(n1), '\033[m'))

