#/usr/bin/env python

f = str(input('Digite uma palavra: '))
if f == f[::-1]:
    print('É palindroma')
else:
    print('Não é palindroma!')

print('Brasil balão'[::-1])
