#!/usr/bin/python3.4
from datetime import date
now = date.today()

ano = int(input('Informe o ano do seu nascimento: '))
idade = now.year - ano
print('Quem nasceu em {} tem {} anos em {}.'.format(ano, idade, now.year))

if idade == 18:
    print('Você tem que se aliastar IMEDIATAMENTE!')
elif idade < 18:
    saldo = 18 - idade
    print('Ainda faltam {} anos para o alistamento.'.format(saldo))
elif idade > 18:
    print('Seu alistamento foi em {}.'.format(now.year - (idade - 18)))
elif idade > 18:
    print('Você já deveria ter se alistado há {} anos.'.format(idade - 18))


