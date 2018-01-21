from tkinter import *

def calc():
    global msg
    altura = int(e1.get())
    peso = float(e2.get())
    imc = peso / ((altura / 100) ** 2)

    if imc < 18.5:
        msg = "abaixo do peso"
    elif imc < 25:
        msg = "peso normal"
    elif imc < 30:
        msg = "sobrepeso"
    elif imc <= 40:
        msg = "obesidade"
    else:
        msg = "obesidade mórbida"

    l3.config(text="O seu IMC é {:.1f} e seu peso é considerado {}".format(imc, msg))

t = Tk()
t.geometry('450x350')
t.title('IMC Admin')

l1 = Label(t, text="Altura (cm)")
e1 = Entry(t)

l2 = Label(t, text="Peso (Kg)")
e2 = Entry(t)

btn = Button(t, text="Calcular IMC", command=calc)

l3 = Label(t)

l1.pack()
e1.pack()
l2.pack()
e2.pack()
btn.pack()
l3.pack()
#t.mainloop()﻿