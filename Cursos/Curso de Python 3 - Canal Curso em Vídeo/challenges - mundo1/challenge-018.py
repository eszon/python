#!/usr/bin/python
from math import cos, sin, tan, radians
ang = float(input('Digite o Ângulo: '))
c = cos(radians(ang))
s = sin(radians(ang))
t = tan(radians(ang))
print('O ângulo de {} tem o COSSENO {}{:.2f}{}'.format(ang, '\033[1;32m', c, '\033[m'))
print('O ângulo de {} tem o SENO {}{:.2f}{}'.format(ang, '\033[1;32m', s, '\033[m'))
print('O ângulo de {} tem a TANGENTE {}{:.2f}{}'.format(ang, '\033[1;32m', t, '\033[m'))
