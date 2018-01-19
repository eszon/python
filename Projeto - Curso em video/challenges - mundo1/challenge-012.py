#!/usr/bin/python
valor = float(input('Digite o preço do produto: '))
desconto = int(input('Digite o valor do desconto: '))
total = valor - (desconto * valor / 100)
print('O produto que custava R$ {:.2f} reais, na promoção com desconto de {}% vai custar R$ {}{:.2f}{} reais.'
      .format(valor,desconto , '\033[1;32m', total, '\033[m'))
