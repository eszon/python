#!/usr/bin/env python

num = int(input('Digite um número: '))

for c in range(1, num + 1):
    if num % c == 0:
        print('\033[1;35m', end=' ')
    else:
        print('\033[1;31m', end=' ')
    print('{}'.format(c), end=' ')
