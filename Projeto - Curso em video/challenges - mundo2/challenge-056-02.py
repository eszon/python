#!/usr/bin/env python

# variaveis
nome_lista = []
idade_lista = []
sexo_lista = []
soma_idade = 0
contador = 0
contador2 = 0
maior_idade = 0
nome_maior_idade = ''

# logica
for i in range(1, 3):
    print(5 * '-', '{}º PESSOA'.format(i), 5 * '-')

    nome = str(input('Nome: '))
    nome_lista.append(nome)

    idade = int(input('Idade: '))
    idade_lista.append(idade)


    sexo = str(input('Sexo [M/F]: '))
    sexo_lista.append(sexo)

    #maior_idade = max(idade_lista)
    soma_idade += idade
    contador += 1

    if sexo in 'Ff' and idade < 20:
        contador2 += 1

for i in range(0, len(idade_lista)):
    if sexo_lista[i] == 'M' and idade_lista[i] > maior_idade:
        maior_idade = idade_lista[i]
        nome_maior_idade = nome_lista[i]


media_idade_geral = soma_idade / contador

# resultado
print('A média de idade do grupo é {} anos'.format(media_idade_geral))
print('O homem mais velho tem {} anos e se chama {}'.format(maior_idade, nome_maior_idade ))
print('Ao todo são {} mulheres com menos de 20 anos'.format(contador2))