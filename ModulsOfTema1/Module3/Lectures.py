# Локальное, встроенное и глобальное пространство имен
from inspect import stack
from pprint import pprint
from sqlite3.dbapi2 import paramstyle

print("_____________________________________________")
print("Локальные и глобальное пространство имен")
print()
def printer():
    global a, b
    a = 'Str'
    b = 'Str2'
    c = 15
    d = 20
    print(a, b, '- global')
    print(c, d, '- local')
printer()

# Способы вызова функции по умолчанию
print("_____________________________________________")
print("Способы вызова функции по умолчанию")
print()
def print_params(a, b, c):
    print(a, b, c, '- print param')
    print(a + c, '- summa 1 and 3 param')
print_params(1, 2,3)

def print_params(a = 1, b = 2, c = 3):
    print(a, b, c, '- print param')
    print(a + c, '- summa 1 and 3 param')
print_params(7)

def print_params(*, a, b, c):
    print(a, b, c, '- print param')
print_params(a = 1, b = 2, c = 3)

# Параметры по умолчанию внутри функции
print("_____________________________________________")
print("Параметры по умолчению внутри функции")
print()
def def_with_params(a, b):
    print(a + b)
def_with_params(1, 2)
def_with_params(4, 3)

def def_with_params(a = 1, b = 2):
    print(a + b)
def_with_params()
def_with_params(4, 3)

def def_with_params(a, b=2):
    print(a + b)
def_with_params(2)
def_with_params(4, 3)

def def_with_params(a, b=2, c=3):
    print(a + b + c)
def_with_params(1, 2)
def_with_params(4, 3, 5)

def def_with_params(a, b=2, c=[]):
    c.append(a)
    print(c)
def_with_params(3)
def_with_params(3)
def_with_params(3)

def def_with_params(a, b=2, c=None):
    if c is None:
        c = []
        c.append(a)
    print(c)
def_with_params(3)
def_with_params(3)
def_with_params(3)

# Распаковка позиционных параметров

print("_____________________________________________")
print("Распаковка позиционных параметров")
print()
def print_params(*args):
    print(args)
print_params(1, 2, 3, 4, 5, 6)

def print_params(*args):
    print(*args)
print_params(1, 2, 3, 4, 5, 6)

def print_params(a, b, c):
    print(a, b, c)
list_ = [1, 2, 3]
print_params(*list_)

def print_params(a, b, c):
    print(a, b, c)
dict_ = {'a': 1, 'b': 2, 'c': 3}
print_params(**dict_)

def print_params(**kwargs):
    print(kwargs)
dict_ = {'a': 1, 'b': 2, 'c': 3}
print_params(**dict_)

def print_params(**kwargs):
    for key in kwargs:
        print(key)
dict_ = {'a': 1, 'b': 2, 'c': 3}
print_params(**dict_)

def print_params(**kwargs):
    for key, value in kwargs.items():
        print(key, value)
dict_ = {'a': 1, 'b': 2, 'c': 3}
print_params(**dict_)

def print_params(a, b, c):
    print(a, b, c)
list_ = [1, 2]
dict_ = {'c': 3}
print_params(*list_, **dict_)

# Произвольное число параметров
print("_____________________________________________")
print("Произвольное число параметров")
print()

def test_func(*params):
    print(params)
test_func()
test_func(1, 2, 3, 4, 5, 6)

def test_func(*params):
    print("Тип: ",type(params))
    print("Аргумент: ", params)
print("Все параметры бдут кортежем")
test_func("Soft", 1, 2, 2.95, "Caramel")

def summator(*values):
    s = 0
    for i in values:
        s += i
    return s
print(summator(1, 2, 3, 4))

def summator(txt, *values):
    s = 0
    for i in values:
        s += i
    return f'{txt}{s}'
print(summator("Сумма чисел: ", 1, 2, 3, 4, 5))

def summator(txt, *values, type = " sum"):
    s = 0
    for i in values:
        s += i
    return f'{txt}{s}{type}'
print(summator("Сумма чисел: ", 1, 2, 3, 4, 5, type = " summator"))

def info(**values):
    print("Тип: ", type(values))
    print("Аргумент: ", values)
