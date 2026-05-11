try:
    test1 = 'aaaaaaa'
    print('Test1:', test1)

    test2 = 0
    print('Test2:', (10 / test2))
except ZeroDivisionError:
    print('Error: нельзя делить на ноль')

try:
    truba = a + b
    truba = 10 / 0
except ZeroDivisionError:
    print('Error: нельзя делить на ноль')
except NameError:
    print("NameError: отсутствуют значения переменных")

try:
    a = 10 / 0
except ZeroDivisionError as exc:
    print(f'что-то пошло не так - {exc}, но мы все решим')

try:
    file = open('file.txt')
except OSError as exc:
    print(f'ошибка {exc} с параметрами {exc.args}')

try:
    i = 0
    result = 10 * (1/i)
    print(result)
except ZeroDivisionError:
    print('do not divide by zero')
else:
    print('all is good')
finally:
    print('end of lesson')

def f1(number):
    return 10 / number
def f2():
    print('What the nice day')
    result_f1 = f1(0)
    return result_f1

try:
    total = f2()
    print(total)
except ZeroDivisionError as exc1:
    print(f'Error: {exc1}')

def f3():
    print('Hey! What the nice day')
    summ = 0
    for i in range(-2, 2):
        summ += f1(i)
        print(summ)
    return summ

try:
    total = f3()
except ZeroDivisionError as exc2:
    print(f'Error: {exc2}')

def f4():
    print('What the beautiful day')
    summ = 0
    for i in range(-2, 2, 1):
        try:
            summ += f1(i)
            print(summ)
        except ZeroDivisionError as exc3:
            print(f'Error: {exc3}')
    return summ
f4()