#!/usr/bin/env python

# Digite o nome para ser exibido posteriomente além de usar os metodos strip que eliminam o espaço e o captalize que torna a
# Primeira letra maiscula
nome = str(input('Digite seu nome: ')).strip().capitalize()

# Exibe o nome digitado acima colorido
print('É um prazer te conhecer {}{}{}!'.format('\033[1;32m', nome, '\033[m'))
