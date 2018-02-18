"""

>>> somar(5, 10)
15

>>> somar(5, 15)
20

"""

'''def somar(num1, num2):
    a = num1 + num2
    return a
'''

from tkinter import *
from random import randint

jogadas = 3
player = 0
selecionar = 0
ganhou = 0

hub = '''
Numero de jogadas restante: 3
Numero = 0
voce escolheu: NENHUM
'''


def SelecionarImpar():
    global selecionar
    selecionar = 1
    atualizarHub()


def SelecionarPar():
    global selecionar
    selecionar = 2
    atualizarHub()


def atualizarHub():
    global selecionar, player, jogadas
    string = "NENHUM"
    if selecionar == 1:
        string = "IMPAR"
    elif selecionar == 2:
        string = "PAR"
    hub = '''
    Numero de jogadas restante %i
    Numero selecionado %i
    Voce escolheu %s
    ''' % (jogadas, player, string)
    label['text'] = hub


def Jogar():
    global player, jogadas, ganhou, selecionar
    if jogadas == -2:
        # resetar as jogadas
        jogadas = 3
        player = selecionar = ganhou = 0
        atualizarHub()
        start['text'] = "Start"
        show['text'] = "---"

    elif jogadas == -1:
        show['text'] = "Voce ganhou [%i/3]" % (ganhou)
        show['fg'] = "green"
        start['text'] = "Resetar"
        jogadas -= 1
    elif jogadas == 0:
        # Caso já der 3 jogadas
        start['text'] = "Resultado"
        jogadas -= 1
    else:
        caption = numero.get()
        if len(caption) == 0:
            show['fg'] = "red"
            show['text'] = "Não a nenhum valor inserido"
            return

        if (caption.isnumeric()) == False:
            show['fg'] = "red"
            show['text'] = "O valor inserido não é numerico"
            return
        player = int(numero.get())  # pegaremos o valor do Entry
        if (player > 0 and player < 11) == False:
            show['fg'] = "red"
            show['text'] = "O valor inserido não é invalido[entre 1 e 10]"
            return
        if selecionar == 0:
            show['fg'] = "red"
            show['text'] = "Voce precisa escolher impar ou par"
            return
        computador = randint(1, 10)  # Valor aleatorio do computador
        total = player + computador  # total - valor somado
        string = "IMPAR"
        if (total % 2) == 0:
            string = "PAR"
        string = "Voce escolheu {} e o computador {} , no total de {} deu {}".format(player, computador, total, string)
        show['text'] = string
        show['fg'] = "blue"
        jogadas -= 1
        if (total % 2) == (selecionar - 1):
            # Caso o jogador ganhar
            ganhou += 1
        atualizarHub()


janela = Tk()
janela.title('Exercicio nº 068')
janela['bg'] = "white"
label = Label(janela, text=hub)
label.place(x=0, y=0)

impar = Button(janela, text='Impar', width=20, command=SelecionarImpar)
impar.place(x=40, y=100)

par = Button(janela, text='Par', width=20, command=SelecionarPar)
par.place(x=230, y=100)

start = Button(janela, text='Start', width=20, command=Jogar)
start.place(x=150, y=300)

numero = Entry(janela)
numero.place(x=40, y=170)

spec = Label(janela, text="Digite um numero de 1 a 10")
spec.place(x=145, y=170)

show = Label(janela, text="---")
show.place(x=0, y=380)

janela.geometry("400x400+200+200")
janela.mainloop()