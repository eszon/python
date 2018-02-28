#!/usr/bin/python
c = float(input('Temperatura em Cº:'))
conversao = ((9*c) / 5) + 32
print('A temperatura de {}Cº para Fahrenheit é {}{}{}ºF'.format(c ,'\033[1;32m', conversao, '\033[m'))
