#!/usr/bin/python3.4

nota1 = float(input('Primeira nota: '))
nota2 = float(input('Seginda nota: '))
nota3 = float(input('Terceira nota: '))

media = (nota1 + nota2 + nota3) / 3

print('Sua média foi: {:.2f}'.format(media))
if media < 5:
    print('Você foi REPROVADO!')
elif media >= 5 and media <= 6.9:
    print('Você foi RECUPERAÇÃO!')
elif media >= 7:
    print('Você foi {}APROVADO{}!'.format('\033[1;32m', '\033[m'))
