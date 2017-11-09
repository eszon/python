#!/usr/bin/python
print(20*'=-=''Dissencando uma Váriável!',20*'=-=')

s = str(input('Digite algo: '))
print('O tipo primitivo desse valor é: {}{}{}!'.format('\033[1;32m', type(s), '\033[m'))
print('Só tem espaços? {}{}{}'.format('\033[1;32m', s.isspace(), '\033[m'))
print('É um número? {}{}{}'.format('\033[1;32m', s.isnumeric(), '\033[m'))
print('É alfabético? {}{}{}'.format('\033[1;32m', s.isalpha(), '\033[m'))
print('É alfanumerico? {}{}{}'.format('\033[1;32m', s.isalnum(), '\033[m'))
print('Está em maiscúla? {}{}{}'.format('\033[1;32m', s.isupper(), '\033[m'))
print('Está em minúsculas? {}{}{}'.format('\033[1;32m', s.islower(), '\033[m'))
print('Está capitalizado? {}{}{}'.format('\033[1;32m', s.istitle(), '\033[m'))






