#!/usr/bin/env python

print(10 * '===')
print('10 TERMOS DE UMA P.A')
print(10 * '===')

num = int(input('Digite o primeiro número da PA: '))
razao = int(input('Digite a razão: '))

#or c in range(1, 11):
contador = 1
while contador < 11:
    print(num, end=' ')
    num += razao
    contador += 1

print(num)



