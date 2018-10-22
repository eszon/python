from random import randint

print('=-='*10)
print('Jogo de Adivinhação')
print('=-='*10)

valor_randomico = randint(1,10)

valor_escolhido = int(input('Digite um valor: '))

if valor_randomico == valor_escolhido:
    print('Parabens! Você acertou!')
else:
    if valor_escolhido > valor_randomico:
        mais_menos = 'maior'
    else:
        mais_menos = 'menor'
    print('O seu chute foi {}, o número era {}. Tente novamente.'.format(mais_menos, valor_randomico))

