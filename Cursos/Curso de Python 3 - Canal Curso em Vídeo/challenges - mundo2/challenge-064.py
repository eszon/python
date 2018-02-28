option = 0
soma = 0
contador = 0
while True:
    option = int(input('Digite um valor: '))
    if option == 999:
        break
    soma = soma + option
    contador = contador + 1
print('Foram digitados {} valores e soma de todos foi {}'.format(contador, soma))
