from tkinter import *

window = Tk()

lb = Label(window, text='Fala galera!')
lb.place(x=100, y=100)

#WxH+l+t
window.geometry('300x300+200+200')

window.mainloop()