info(name = "Julia", course = "Python")
info(name = "Ivan", course = "Robototehnika")

def info1(**values):
    print("Тип: ", type(values))
    print("Аргумент: ", values)
    for key, value in values.items():
        print(key, value)
info1(name = "Julia", course = "Python")

def info(*types, **values):
    print("Тип: ", type(values))
    print("Аргумент: ", values)
    for key, value in values.items():
        print(key, value)
    print(types)
info(1, 2, 3, name = "Julia", course = "Python")

def info(value, *types, names_author = "Den", **values):
    print("Тип: ", type(values))
    print("Аргумент: ", values)
    for key, value in values.items():
        print(key, value)
    print(types)
info("Пример использования параметров всеъ типов", 1, 2, 3, names_author = "Den", name = "Julia", course = "Python")

def my_sum(n, *args, txt = "Сумма чисел"):
    s = 0
    for i in range(len(args)):
        s += args[i] ** n
    print(txt + ":", s)
my_sum(1, 1, 2, 3, 4, 5)
my_sum(2, 2, 3, 4, 5, txt = "Сумма квадратов")

# Рекусия
print("_____________________________________________")
print("Рекусия - способ определения функции, когда эта функция вызывает саму себя")
print()

def summa(n):
    if n == 0:
        return 0
    else:
        return n + summa(n - 1)
print(summa(5))

stack = []
stack.append(1)
print("Добавили элемент ", stack)
stack.append(2)
print("Добавили элемент ", stack)
stack.append(3)
print("Добавили элемент ", stack)
print(stack)
stack.pop()
print("Убрали элемент ", stack)
stack.pop()
print("Убрали элемент ", stack)
stack.pop()
print("Убрали элемент ", stack)
print(stack)

# Встроенные функции Python 1.1
print("_____________________________________________")
print("Встроенные функции Python")
print()

#int() - целое число
#float() - число с плавающей запятой
#bool() - логические значения
#str() - строки
#list() - список
#tuple() - кортеж
#dict() - словарь
#set() - множество

salary = [2300, 1800.80358, 5000.8888444, 1234.521545138, 7500.125578]
print('Всего сотрудников: ', len(salary))
print("Общая сумма ФОТ: ", round(sum(salary), 3))
print("Средняя зарплата: ", round(sum(salary)/len(salary), 2))
print("Минимальная зарплата: ", round(min(salary), 2))
print("Максимальная зарплата: ", round(max(salary), 2))
names = ['Денис', 'Антон', 'Егор', 'Катя', 'Женя']
zipped = dict(zip(names, salary))
#print(list(zipped))
#print(dict(zipped))
print("Зарплата Дениса", zipped['Денис'])

# Встроенные функции. 1.2
print("_____________________________________________")
print("Встроенные функции 1.2")
print()

a = [1, 1, 1]
print(any(a))
b = [1, 1, 1]
print(any(b))
print(all(a))
print(all(b))
print(dir(a))
print(type(b))
print(isinstance(b, str))
print(a == b)
print(a is b)
print(id(a), id(b))
c = b
c[0] = 2
print(id(c), id(b))
print(c, b)
print(help(a))

# Практика по функциям
print("_____________________________________________")
print("Практика по функциям")
print()

#Функция поиска максимального числа в списке
def findMax(list_):
    max_ = list_[0]
    for i in list_:
        if i > max_:
            max_ = i
    return max_
list0_ = [1, 54, 12, -1, 2, 4]
print("Список: ", list0_)
print("Максимальное число в списке:", findMax(list0_))

#Функция по подсчету четных чисел в списке
def countEven(list_):
    counter = 0
    for i in list_:
        if i == 0:
            continue
        if i % 2 == 0:
            counter += 1
    return counter
list1_ = [6, 54, 12, 0, -1, 2, 4]
print("Список: ", list1_)
print("Количество четных чисел в списке:", countEven(list1_))

#Функция уникальный список
def unique(list_):
    newList = []
    for i in list_:
        if i not in newList:
            newList.append(i)
    return newList
list2_ = [1, 2, 3, 4, 5, 6, 7, 8, 1, 2, 3, 4, 10]
print("Список: ", list2_)
print("Уникальные числа в списке:", unique(list2_))