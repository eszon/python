#!/usr/bin/python
from math import sqrt
n1 = int(input('Digite um número: '))
print('O dobro deste número é: {}{}{}'.format('\033[1;32m', n1 * 2, '\033[m'))
print('O triplo deste número é: {}{}{}'.format('\033[1;32m', n1 * 3, '\033[m'))
print('A raiz quadrada deste número é: {}{:.2f}{}'.format('\033[1;32m', sqrt(n1), '\033[m'))

