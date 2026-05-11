import tkinter as tk
from tkinter import messagebox
import math
import sys

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculator Pro")
        self.root.configure(bg='purple1')
        self.root.resizable(False, False)
        self.root.geometry('390x190')

        # Поле ввода
        self.entry = tk.Entry(root, width=33, bg="MediumPurple1", fg="OliveDrab1",
                              font=("Arial", 15, "bold"), justify='right')
        self.entry.grid(row=0, column=0, columnspan=5, padx=5, pady=5)

        # Определение кнопок (текст, строка, команда)
        buttons = [
            ('C', 1, 0), ('√', 1, 1), ('sin', 1, 2), ('cos', 1, 3), ('/', 1, 4),
            ('(', 2, 0), ('1', 2, 1), ('2', 2, 2), ('3', 2, 3), ('*', 2, 4),
            (')', 3, 0), ('4', 3, 1), ('5', 3, 2), ('6', 3, 3), ('-', 3, 4),
            ('n!', 4, 0), ('7', 4, 1), ('8', 4, 2), ('9', 4, 3), ('+', 4, 4),
            ('±', 5, 0), ('0', 5, 1), ('.', 5, 2), ('xⁿ', 5, 3), ('=', 5, 4),
            ('π', 6, 0), ('Exit', 6, 1)
        ]

        self.button_refs = {}  # для доступа к кнопкам по тексту

        for text, row, col in buttons:
            cmd = lambda t=text: self.on_button_click(t)
            btn = tk.Button(root, text=text, command=cmd, width=5, bg='thistle1', font=('Arial', 9, 'bold'))
            btn.grid(row=row, column=col, padx=2, pady=2)
            self.button_refs[text] = btn

    def on_button_click(self, char):
        """Обработка нажатия кнопки"""
        current = self.entry.get()

        if char == 'C':
            self.entry.delete(0, tk.END)

        elif char == 'Exit':
            self.root.quit()
            sys.exit()

        elif char == '=':
            try:
                # Подготовка выражения: заменяем 'xⁿ' на '**', '√' на 'math.sqrt', 'sin'/'cos' на вызовы
                expr = current.replace('xⁿ', '**')
                # Для функций sin, cos, √, n! нужно аккуратно обработать, т.к. они вводятся как sqrt(...)
                # Упростим: eval не поддерживает sin(x) напрямую. Лучше преобразовать.
                # Но для простоты используем eval с математическими функциями в словаре
                # Однако, чтобы избежать ввода произвольного кода, ограничим доступные имена
                allowed_names = {
                    'sin': math.sin, 'cos': math.cos, 'sqrt': math.sqrt,
                    'factorial': math.factorial, 'pi': math.pi
                }
                # Заменяем 'n!' на factorial(целое_число) – нужно парсить, но для демо сделаем упрощённо
                # Лучше использовать безопасный eval с явным преобразованием
                # Здесь для простоты оставим eval, но это небезопасно. Для учебного калькулятора пойдёт.
                # Но мы добавим обработку 'n!' вручную
                if 'n!' in expr:
                    # Ищем число перед 'n!'
                    import re
                    match = re.search(r'(\d+)n!', expr)
                    if match:
                        num = int(match.group(1))
                        expr = expr.replace(f'{num}n!', str(math.factorial(num)))
                    else:
                        raise ValueError("Используйте n! после числа, например 5n!")

                # Заменяем π на pi
                expr = expr.replace('π', 'math.pi')
                # Обрабатываем унарный ±: заменяем на - (если в начале или после оператора)
                # Но проще позволить eval самому обработать минус

                result = eval(expr, {"__builtins__": None}, allowed_names)
                self.entry.delete(0, tk.END)
                self.entry.insert(0, str(result))
            except Exception as e:
                messagebox.showerror("Ошибка", f"Неверное выражение\n{e}")
                self.entry.delete(0, tk.END)

        elif char == '±':
            # Изменение знака текущего числа
            try:
                # Пытаемся взять последнее число в выражении
                text = current
                # Ищем последнее число (или выражение в скобках) – упрощённо
                # Если строка пустая или начинается с ', то добавляем '-'
                if not text:
                    self.entry.insert(0, '-')
                elif text[0] == '-':
                    self.entry.delete(0)
                else:
                    # Вставляем минус в начало
                    self.entry.insert(0, '-')
            except:
                pass

        elif char == '√':
            # Вставляем sqrt( и ждём ввода скобки
            self.entry.insert(tk.END, 'sqrt(')

        elif char == 'sin':
            self.entry.insert(tk.END, 'sin(')

        elif char == 'cos':
            self.entry.insert(tk.END, 'cos(')

        elif char == 'xⁿ':
            self.entry.insert(tk.END, '**')

        elif char == 'π':
            self.entry.insert(tk.END, 'π')

        elif char == 'n!':
            # Вставим перед текущей позицией? Просто вставим n!
            self.entry.insert(tk.END, 'n!')

        else:
            # Обычные символы: цифры, операторы, точка, скобки
            # Если последний результат был показан и сейчас нажата цифра – очищаем поле
            # (простая эвристика: если в конце есть '=' – не делаем, но у нас поле очищается после '=')
            # Просто вставляем символ
            self.entry.insert(tk.END, char)


if __name__ == "__main__":
    root = tk.Tk()
    app = Calculator(root)
    root.mainloop()
