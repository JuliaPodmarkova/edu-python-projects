# Задача
# 1. Написать функцию, которая возвращает другую функцию, повторения двух символов
# «n» раз. У нас есть какая-то строчка, и нам нужно написать функцию, которая будет
# возвращать повторение первых двух символов. Но это не просто функция, это функция,
# которая будет генерировать другие функции, которые будут повторять первые два символа
# «n» количество раз.
# 2. Создать массив функций с различными параметрами «n» и применить все эти функции
# поочерёдно к аргументу «animal».
# 3. Применить все функции, которые мы до этого создадим, поочерёдно к массиву
# аргументов.

animal = "Медведь"
animals = ['Заяц', 'Медведь', 'Бегемот']

def gen_reeat(n):
    def repeat(animal):
        return (animal[:2] + ' - ') * n + animal
    return repeat

test_1 = gen_reeat(1)
test_2 = gen_reeat(2)
print(test_1(animal))
print(test_2(animal))

# Задача 2
repetitions = [gen_reeat(n) for n in range(1, 4)]
print(repetitions)

result = [func(animal) for func in repetitions]
print(result)

# Задача 3
fin_result = [func(x) for func in repetitions for x in animals]
print(fin_result)

# another funct

def memoize_func(f):
    mem = {}
    def wrapper(*args):
        print(f'Выполнение функции с аргументами = {args}, внутренняя память = {mem}')
        if args not in mem:
            mem[args] = f(*args)
            return f'Функция выполнилась, ответ = {mem[args]}'
        else:
            return f' Функция уже была выполнена раньше = {mem[args]}'
    return wrapper

@memoize_func
def func(a, b):
    print(f'Выполняем функцию с аргументами {a} и {b}')
    return a ** b

print(func(3, 5), '\n')
print(func(3, 4), '\n')
print(func(3, 2), '\n')
print(func(3, 5), '\n')
print(func(3, 4), '\n')
print(func(3, 5), '\n')