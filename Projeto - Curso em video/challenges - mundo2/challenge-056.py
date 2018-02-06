#!/usr/bin/env python

# variaveis
soma_idade = 0
contador = 0
contador2 = 0
maior_idade = 0
nome_maior_idade = 'vazio'

# logica
for i in range(1, 5):
    print(5 * '-', '{}º PESSOA'.format(i), 5 * '-')

    nome = str(input('Nome: '))

    idade = int(input('Idade: '))


    sexo = str(input('Sexo [M/F]: '))


    soma_idade += idade
    contador += 1

    if i == 1 and sexo in 'Mm':
              maior_idade = idade
              nome_maior_idade = nome

    if sexo in 'Mm' and idade > maior_idade:
        maior_idade = idade
        nome_maior_idade = nome

if sexo in "Ff" and idade < 20:
    contador2 += 1

media_idade_geral = soma_idade / contador

# resultado
print('A média de idade do grupo é {} anos'.format(media_idade_geral))
print('O homem mais velho tem {} anos e se chama {}'.format(maior_idade, nome_maior_idade))
print('Ao todo são {} mulheres com menos de 20 anos'.format(contador2))


