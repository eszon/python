#Exercicio71

cedulas = [50, 20, 10, 1]

quantidade = int(input("Quantidade a ser sacada: "))

for i in range(len(cedulas)):
    if quantidade >= cedulas[i]:
        j = quantidade // cedulas[i]
        print("Total de {} cédulas de {}R$".format(j, cedulas[i]))
    quantidade %= cedulas[i]