#/usr/bin/env python

f = str(input('Digite uma palavra: ').replace(' ', ''))
if f == f[::-1]:
    print('O inverso de {} é {}'.format(f, f[::-1]))
    print('É palindroma')
else:
    print('O inverso de {} é {}'.format(f, f[::-1]))
    print('Não é palindroma!')


