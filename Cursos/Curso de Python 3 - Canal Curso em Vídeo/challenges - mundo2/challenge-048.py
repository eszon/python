#!/usr/bin/env python
soma = 0
cont = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        soma += 1
        cont += c
        print(c, end=' ')
print('A soma de todos os {} obitidos é {}'.format(soma, cont ))

