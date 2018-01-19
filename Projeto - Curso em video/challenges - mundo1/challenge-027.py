#!/usr/bin/python
nome = str(input('Qual seu nome? '))
n = nome.split()
print('Primeiro nome: {}{}{}'.format('\033[1;32m', n[0], '\033[m'))
print('Seu ultimo nome: {}{}{}'.format('\033[1;32m', n[len(n)-1],'\033[m'))


