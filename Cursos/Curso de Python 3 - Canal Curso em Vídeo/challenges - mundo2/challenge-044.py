#/usr/bin/env python

valor = float(input('Digite o valor do produto: '))

f = int(input('FORMA DE PAGAMENTO:'
              '\n [1] Á vista em dinheiro/cheque - 10% de desconto '
              '\n [2] Á vista no cartão - 5% de desconto'
              '\n [3] Em até 2x - Preço normal'
              '\n [4] Em 3x ou mais no cartão - 20% de juros '
              '\n Opção: '))

d = valor - (valor * 10 / 100)
d1 = valor - (valor * 5 / 100)
j = valor + (valor * 20 / 100)

if f == 1:
    print(' Você escolheu pagamento à vista: R$ {:.2f}'.format(d))

elif f == 2:
    print('Você escolheu À vista no cartão: R${}'.format(d1))

elif f == 3:
    parcelar = int(input('Parcelar: '))
    if parcelar != 2:
        print('Parcelamento inválido, está opção é até em 2x. Por favor, tente novamente.')
        exit(1)
    p = valor / parcelar
    print('Você escolheu parcelar em {:.2f}x de R${:.2f}'.format(parcelar, p))

elif f == 4:
    parcelar = int(input('Parcelar: '))
    if parcelar > 10:
        print('Desculpe, só é possível parcelar em até 10x. Por favor, tente novamente.')
        exit()
    p = valor / parcelar
    print('Você escolheu parcelar em {}x vezes de R${:.2f}'.format(parcelar, p))
    print('Sua compra de R${:.2f} vai custar R${:.2f} com JUROS no final.'.format(valor, j))

else:
    print('{}Opção invalida. Por favor, tente novamente.{}'.format('\033[1;31m', '\033[m'))