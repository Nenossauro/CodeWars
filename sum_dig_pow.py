# -*- coding: UTF-8 -*-
import time
import tkinter.font as font
from tkinter import *
from tkinter import ttk


def abrir():
    rodar = True
    funcionarios = 30
    
    time.sleep(0.5)
    for i in range(funcionarios):
            if i == 1 or i == 0:
                continue

rodar = False


window = Tk()
window.title("Automação Planilha de Horas")
window.geometry('320x530')
window.configure(background = "grey")


"""
c = Label(window ,text = "Horas",bg="grey",fg="Black",font=("Arial",32)).place(x=150, y=0)

a = Label(window ,text = "Agencia",bg="grey",fg="Black",font=("Arial",22)).place(x=10, y=50)
agencia_select = tk.StringVar()
combobox = ttk.Combobox(window, textvariable=agencia_select,font=("Arial",22))
combobox['values'] = ('WilsonSons','Debug')
combobox['state'] = 'readonly'

b = Label(window ,text = "Navio",bg="grey",fg="Black",font=("Arial",22)).place(x=10, y=100)
b1 = Entry(window,font=("Arial",12)).place(x=100, y = 110)
"""

btn = Button(window ,text="Fazer planilha",command=abrir,height=2, width=50).place(x = 20, y = 40)














    
window.mainloop()
