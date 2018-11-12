# Faça um programa que leia três números e mostre qual é o maior e qual é o menor.

n1 = int(input('Primeiro valor: '))
n2 = int(input('Primeiro valor: '))
n3 = int(input('Primeiro valor: '))

maior_valor = max(n1, n2, n3)
menor_valor = min(n1, n2, n3)

print()

print('Maior valor: {}.'.format(maior_valor))
print('Menor valor: {}'.format(menor_valor))