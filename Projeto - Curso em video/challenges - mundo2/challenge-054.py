#!/usr/bin/env python

# variaveis
contador_maior = 0
contador_menor = 0
ano_atual = 2018

# logica
for i in range(1, 5):
    ano_nasc = int(input('Em que ano a {}º pessoa nasceu? '.format(i)))
    idade = ano_atual - ano_nasc
    if idade >= 18:
        contador_maior += 1
    else:
        contador_menor += 1

# resultado
print('Ao todo tivemos {} pessoas maior(s) de idade.'.format(contador_maior))
print('E também tivemos {} pessoas menor(s) de idade.'.format(contador_menor))
