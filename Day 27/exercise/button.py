# Tkinter Buttons : Day 27

import tkinter as t

screen = t.Tk()
screen.title("Tkinter Buttons")
screen.minsize(width=600, height=400)

label = t.Label(text='Hooooooooolaaa', font=('Calibri', 24, 'bold'))
label.pack()

def clicker():
    label.config(text=input.get())
    
button = t.Button(text='Click Me', command=clicker)
button.pack()

input = t.Entry(width=15)
input.pack()


t.mainloop()
