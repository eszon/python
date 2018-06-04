print('-' * 25)
print('Sequência de Fibonnaci')
print('-' * 25)

contador = 0

termos = int(input('Quantos termos você quer mostrar? '))

t1 = 0
t2 = 1
print('{} -> {}'.format(t1, t2), end='')
contador = 1
while contador <= termos - 2:
    t3 = t1 + t2
    print(' -> {}'.format(t3), end='')
    t1 = t2
    t2 = t3
    contador += 1