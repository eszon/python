#!/usr/bin/env python
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

if a == b and a == c:
    a = "Equilatero!"
elif b == a and b == c:
    a = "Equilatero"
elif c == a and c == b:
    a = "Equilatero"



print(a)
