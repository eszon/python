#!/usr/bin/python
n1 = str(input('Digite seu nome completo: ')).strip()
print('Analisando seu nome...')
print('Seu nome em maiúsculas é: {}{}{}'.format('\033[1;32m', n1.upper(), '\033[m'))
print('Seu nome em minúsculos é: {}{}{}'.format('\033[1;32m', n1.lower(), ' \033[m'))
print('Seu nome tem {}{}{} letras.'.format('\033[1;32m', len(n1) - n1.count(' '), '\033[m'))
separa = n1.split()
print('Quantas letras tem o primeiro nome: {}{}{}'.format('\033[1;32m', len(separa[0]), '\033[m'))
