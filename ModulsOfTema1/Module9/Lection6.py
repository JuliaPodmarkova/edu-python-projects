import time

def func_generator(n):
    i = 0
    while i != n:
        yield i
        i += 1

print(list(func_generator(10)))

def fibonacci_v1(n):
    result = []
    a, b = 0, 1
    for _ in range(n):
        result.append(a)
        a,v = b, a + b
    return result

def fibonacci_v2(n):
    a, b = 0, 1
    for i in range(n):
        yield a
        a, b = b, a + b

'''fib1 = fibonacci_v1(n = 10)
for value in fib1:
    print(value)'''

'''fib2 = fibonacci_v2(n = 10)
print(fib2)
for value in fib2:
    print(value)'''

def fibonacci_v3():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

'''for value in fibonacci_v3():
    print(value)
    if value > 10 ** 6:
        break'''
start = time.time()

def read_large_file(file_path):
    with open(file_path, 'r', encoding="utf-8") as f:
        for line in f:
            yield line.strip()

for line in read_large_file("large_file.txt"):
    print(line)

fin = time.time()
print((fin - start) * 1000)