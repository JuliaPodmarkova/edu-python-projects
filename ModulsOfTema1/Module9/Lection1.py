def get_russian_names():
    print(['Иван', 'Николай', 'Мария'])

#get_russian_names()
#print(type(get_russian_names))
#print(get_russian_names.__name__)

#my_func = get_russian_names
#print(type(my_func))
#print(my_func.__name__)

def get_british_names():
    print(['Jack', 'Oliver', 'Harry'])

name_getters = [get_russian_names, get_british_names]
#for name_getter in name_getters:
#    print(name_getter())

def adder(args):
    res = 0
    for num in args:
        res += num
    return res

def multiplier(args):
    res = 1
    for num in args:
        res *= num
    return res

def mul_by_2(x):
    return x * 2

def is_odd(x):
    return x % 2

def process_numbers(numbers, function):
    result = function(numbers)
    print(f'Получилось: {result}')

my_numbers = [3, 1, 4, 1, 5, 9, 2, 6]

process_numbers(my_numbers, adder)
process_numbers(my_numbers, multiplier)
result = map(mul_by_2, my_numbers)
print(result)
print(list(result))
result1 = filter(is_odd, my_numbers)
print(result1)
print(list(result1))