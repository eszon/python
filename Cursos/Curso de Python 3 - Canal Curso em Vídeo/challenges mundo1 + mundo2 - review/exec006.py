# Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.

n = int(input('Digite um número: '))

dobro = n * 2
triplo = n * 3
raizquadrada = n ** (1/2)

print('O dobro do número é: {}'.format(dobro))
print('Seu triplo é: {}'.format(triplo))
print('A raiz quadrada de {} é {:.2f}'.format(n, raizquadrada))
