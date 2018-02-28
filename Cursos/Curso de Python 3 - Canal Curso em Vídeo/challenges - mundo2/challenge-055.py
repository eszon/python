#!/usr/bin/env python

# lista
lista_peso = []

# logica
for i in range(1, 5):
    peso = int(input('Peso da {}º pessoa: '.format(i)))
    lista_peso.append(peso)

# varivel
maior_peso = max(lista_peso)
menor_peso = min(lista_peso)

# exibicao
print('Maior Peso lido foi: {}'.format(maior_peso))
print('Menor Peso: {}'.format(menor_peso))
