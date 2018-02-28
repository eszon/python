#!/usr/bin/python
a = float(input('Digite à altura: '))
l = float(input('Digite a largura: '))
area = a * l
pintura = (area / 2)
print('Sua parede tem dimensão de {} x {} e sua área é: {:.2f}m².'.format(a, l, area))
print('Você irá precisar de {}{:.2f}{} litros de tinta.'.format('\033[1;32m', pintura, '\033[m'))
