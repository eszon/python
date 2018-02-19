from tkinter import *

def bt_click():
    print('Push button')

window = Tk()

bt = Button(window, width=20, text='OK', command=bt_click)
bt.place(x=100, y=100)

lb = Label(window, text='Teste')
lb.place(x=100, y=150)

window.geometry('300x300+200+200')
mainloop()