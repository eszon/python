#Informar um valor

v1 = int(input('Informe um número: '))

if v1 % 2 == 0:
    print('Este número é {}PAR!{}'.format('\033[1;32m', '\033[m'))
else:
    print('Este número é {}IMPAR!{}'.format('\033[1;32m', '\033[m'))