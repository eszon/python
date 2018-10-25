# Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece a letra "A", em que posição ela aparece a primeira vez e em que posição ela aparece a última vez.

frase = str(input('Digite uma frase: ')).strip().upper()

print('A letra A aparece {} vez(es) na frase.'.format(frase.count('A')))
print('A primeira letra A apareceu na posição {}'.format(frase.index('A')))

posicao = frase[::-1]
print(posicao)




#print('A ultima vez que o A apareceu foi na posicao {}.'.format(frase.find('A', -1)))
