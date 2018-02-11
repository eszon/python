#!/usr/bin/python
r = float(input('Quanto você tem na carteira: '))
dolar = r / 3.27
print('Você pode compra: {}{:.2f}{}'.format('\033[1;32m', dolar, '\033[m'))
