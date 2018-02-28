#!/usr/bin/env python

print(10 * '===')
print('10 TERMOS DE UMA P.A')
print(10 * '===')

num = int(input('Digite o primeiro número da PA: '))
razao = int(input('Digite a razão: '))

for c in range(1, 11):
    print(num, end=' ')
    num += razao

print(num)



