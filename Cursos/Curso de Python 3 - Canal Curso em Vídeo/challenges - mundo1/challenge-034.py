#!/usr/bin/python3.4

salario = float(input('Salário: '))

if salario > 1250:
    aumento = salario + (salario * 10/100)
    print('Seu antigo salário era: R$ {}{:.2f}{}reais e agora com aumento de 10% passou a ser R$ {}{:.2f}{}reais.'.format('\033[1;32m', salario, '\033[m', '\033[1;32m', aumento, '\033[m'))
else:
    aumento2 = salario + (salario * 15/100)
    print('Seu antigo salário era: R$ {}{:.2f}{} reais e agora com aumento de 15% passou a ser R$ {}{:.2f}{} reais.'.format('\033[1;32m', salario, '\033[m', '\033[1;32m', aumento2, '\033[m'))


