#!/usr/bin/python
km = int(input('Quantos KM rodados? '))
dias = float(input('Quantos dias alugados? '))
pago = (dias * 60) + (km * 0.15)
print('O valor a pagar é R$ {}{:.2f}{} reais'.format('\033[1;32m', pago, '\033[m'))
