#!/usr/bin/env python

# Imprimi o titulo
print(10 * '===*===', 'Dissecando uma variável', 10 * '===*===')

# Insira os dados
n1 = str(input('Digite algo: '))

# Especificando o tipo da variavel

print('O tipo primitivo desse valor é: {}{}{} ?'.format('\033[1;32m', type(n1), '\033[m'))
print('Só tem espaços: {}{}{}'.format('\033[1;32m', n1.isspace(), '\033[m'))
print('É um número? {}{}{}'.format('\033[1;32m', n1.isnumeric(), '\033[m'))
print('É alfabetico? {}{}{}'.format('\033[1;32m', n1.isalpha(), '\033[m'))
print('É alfanumerico? {}{}{}'.format('\033[1;32m', n1.isalnum(), '\033[m'))
print('É maiúscula? {}{}{}'.format('\033[1;32m', n1.isupper(), '\033[m'))
print('É minúscula? {}{}{}'.format('\033[1;32m', n1.islower(), '\033[m'))
print('É capitalizada? {}{}{}'.format('\033[m', n1.capitalize(), '\033[m'))







