#!/usr/bin/env python

n = int(input('Digite o valor para gerar a tabuada: '))
print(10 * '-=-')
print('Tabuada de {}'.format(n))
for c in range(1, 11):
    print('{} x {:2} = {}{}{}'.format(n, c, '\033[1;32m', n * c, '\033[m'))
print(10 * '-=-')