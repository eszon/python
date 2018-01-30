print('Detitive de Palindroma')
f = str(input('Digite uma palavra: ').replace(' ', ''))

if f == f[::-1]:
    print('O inverso de {} é {}'.format(f, f[::-1]))
    print('É palindroma')
    input('Pressione Enter para sair.')
else:
    print('O inverso de {} é {}'.format(f, f[::-1]))
    print('Não é palindroma!')
    input('Pressione Enter para sair.')


