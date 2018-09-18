tabel = ('Flamengo', 'São Paulo', 'Cruzeiro', 'Grêmio', 'Internacional', 'Sport Recife', 'Palmeiras', 'Corinthians',
         'Fluminense', 'Atlético', 'América-MG', 'Botofogo', 'Vasco da Gama', 'Chapecoense', 'Santos,'
         'Atlético-PR', 'EC Vitória', 'Bahia', 'Paraná', 'Ceára SC')

print('What do you want to do? ')
print(''' 
          1- Apenas os cinco primeiros colocados.
          2- Os últimos quatro colocados na tabela.
          3- Uma lista com os times em ordem alfabética.
          4- Em que posição na tabela está o time da Chapecoense.
      ''')
print()

option = int(input('Enter a number: '))

if option == 1:
    for i in range(0,5):
        print(f'Time na {i+1} posição: {tabel[i]}')

if option == 2:
    print(f'Os últimos quatro colocados na tabela são: {tabel[-4]},{tabel[-3]}, {tabel[-2]}, {tabel[-1]}')

if option == 3:
    print(f'Os times em ordem alfabetica são {sorted(tabel)}')

if option == 4:
    print('A posição do time Chapecoense é: {}º'.format(tabel.index('Chapecoense') + 1))