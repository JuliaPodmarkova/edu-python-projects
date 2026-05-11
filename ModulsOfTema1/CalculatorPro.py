import os
from idlelib.configdialog import font_sample_text
from tkinter import PhotoImage

os.environ["TCL_LIBRARY"] = 'C:/Users/user/AppData/Local/Programs/Python/Python313/tcl/tcl8.6'
os.environ["TK_LIBRARY"] = 'C:/Users/user/AppData/Local/Programs/Python/Python313/tcl/tk8.6'

from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import math
import sys

window = Tk()
window.title("Calculator")
window.configure(background='purple1')
window.resizable(False, False)
window.geometry('390x190')


def buttonsPlays(list):
    r = 1
    c = 0
    for i in list:
        rel = ""
        cmd=lambda x=i: calc(x)
        i.grid(row=r, column = c)
        c += 1
        if c > 4:
            c = 0
            r += 1
calc_entry = Entry(window, width = 33, bg = "MediumPurple1", fg ="OliveDrab1", font = "Arial 15 bold")
calc_entry.grid(row=0, column=0, columnspan=5)



num1 = ttk.Button(window, text="1", command= lambda: print("1"))
num2 = ttk.Button(window, text="2", command= lambda: print("2"))
num3 = ttk.Button(window, text="3", command= lambda: print("3"))
num4 = ttk.Button(window, text="4", command= lambda: print("4"))
num5 = ttk.Button(window, text="5", command= lambda: print("5"))
num6 = ttk.Button(window, text="6", command= lambda: print("6"))
num7 = ttk.Button(window, text="7", command= lambda: print("7"))
num8 = ttk.Button(window, text="8", command= lambda: print("8"))
num9 = ttk.Button(window, text="9", command= lambda: print("9"))
num0 = ttk.Button(window, text="0", command= lambda: print("0"))
num11 = ttk.Button(window, text="=", command= lambda: print("="))
num12 = ttk.Button(window, text="*", command= lambda: print("*"))
num13 = ttk.Button(window, text="/", command= lambda: print("/"))
num14 = ttk.Button(window, text="-", command= lambda: print("-"))
num15 = ttk.Button(window, text="+", command= lambda: print("+"))
num16 = ttk.Button(window, text="xⁿ", command= lambda: print("xⁿ"))
num17 = ttk.Button(window, text=".", command= lambda: print("."))
num18 = ttk.Button(window, text="±", command=lambda: print("±"))
num19 = ttk.Button(window, text='C', command= lambda: print("C"))
num20 = ttk.Button(window, text='Exit', command= lambda: print("Exit"))
num21 = ttk.Button(window, text='π', command= lambda: print("π"))
num22 = ttk.Button(window, text='sin', command= lambda: print("sin"))
num23 = ttk.Button(window, text='cos', command= lambda: print("cos"))
num24 = ttk.Button(window, text='(', command= lambda: print(")"))
num25 = ttk.Button(window, text=')', command= lambda: print(")"))
num26 = ttk.Button(window, text='n!', command= lambda: print("n!"))
num27 = ttk.Button(window, text='√2', command= lambda: print("√2"))

num_list_start = [
num19, num27, num22, num23, num13,
num24, num1, num2, num3, num12,
num25, num4, num5, num6, num14,
num26, num7, num8, num9, num15,
    num16, num17, num0, num18, num11,
    num20, num21
]
buttonsPlays(num_list_start)

#логика калькулятора
def calc(key):
    global memory
    if key == num11:
#исключение написания слов
        str1 = "-+0123456789.*/)("
        if calc_entry.get()[0] not in str1:
            calc_entry.insert(END, "First symbol is not number!")
            messagebox.showerror("Error!", "You did not enter the number!")
#исчисления
        try:
            result = eval(calc_entry.get())
            calc_entry.insert(END, num11 + str(result))
        except:
            calc_entry.insert(END, "Error!")
            messagebox.showerror("Error!", "Check the correctness of data")

# очищение поля ввода
    elif key == num19:
        calc_entry.delete(0, END)
    elif key == num18:
        if num11 in calc_entry.get():
            calc_entry.delete(0, END)
        try:
            if calc_entry.get()[0] == num14:
                calc_entry.delete(0)
            else:
                calc_entry.insert(0, num14)
        except IndexError:
            pass
    elif key == num21:
        calc_entry.insert(END, math.pi)
    elif key == num20:
        window.after(1, window.destroy)
        sys.exit
    elif key == num16:
        calc_entry.insert(END, "**")
    elif key == num22:
        calc_entry.insert(END, num11 + str(math.sin(int(calc_entry.get()))))
    elif key == num23:
        calc_entry.insert(END, num11 + str(math.cos(int(calc_entry.get()))))
    elif key == num24:
        calc_entry.insert(END, num24)
    elif key == num25:
        calc_entry.insert(END, num25)
    elif key == num26:
        calc_entry.insert(END, num11 + str(math.factorial(int(calc_entry.get()))))
    elif key == num27:
        calc_entry.insert(END, num11 + str(math.sqrt(int(calc_entry.get()))))
    else:
        if "=" in calc_entry.get():
            calc_entry.delete(0, END)
        calc_entry.insert(END, key)
window.mainloop()