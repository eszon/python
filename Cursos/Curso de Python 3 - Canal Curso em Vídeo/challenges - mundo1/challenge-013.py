#!/usr/bin/python
salario = float(input('Salário: R$ '))
aumento = salario + (15 * salario / 100)
print('Seu novo salário é: R$ {}{:.2f}{} reais'.format('\033[1;32m', aumento, '\033[m'))
