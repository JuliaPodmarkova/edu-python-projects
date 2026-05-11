#import this
import math

#def print(*args):
#    return 'ok'
#def square(x):
# global a
# a = x ** 2
# return a
# return a ** 2
# d = x ** 2

d = 7

def square(x):
    #global d
    d = x ** 2
    def even(x):
        nonlocal d
        d = x / 2
        #d = x * 2
        if d % 2 == 0:
            print("Четное")
        else:
            print("Нечетноe")
    even(x)
    return d

a = 5
b = square(4)
print(a)
#print(math.sqrt(a))
print(b)
#print(globals())