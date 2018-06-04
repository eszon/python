'''def capital_case(x):
    return x.capitalize()

def somaa(a, b):
    return a + b

def multiply(a, b):
    return a * b
'''

def soma_valores():
    option = 0
    soma = 0
    contador = 0
    while option != 999:
        option = int(input('Digite um valor: '))
        if option == 999:
            break
        soma = soma + option
        contador = contador + 1
    print('Foram digitados {} valores'.format(contador))
    print('A soma de todos os valores foi {}'.format(soma))

soma_valores()