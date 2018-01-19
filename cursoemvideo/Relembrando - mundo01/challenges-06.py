#!/usr/bin/env python
from math import sqrt

# ler número
n1 = int(input('Digite um número: '))

# variaveis
dobro = n1 * 2
triplo = n1 * 3
sqrt = sqrt(n1)

# exibi o resultado.
print('O dobro de {} é {}, seu triplo é {} e sua raiz quadrada é {:.3}.'.format(n1, dobro, triplo, sqrt))
