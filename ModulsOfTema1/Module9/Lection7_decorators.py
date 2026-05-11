import sys
import time

def null_decorator(func):
    start = time.time()
    func()
    fin = time.time()
    print('Время работы функции в млс: ', (fin - start) * 1000, '\nфункция:')
    return func

def greet():
    return "Hello!"

greet = null_decorator(greet) # если нужно сохранить функционал без декоратора
print(greet())
print('')
@null_decorator # функция работает только с декоратором
def greet1():
    return "Hello world!"

print(greet1())
print('')

def uppercase(func):
    def wrapper():
        original_result = func()
        modified_result = original_result.upper()
        return modified_result
    return wrapper

@uppercase
def greet2():
    return "Hello!"
print(greet2())
print('')

def time_track(func):
    def surrogate(*args, **kwargs):
        started_at = time.time()
        result = func(*args, **kwargs)
        ended_at = time.time()
        elapsed = round(ended_at - started_at, 4)
        print((f'Функция работала {elapsed} секунд(ы)'))
        return result
    return surrogate

@time_track
def digits(*args):
    total = 1
    for number in args:
        total *= number ** 5000
    return len(str(total))

sys.set_int_max_str_digits(100000)

result = digits(3141, 5926, 2718, 2818)
print(result)