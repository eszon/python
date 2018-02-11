#Informa a velocidade do carro
v1 = int(input('Qual é a velocidade atualo do carro? '))

#Bloco de código que defini o programa
if v1 > 80:
    print('{} MULTADO! Você deve pagar a multa de R$ {:.2f} reais. {}'.format('\033[1;32m', (v1 * 7), '\033[m'))
else:
    print('Você está dentro da velocidade permitida.')
