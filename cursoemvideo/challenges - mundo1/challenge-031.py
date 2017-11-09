#Informar o valor
v1 = int(input('Qual a distância da viagem? '))

#Algoritimo 01

if v1 <= 200:
    valorv1 = 200 * 0.50
    print('O valor para esse destino até 200KM é R$ {}{:.2f} reais.'.format('\033[1;32m', valorv1))
else:
    valorv2 = 200 * 0.45
    print('O valor para esse destino com mais de 200KM é R$ {}{:.2f} reais'.format('\033[1;32m', valorv2))
