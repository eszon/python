#Parte de Cadastro

nome = input('Digite seu nome: ');
while (len(nome) < 4 or len(nome) > 10):
    nome = input('Digite seu nome novamente: ');

idade = int(input('Digite sua idade: '));
while (idade <= 0 or idade >= 100):
    idade = int(input('Digite sua idade novamente: '));

peso = int(input('Digite seu peso: '));
while (peso <= 0):
           int(input('Digite seu peso novamente: '));
               

