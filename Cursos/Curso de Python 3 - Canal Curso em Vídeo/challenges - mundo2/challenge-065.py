# variveis
contador = 1
option = ''
soma = 0
maior_valor = 0
menor_valor = 1
while option in 'Ss':
    num = int(input('Digite um número: '))
    option = str(input('Quer continuar [S/N]: '))
    if option in 'Ss':
        contador += 1
    soma += num
    media = soma / contador
    if num > maior_valor:
        maior_valor = num
    if num < menor_valor:
        menor_valor = num
print('Você digitou {} e a média foi: {}'.format(contador, media))
print('O maior valor é {} e o menor é {}'.format(maior_valor, menor_valor))
