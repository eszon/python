# Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção Inteira.

num = float(input('Digite um valor: '))

print('O valor digitado foi {:.3f} e a sua porção inteira é {}.'.format(num, int(num)))