#!/usr/bin/python

#Pede para o usuário digitar um valor para ser convertido
n1 = int(input('Digite um valor: '))

#Pede para o usuário escolher qual será a base de conversão
print('''Escolha uma das bases para conversão:
[ 1 ] Converter para BINÁRIO
[ 2 ] Converter para OCTAL
[ 3 ] Converter para HEXADECIMAL.''')
print('')
n2 = int(input('Escolha uma opção: '))

#Verifica qual a opção escolhida
if n2 == 1:
    print('Sua opção {}'.format(n1))
    print('Conversão para binário: {}{}{}'.format('\033[1;32m', bin(n1)[2:], '\033[m'))
elif n2 == 2:
    print('Sua opção {}'.format(n1))
    print('Conversão para octal: {}{}{}'.format('\033[1;32m', oct(n1)[2:], '\033[m'))
elif n2 == 3:
    print('Sua opção: '.format(n2))
    print('Conversão para hexadecimal: {}{}{}'.format('\033[1;32m', hex(n1)[2:], '\033[m'))
else:
    print('Opção inválida. Tente novamente.')