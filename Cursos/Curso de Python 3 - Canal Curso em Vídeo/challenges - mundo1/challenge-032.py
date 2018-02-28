#Importando modulo
from datetime import date
hj = date.today()

#Algoritimo
v1 = int(input('Digite um ano: '))

if v1 == 0:
    v1 = hj.year

if v1 % 4 == 0 and v1 % 100 != 0:
    print('É {}BISSEXTO!'.format('\033[1;32m'))
else:
    print('Não é {}BISSEXTO!'.format('\033[1;32m'))
