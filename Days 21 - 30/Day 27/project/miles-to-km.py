# Miles to Km Converter: Day 27 Project

import tkinter as t

screen = t.Tk()
screen.title("Miles to KM Converter")
screen.minsize(width=200, height=100)

def calculate():
    kmO = int(int(mileInput.get()) * 1.60934)
    kmText.config(text=f"{kmO} Km")
    return kmO


mileInput = t.Entry(width=15)
mileInput.grid(column=4, row=4)

mileLabel = t.Label(text="Miles")
mileLabel.grid(column=6, row=4)

kmText = t.Label(text="Km")
kmText.grid(column=4, row=7)

calculate = t.Button(text="Calculate", command=calculate)
calculate.grid(column=4, row=5)

screen.mainloop()
