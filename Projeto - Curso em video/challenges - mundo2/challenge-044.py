#/usr/bin/env python
import os
try:
    valor = float(input('Digite o valor do produto: '))
    parcelar = int(input('Parcelar: '))
    if parcelar == 0:
        pass
    else:
        p = valor / parcelar
    f = int(input('FORMA DE PAGAMENTO:'
                  '\n [1] Á vista em dinheiro/cheque - 10% de desconto '
                  '\n [2] Á vista no cartão - 5% de desconto'
                  '\n [3] Em até 2x - Preço normal'
                  '\n [4] Em 3x ou mais no cartão - 20% de juros '
                  '\n Opção: '))

    if f == 1 and parcelar > 0:
        print('Está opção é só para pagamento a vista.')
        input('Pressione Enter para continuar.')
        exit(1)
    elif f == 2 and parcelar > 0:
        print('Está opção é só para pagamento a vista.')
        input('Pressione Enter para continuar.')
        exit(1)

    d = valor - (valor * 10 / 100)
    d1 = valor - (valor * 5 / 100)
    j = valor + (valor * 20 / 100)


    if f == 1 and parcelar == 0:
        print(' Você escolheu pagamento à vista: R$ {:.2f}'.format(d))
    elif f == 2 and parcelar == 1:
        print('Você escolheu À vista no cartão: R${}'.format(d1))
    elif f == 3 and parcelar == 2:
        print('Você escolheu parcelar em {}x de R${}'.format(parcelar, p))
    else:
        print('Você escolheu parcelar em {}x vezes de R${:.2f} totalizando R${:.2f}'.format(parcelar, p, j))

except:
    print('Opção invalida, procure o administrador de sistemas.')
