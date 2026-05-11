import os
from tkinter import PhotoImage

os.environ["TCL_LIBRARY"] = 'C:/Users/user/AppData/Local/Programs/Python/Python313/tcl/tcl8.6'
os.environ["TK_LIBRARY"] = 'C:/Users/user/AppData/Local/Programs/Python/Python313/tcl/tk8.6'

import tkinter as tk

def addValues():
    num1 = int(number1Entry.get())
    num2 = int(number2Entry.get())
    return num1, num2

def insertValues(value):
    answerEntry.delete(0, 'end')
    answerEntry.insert(0, value)

def add():
    num1, num2 = addValues()
    res = (num1 + num2)
    insertValues(res)

def sub():
    num1, num2 = addValues()
    res = (num1 - num2)
    insertValues(res)

def mul():
    num1, num2 = addValues()
    res = (num1 * num2)
    insertValues(res)

def div():
    num1, num2 = addValues()
    res = (num1 / num2)
    insertValues(res)


window = tk.Tk()
window.configure(background='MistyRose1')


window.title("Калькулятор")
window.geometry("350x350")
window.resizable(False, False)
button_add = tk.Button(window, text = " + ", width = 2, height = 2, command = add, bg = "MediumPurple1", fg ="OliveDrab1", font = "Arial 15 bold")
button_add.place(x = 100, y = 200)
button_sub = tk.Button(window, text = " - ", width = 2, height = 2, command = sub, bg = "MediumPurple1", fg ="OliveDrab1", font = "Arial 15 bold")
button_sub.place(x = 150, y = 200)
button_mul = tk.Button(window, text = " * ", width = 2, height = 2, command = mul, bg = "MediumPurple1", fg ="OliveDrab1", font = "Arial 15 bold")
button_mul.place(x = 200, y = 200)
button_div = tk.Button(window, text = " / ", width = 2, height = 2, command = div, bg = "MediumPurple1", fg ="OliveDrab1", font = "Arial 15 bold")
button_div.place(x = 250, y = 200)
number1Entry = tk.Entry(window, width = 28)
number1Entry.place(x = 100, y = 75)
number2Entry = tk.Entry(window, width = 28)
number2Entry.place(x = 100, y = 150)
answerEntry = tk.Entry(window, width = 28)
answerEntry.place(x = 100, y = 300)
number1 = tk.Label(window, text = "Введите первое число:", bg = "MistyRose1", font = "Arial 15 bold")
number1.place(x = 100, y = 50)
number2 = tk.Label(window, text = "Введите второе число:", bg = "MistyRose1", font = "Arial 15 bold")
number2.place(x = 100, y = 125)
answer = tk.Label(window, text = "Ответ:", bg = "MistyRose1", font = "Arial 15 bold")
answer.place(x = 100, y = 275)
window.mainloop()