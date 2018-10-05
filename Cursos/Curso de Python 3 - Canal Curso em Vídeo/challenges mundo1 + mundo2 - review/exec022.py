# Crie um programa que leia o nome completo de uma pessoa e mostre:
# - O nome com todas as letras maiúsculas e minúsculas.
# - Quantas letras ao todo (sem considerar espaços).
# - Quantas letras tem o primeiro nome

nome = str(input('Nome Completo: ')).strip()
n = nome.split()

print('Com letras maiúsculas: {}'.format(nome.upper()))
print('Com letras minusculas: {}'.format(nome.lower()))
print('Quantas letras (sem espaços) : {}'.format(len(nome.replace(' ', ''))))
print('Quantas letras tem o primeiro nome: {}'.format(len(n[0])))
print('Primeiro nome é: {}'.format(n[0]))