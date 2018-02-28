#!/usr/bin/python
nome = str(input('Qual seu nome completo? ')).strip().upper().split()
print('Tem Silva no nome? {}{}{}'.format('\033[1;32m', 'SILVA' in nome, '\033[m'))


