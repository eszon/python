#!/usr/bin/python3.5

#Informe os valores
n1 = int(input('Digite um valor: '))
n2 = int(input('Digite outro valor: '))

soma = n1 + n2

#Exibe os valores
print('A soma dos valores {} e {} é: {}{}{}'.format(n1, n2, '\033[1;32m', soma, '\033[m'))
