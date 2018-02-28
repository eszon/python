from random import randint
print('-=-'* 10)
print('VAMOS JOGAR PAR OU ÍMPAR')
print('-=-'* 10)
jogador = 0
computador = 0
contador = 0
while True:
    jogador = int(input('Diga um valor: '))
    computador = randint(0, 10)
    total = computador + jogador
    par_impar = str(input('PAR ou ÍMPAR [P/I]: '))
    print(f'Você jogou {jogador} e o computador {computador}. Total deu {total}.', end='')
    print(' DEU PAR!' if total % 2 == 0 else 'DEU ÍMPAR')
    if par_impar == 'p':
        if total % 2 == 0:
            print('Você Venceu!')
            print('Vamos jogar novamente!')
            contador += 1
        else:
            print('GAME OVER! Você Perdeu!')
            break
    if par_impar == 'i':
        if total % 2 == 1:
            print('Você Venceu!')
            print('Vamos jogar novamente!')
            contador += 1
        else:
             print('GAME OVER! Você Perdeu!')
             break
print(f'Você venceu {contador} vezes.')






'''
    if total % 2 == 0:
        resultado = 'DEU PAR!'
        mao = 'p'
    else:
        resultado = 'DEU ÍMPAR!'
        mao = 'i'
'''