# Faça um programa que leia um ano qualquer e mostre se ele é bissexto.
from datetime import date


ano_atual = date.today().year

print('Digite 0 para analisar o ano atual.')
ano = int(input('Digite o ano que você quer analisar: '))

if ano == 0:
    ano = ano_atual

if (ano % 4 == 0 and ano % 100 != 0) or (ano % 4 == 0 or ano % 400 == 0):
    print('O ano de {} é BISSEXTO.'.format(ano))
else:
    print('O ano de {} não é BISSEXTO.'.format(ano))


