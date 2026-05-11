my_func = lambda x: x + 10

print(my_func(x=42))
print(type(my_func))

my_numbers = [3, 1, 4, 1, 5, 9, 2, 6]
result = map(lambda x: my_func(x), my_numbers)
print(list(result))

they_numbers = [2, 7, 1, 8, 2, 8, 1, 8]

result = map(lambda x, y: x + y, my_numbers, they_numbers)
print(list(result))

print(my_func.__name__)

def get_multiplier_v1(n):
    if n == 2:
        def multiplier(x):
            return x * 2
    elif n == 3:
        def multiplier(x):
            return x * 3
    else:
        '''raise Exception("Я могу умножить только на 2 или 3")'''
        def multiplier(x):
            return x * n
    return multiplier

my_numbers = [3, 1, 4, 1, 5, 9, 2, 6]

by_2 = get_multiplier_v1((2))
by_3 = get_multiplier_v1((3))

result = map(by_2, my_numbers)
print(list(result))
result = map(by_3, my_numbers)
print(list(result))

by_5 = get_multiplier_v1(5)
print(by_5(x=42))

by_10 = get_multiplier_v1(10)
by_100 = get_multiplier_v1(100)

print(list(map(by_10, my_numbers)))
print(list(map(by_100, my_numbers)))

def matrix(some_list):
    def multiply_column(x):
        res = []
        for elem in some_list:
            res.append(elem * x)
        return res
    return multiply_column

matrix_on_my_numbers = matrix(my_numbers)
result = map(matrix_on_my_numbers, they_numbers)
print(list(result))


class Multiplier:
    def __init__(self, n):
        self.n = n

    def __call__(self, x):
        return x * self.n

by_100500 = Multiplier(n = 100500)
result = by_100500(x = 42)
print(result)

result = map(by_100500, my_numbers)
print(list(result))