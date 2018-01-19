#!/usr/bin/python
n1 = int(input('Digite um número: '))
ant = n1 - 1
suc = n1 + 1
print('Analisando o número, seu antecessor é {}{}{} e seu sucessor é {}{}{}.'
      .format('\033[1;32m', ant, '\033[m', '\033[1;32m',  suc, '\033[m'))
