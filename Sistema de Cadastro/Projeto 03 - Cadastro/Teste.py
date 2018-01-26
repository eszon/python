print('')

print('\033[1;33m{}\033[m'.format('=+' * 40))
print('{:^80}'.format('Olá,Seja bem vindo'))
print('\033[1;33m{}\033[m'.format('=+' * 40))
print('')

print('Este programa informa se um número é primo ou não.')
print('Usaremos \033[1;31mvermelho\033[m para números divisiveis e \033[1;33mamarelo\033[m para não divisiveis')
print('')

numero = int(float(input('Digite qualquer número inteiro: ')))
print('')

a = 0
b = 0
c = 0
d = str(numero)
d = str(d.count('') - 1)
for contador in range(1, numero + 1):
    c += 1
    if numero % contador == 0:
        a += 1
        b += 1
        print('\033[1;31m{:&gt;2} \033[m'.replace('2', d).format(contador), end='')
    else:
        print('\033[1;33m{:&gt;2} \033[m'.replace('2', d).format(contador), end='')
    if c == 10:
        print('')

        c += -10
print('')

if a == 2:
    print('\nO número \033[1;31m{}\033[m é primo'.format(numero))
    print('')

else:
    print('\nO número \033[1;31m{}\033[m não é primo'.format(numero))
    print('')

print('Ele é divisivel por \033[1;31m{}\033[m números'.format(b))
print('')

print('\033[1;33m{}\033[m'.format('=+' * 40))
print('{:^80}'.format('Obrigado por usar nosso serviço'))
print('\033[1;33m{}\033[m'.format('=+' * 40))﻿
