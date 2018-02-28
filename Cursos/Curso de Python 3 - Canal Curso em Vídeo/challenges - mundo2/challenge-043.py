#!/usr/bin/env python

# Solicita dados ao usuários
peso = float(input('Digite seu peso:  (KG)'))
altura = float(input('Digite sua altura: (M)'))

# Calculo
imc = peso / (altura ** 2)

# Mostrando IMC
print(' Seu IMC é: {:.2f}'.format(imc))

if imc < 18.5:
    print('Você está {}Abaixo do Peso{}!'.format('\033[1;32m', '\033[m'))
elif imc > 18.5 and imc < 25:
    print('Você está com o {}Peso ideal{}!'.format('\033[1;32m', '\033[m'))
elif imc > 25 and imc < 30:
    print('Você está com {}Sobrepeso{}!'.format('\033[1;32m', '\033[m'))
elif imc > 30 and imc < 40:
    print('Você possui {}Obesidade{}!'.format('\033[1;32m', '\033[m'))
else:
    print('Você possui {}Obesidade Morbida{}!'.format('\033[1;32m', '\033[m'))