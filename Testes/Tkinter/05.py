from tkinter import *

def bt_click(param1):
    print(param1["text"])

window = Tk()

bt1 = Button(window, width=20, text='Button 01')
bt1['']
bt1.place(x=100, y=100)

bt2 = Button(window, width=20, text='Button 02')
bt2.place(x=100, y=130)

window.geometry('300x300+200+200')
mainloop()
