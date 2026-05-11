# race condition (состояние гонки)
import threading
from threading import Thread, Lock
import time

x = 0
lock = Lock()

def thread_task():
    global x
    for i in range(1_000_000):
        try:
            lock.acquire()
            x = x + 1
        finally:
            lock.release()

def main():
    global x
    x = 0
    t1 = threading.Thread(target=thread_task)
    t2 = threading.Thread(target=thread_task)

    t1.start()
    t2.start()

    t1.join()
    t2.join()

for i in range(10):
    main()
    print(x)

#Рассмотрим несколько примеров атомарных операций:
# 1. Добавление элемента в список «append»: элемент либо добавляется
# в список, либо нет. Никаких промежуточных состояний в процессе добавления
# нет.
# 2. Объединение списков «extend»: списки либо объединяются полностью,
# либо не объединяются вовсе.
# 3. Сортировка списка «sort»: Либо список отсортирован полностью, либо нет.
# Процесс не может остановиться на полпути, оставив список частично
# отсортированным.
# 4. Присваивание значений «y = x»: если, например, переменная «x» равна 10,
# то операция присваивания либо выполнится, и «y» примет значение 10, либо
# не выполнится вовсе.

lock1 = threading.Lock()
lock2 = threading.Lock()

def thread_task1():
    lock1.acquire()
    print('thread 1 lock1 acquride')
    lock2.acquire()
    print('thread 1 lock2 acquride')
    lock1.release()
    lock2.release()

def thread_task2():
    lock2.acquire()
    print('thread 1 lock2 acquride')
    lock1.acquire()
    print('thread 2 lock1 acquride')
    lock2.release()
    lock1.release()

t1 = threading.Thread(target=thread_task1)
t2 = threading.Thread(target=thread_task2)
t1.start()
t2.start()
t1.join()
t2.join()