#!/usr/bin/python

n1 = str(input('Digite uma frase: ')).strip().upper()
xa = n1.count('A')
pa = n1.find('A')
pu = n1.rfind('A')

print('A letra A aparece {}{}{}'.format('\033[1;32m', xa, '\033[m'))
print('A primeira letra A aparece na posição: {}{}{}'.format('\033[1;32m', pa, '\033[m'))
print('A ultima posição que a letra A aparece é: {}{}{}'.format('\033[1;32m', pu, '\033[m'))
