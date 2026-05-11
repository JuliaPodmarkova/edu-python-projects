def sey_hi():
    print("Привет, я из модуля 1")
    from random import randint
    print(randint(1, 10))

a = 0

def main():
    a = 5
    b = 10
    print("Привет")

#print("Hellow")

#print(__name__)

if __name__ == '__main__':
    main()

from dis import dis

def some_func():
    a = "Я из второго модуля"
    print("Я из второго модуля")
    return a

print(some_func())
dis(some_func)