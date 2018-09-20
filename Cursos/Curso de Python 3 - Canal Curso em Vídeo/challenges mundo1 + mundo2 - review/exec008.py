# Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.

medida = float(input('Digite a distância em metros: '))

mm = medida * 1000
cm = medida * 100

print('A media de {}m corresponde a {:.0f}cm e {:.0f}mm'.format(medida ,mm, cm))


