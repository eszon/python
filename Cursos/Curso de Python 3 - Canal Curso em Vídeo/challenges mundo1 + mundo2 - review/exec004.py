anything = str(input('Digite algo: '))

print('O tipo primitivo desse valor é: {}'.format(type(anything)))
print('É um número? {} '.format(anything.isnumeric()))
print('Possui a primeira letra em maisculo? {}'.format(anything.capitalize()))
print('É alphanúmerico? {}'.format(anything.isalnum()))
print('É uma letra do alfabeto? {}'.format(anything.isalpha()))
print('Está em letra maiscula? {}'.format(anything.isupper()))
print('Só tem espaço? {}'.format(anything.isspace()))
