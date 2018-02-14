print('-' * 20)
print('LOJA SUPER BARATÃO!')
print('-' * 20)


soma_compras = 0
prod_maior_1000 = 0
prod_mais_barato = ''
valor_prod_mais_barato = 0
contador = 0

while True:
    nome_prod = str(input('Nome do Produto: '))
    preco_prod = float(input('Preço: R$ '))
    soma_compras += preco_prod
    if preco_prod > 1000:
        prod_maior_1000 += 1

    contador += 1
    if contador == 1 or valor_prod_mais_barato > preco_prod:
        valor_prod_mais_barato = preco_prod
        prod_mais_barato = nome_prod

    option = ''
    while option not in 'SN':
       option = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    if option == 'N':
           break

print(f'O total de compras foi de R${soma_compras:.2f} reais')
print(f'Temos {prod_maior_1000} produto(s) custando mais que R$ 1000,00 reais.')
print(f'O produto mais barato foi {prod_mais_barato} que custa R$ {valor_prod_mais_barato:.2f} reais.')

