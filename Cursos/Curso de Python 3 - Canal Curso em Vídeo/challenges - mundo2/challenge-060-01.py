#/usr/bin/env python

n1 = int(input('Digite um valor: '))
c = n1 + 1
contador = 0
while contador <= n1:
        fatorial = n1 * (n1 - contador)
        contador += 1
        c -= 1
        print('{}! = {} x {} = {}'.format(n1 , n1, c, fatorial))
