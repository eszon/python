#Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.

nome_completo = str(input('Nome Completo: ')).strip().split()
print('Primeiro nome: {}'.format(nome_completo[0]))
print('Segundo nome: {}'.format(nome_completo[-1]))

