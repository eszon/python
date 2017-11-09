#!/usr/bin/python

n1 = int(input('Digite um valor: '))
u = n1 // 1 % 10
d = n1 // 10 % 10
c = n1 // 100 % 10
m = n1 // 1000 % 10
print('Unidade: {}{}{}'.format('\033[1;32m', u, '\033[m'))
print('Dezena: {}{}{}'.format('\033[1;32m', d, '\033[m'))
print('Centena: {}{}{}'.format('\033[1;32m', c, '\033[m'))
print('Milhar: {}{}{}'.format('\033[1;32m', m, '\033[m'))