countextense = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez', 'Onze', 'Doze', 'Treze',
                'Catorze', 'Quinze', 'Dezesseis', 'Dezessete', 'Dezoito', 'Dezenove', 'Vinte')

option = int(input('Digite um número: '))

while option not in range(0,21):
    print('Opção inválida, tente novamente.')
    option = int(input('Digite um número: '))

print(f'O número escrito por extenso é {countextense[option]}.')














