# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.

real = float(input('Quanto você tem em reais? R$ '))

dolar = real / 4.24

print('Com R${:.2f} reais pode comprar US${:.2f} dolares'.format(real, dolar))