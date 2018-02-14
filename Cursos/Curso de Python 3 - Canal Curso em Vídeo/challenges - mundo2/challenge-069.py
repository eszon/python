
contador_idade = 0
contador_sexoM = 0
contador_mulheres_20anos = 0
option = ''

while True:
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip().upper()[0]

    if idade > 18:
        contador_idade += 1
    if sexo in 'Mm':
        contador_sexoM += 1
    if sexo in 'Ff' and idade < 20:
        contador_mulheres_20anos += 1

    option = str(input('Deseja continuar? [S/N]'))
    if option in 'Ss':
        pass
    else:
        break

print('=-=' * 20)
print(f'Total de pessoas com mais de 18 anos é {contador_idade}.')
print(f'Foram cadastrados {contador_sexoM} homens.')
print(f'Total de mulheres tem menos de 20 anos é {contador_mulheres_20anos}.')


