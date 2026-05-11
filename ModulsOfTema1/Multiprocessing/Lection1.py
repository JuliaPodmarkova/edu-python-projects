import multiprocessing as mp
import time
import threading

counter = 0

def first_worker(n):
    global counter
    for i in range(n):
        counter += 1
        time.sleep(1)
        print('Первый рабочий изменил значение счетчика', counter)
    print('Первый рабочий изменил значение счетчика', counter)

def second_worker(n):
    global counter
    for i in range(n):
        counter += 1
        time.sleep(1)
        print('Второй рабочий изменил значение счетчика', counter)
    print('Второй рабочий изменил значение счетчика', counter)

'''t1 = threading.Thread(target=first_worker, args=(10, ))
t2 = threading.Thread(target=second_worker, args=(5, ))
t1.start()
t2.start()'''

if __name__ == '__main__':
    p1 = mp.Process(target=first_worker, args=(10, ))
    p2 = mp.Process(target=second_worker, args=(15, ))
    p1.start()
    p2.start()