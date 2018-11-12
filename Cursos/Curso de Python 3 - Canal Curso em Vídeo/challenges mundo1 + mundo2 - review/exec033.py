# Faça um programa que leia três números e mostre qual é o maior e qual é o menor.

n1 = int(input('Primeiro Valor: '))
n2 = int(input('Segundo Valor: '))
n3 = int(input('Terceiro Valor: '))

if n1 > n2 and n1 > n3:
    print('O maior valor digitado foi: {}'.format(n1))
elif n2 > n1 and n2 > n3:
    print('O maior valor digitado foi: {}'.format(n2))
else:
    print('O maior valor digitado foi: {}'.format(n3))

if n1 < n2 and n1 < n3:
    print('O menor valor digitado foi: {}'.format(n1))
elif n2 < n1 and n2 < n3:
    print('O menor valor digitado foi: {}'.format(n2))
else:
    print('O menor valor digitado foi: {}'.format(n3))

