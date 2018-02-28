#!/usr/bin/python
n1 = int(input('Valor em metros: '))
print('Em milímetros: {}{}{}mm.'.format('\033[1;32m', (n1 * 1000), '\033[m'))
print('Em centímetros: {}{}{}cm.'.format('\033[1;32m', (n1 * 100), '\033[m'))


