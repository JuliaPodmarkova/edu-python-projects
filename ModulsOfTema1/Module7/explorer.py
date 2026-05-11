import os
import time

from Module7.HomeWork7 import directory

os.environ["TCL_LIBRARY"] = 'C:/Users/user/AppData/Local/Programs/Python/Python313/tcl/tcl8.6'
os.environ["TK_LIBRARY"] = 'C:/Users/user/AppData/Local/Programs/Python/Python313/tcl/tk8.6'

import tkinter as tk
from tkinter import filedialog

def file_select():
    filename = filedialog.askopenfilename(initialdir="/", title="Выберите файл",
                                          filetypes=(('Текстовый файл', '.txt'),
                                                     ('Все файлы', '*')))
    text['text'] =text['text'] + filename
    os.startfile(filename)

window = tk.Tk()
window.title('Проводник')
window.geometry('450x150')
window.configure(bg='black')
window.resizable(width=False, height=False)
text = tk.Label(window, text='Файл',width=65, height=3, background='silver',
                foreground='blue')
text.grid(column=1, row=1)
button_select = tk.Button(window, width=10, height=3, text='Выбрать файл',
                          background='silver', foreground='blue', command=file_select)
button_select.grid(column=1, row=2, pady=5)
window.mainloop()
