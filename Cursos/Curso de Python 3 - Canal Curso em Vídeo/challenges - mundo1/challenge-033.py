#!/usr/bin/python3.4

n1 = int(input('Primeiro número: '))
n2 = int(input('Segundo número: '))
n3 = int(input('Terceiro número: '))

#Verificando que é o maior número
if n1 > n2 and n1 > n3:
    print('{}{}{} é o maior valor!'.format('\033[1;32m', n1, '\033[m'))
elif n2 > n1 and n2 > n3:
    print('{}{}{} é o maior valor!'.format('\033[1;32m', n2, '\033[m'))
else:
    print('{}{}{} é o maior valor!'.format('\033[1;32m', n3, '\033[m'))

#Verificando que é o menor número
if n1 < n2 and n1 < n3:
    print('{}{}{} é o menor valor!'.format('\033[1;32m', n1, '\033[m'))
elif n2 < n1 and n2 < n3:
    print('{}{}{} é o menor valor!'.format('\033[1;32m', n2, '\033[m'))
else:
    print('{}{}{} é o menor valor!'.format('\033[1;32m', n3, '\033[m'))
