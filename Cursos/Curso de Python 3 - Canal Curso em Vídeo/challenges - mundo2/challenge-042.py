#!/usr/bin/env python
print('-=-'*20)
print('Analisador de Triângulos')
print('-=-'*20)
a = int(input('Digite o primeiro segmento: '))
b = int(input('Digite o segundo segmento: '))
c = int(input('Digite o terceiro segmento: '))


# Identificando se irá forma um triangulo
if (a < (b + c)) and (b < (c + a)) and (c < (a + b)):
    print('{}Os segmentos acima PODEM FORMAR um triângulo{}!'.format('\033[4;33m', '\033[m'))
else:
    print('Os segmentos acima NÃO PODEM FORMAR um triângulo!')

# Verificando se o triangulo será equilatero
if a == b and a == c or b == a and b == c or c == a and c == b:
    print('Este triangulo é Equilatero!')
# Verificando se o triangulo é isosceles
elif a == b and a != c or a == c and a != b:
    print('Este triangulo é Isosceles!')
elif b == a and b != c or b == c and b != a:
    print('Este triangulo é Isosceles!')
elif c == a and c != b or c == b and c != a:
    print('Este triangulo é Isosceles!')
else:
    print('Este triangulo é Escaleno!')

