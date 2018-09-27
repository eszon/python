# Escreva um programa que converta uma temperatura digitando em graus Celsius e converta para graus Fahrenheit.

temperatura = float(input('Informe a temperatura em Cº: '))

conversao = (temperatura / 5 * 9) + 32

print('A temperatura de {}º C corresponde a {:.1f}º F!.'.format(temperatura, conversao))