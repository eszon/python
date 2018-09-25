# Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.

preco = float(input('Digite o preço do produto: R$ '))
desconto = float(input('Digite o valor do desconto em %: '))

novo = preco - (preco * desconto / 100)

print('O produto de preço R$ {:.2f} reais com desconto de {:.0f}% vai custar R$ {:.2f} reais.'.format(preco, desconto,
                                                                                                     novo))
