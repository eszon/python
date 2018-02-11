#/usr/bin/env python

soma = 0
contador = 0
somaimpar = 0
contadorimpar = 0


for c in range(1, 7):
    n = int(input('Digite o {}º valor: '.format(c)))
    if n % 2 == 0:
        soma += n
        contador += 1
    else:
        somaimpar += n
        contadorimpar += 1
print('Você informou {} números pares e a soma deles foi {}'.format(contador, soma))
print('Você informou {} números impares1 e a soma deles foi {}'.format(contadorimpar, somaimpar))
