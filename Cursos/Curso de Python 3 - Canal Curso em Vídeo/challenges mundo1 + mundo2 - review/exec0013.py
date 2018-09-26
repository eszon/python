# Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento

salario = float(input('Digite seu salário: R$ '))
aumento = salario + (15 * salario / 100)

print('Um funcionário com salário de R${:.2f} reais com aumento de 15% passa a receber R${} reais.'
      .format(salario, aumento))
