#Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem,
#  cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 parta viagens mais longas.

viagem = int(input('Qual a distância da sua viagem? '))

if viagem <= 200:
    calculo = viagem * 0.50
    print('Você está prestes a começar uma viagem de {} km.'.format(viagem))
    print('O custo dessa viagem é de R$ {:.2f} reais.'.format(calculo))
else:
    calculo02 = viagem * 0.45
    print('Você está prestes a começar uma viagem de {} km.'.format(viagem))
    print('O custo dessa viagem é de R$ {:.2f} reais.'.format(calculo02))