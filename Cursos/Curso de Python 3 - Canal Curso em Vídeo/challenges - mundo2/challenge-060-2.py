#!/usr/bin/env python

n = int(input('Digite um número para calcular seu fatorial: '))
c = n
f = 1
print('Calculando {}!: '.format(n))
while c > 0:
    print('{}'.format(c, end=''))
    print(' x ' if c > 1 else ' = ', end='')
    f *= c
    c -= 1
print('{}'.format(f))

