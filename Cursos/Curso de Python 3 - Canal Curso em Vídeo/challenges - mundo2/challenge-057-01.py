#!/usr/bin/env python
#Exercicio 57

sexo = str(input('Digite seu sexo (M/F): ')).strip().upper()[0]

while sexo not in 'MmFf':
    sexo = str(input('Dados inválidos. Digite seu sexo novamente: '))
print('Sexo {} registrado com sucesso.'.format(sexo))

