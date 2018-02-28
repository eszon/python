#!/usr/bin/python

#Pede para o usuário digitar um valor
num1 = int(input('Primeiro número: '))
num2 = int(input('Segundo número: '))

#Verifica o valor digitado
if num1 > num2:
    print('Primeiro número é {}MAIOR{}!'.format('\033[1;32m', '\033[m'))
elif num2 > num1:
    print('Segundo número é {}MAIOR!{}'.format('\033[1;32m', '\033[m'))
else:
    print('Os dois valores são iguais')

