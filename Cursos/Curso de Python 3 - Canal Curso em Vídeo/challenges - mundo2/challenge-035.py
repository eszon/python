#!/usr/bin/python3.4

salario = float(input('Salário: R$ '))
vcasa = float(input('Valor da casa: R$ '))
anos = int(input('Parcelado em quantos anos: '))

#Calcula o valor da prestação da casa
pm = vcasa / anos

#Calcula quanto é 30% do salario
mínimo = salario * 30/100

#Verifica se a prestação não excede 30% do salario para aprovar o emprestimo, caso contrário nega
if pm >= mínimo:
    print('O valor da parcela fica em R$ {}{:.2f}{} reais'.format('\033[1;32m', pm, '\033[m'))
    print('30% do seu salário seria: R$ {}{:.2f}{} reais'.format('\033[1;32m', mínimo, '\033[m'))
    print('Parcelado em {}{}{} anos'.format('\033[1;32m', anos, '\033[m'))
    print('Emprestimo NEGADO!')
else:
    print('O valor da parcela fica em R$ {}{:.2f}{} reais'.format('\033[1;32m', pm, '\033[m'))
    print('30% do seu salário seria: R$ {}{:.2f}{} reais'.format('\033[1;32m', mínimo, '\033[m'))
    print('Parcelado em {}{}{} anos'.format('\033[1;32m', anos, '\033[m'))
    print('Emprestimo {} APROVADO!{}'.format('\033[1;32m', '\033[m'))
