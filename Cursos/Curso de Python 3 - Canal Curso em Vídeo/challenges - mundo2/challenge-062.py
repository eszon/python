#!/usr/bin/env python

print(10 * '===')
print('10 TERMOS DE UMA P.A')
print(10 * '===')

num = int(input('Digite o primeiro número da PA: '))
razao = int(input('Digite a razão: '))

mais_termos = 1
contador = 1
termos = 11
contador_termos = termos

while contador < termos:
    print(num,'->', end=' ')
    if contador == termos -1:
        print('PAUSE', end='')
    num += razao
    contador += 1
    if contador >= termos:
        mais_termos = int(input('\nQuantos termos você quer mostrar a mais? '))
        termos += mais_termos
        if mais_termos == 0:
            contador_termos -= 1
            print('Finalizando programa...')
            break
        contador_termos += mais_termos
print('Foram mostrados {} termos'.format(contador_termos))






