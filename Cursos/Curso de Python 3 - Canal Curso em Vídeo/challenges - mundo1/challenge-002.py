#!/usr/bin/python
nome = str(input('Digite seu nome: ')).strip().capitalize()
print('Prazer em te conhecer,{}{}{}!.'.format('\033[1;32m', nome, '\033[m'))
