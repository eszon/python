#Exercício Python 007: Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média.

n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))
n3 = float(input('Terceira nota: '))

m = (n1 + n2 + n3) / 3

print(f'Primeira nota foi {n1}, a segunda {n2} e a terceira {n3}.')
print(f'A media é: {m:.2f}')
