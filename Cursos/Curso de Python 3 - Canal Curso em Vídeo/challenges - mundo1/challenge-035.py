#!/usr/bin/python3.4
print('-=-'*20)
print('Analisador de Triângulos')
print('-=-'*20)
a = int(input('Digite o primeiro segmento: '))
b = int(input('Digite o segundo segmento: '))
c = int(input('Digite o terceiro segmento: '))

if (a < (b + c)) and (b < (c + a)) and (c < (a + b)):
    print('{}Os segmentos acima PODEM FORMAR um triângulo{}!'.format('\033[4;33m', '\033[m'))
else:
    print('Os segmentos acima NÃO PODEM FORMAR um triângulo!')