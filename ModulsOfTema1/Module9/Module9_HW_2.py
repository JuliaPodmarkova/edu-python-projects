def is_prime(func):
    def wrapper(*args):
        x = func(*args)
        if all((x % 2) !=0 for i in range (2, int(x**0.5)+1)):
            print(f"Простое: \n {x}")
        else:
            print(f"Составное: \n {x}")
        return x
    return wrapper

@is_prime
def sum_tree(*args):
    res = 0
    for i in args:
        res += i
    return res

result = sum_tree(2, 3, 6)
result1 = sum_tree(1, 2, 1)
