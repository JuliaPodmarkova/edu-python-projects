# Конструкция очередь для работы с потоками бывает трех видов:
# 1. fifo (first in first out) - скорость обращения к элементам этой очереди
# будет самой быстрой

from queue import Queue

q = Queue()
q.put(6)
print(q.get(timeout=2)) # данный метод .get() блокирует программу внутри очереди,
# если к методу добавить timeout, то блокировка будет временной.
print('The end of program')

# 2. lifo - Первый рабочий будет класть с каким-то промежутком времени
# элементы в очередь, т.е. главный поток. Дальше создадим дополнительно
# поток, который будет из очереди доставать элементы.

import time
import threading

def getter(queue):
    while True:
    #while not queue.empty():
        time.sleep(5)
        item = queue.get()
        print('Element was taken', item)

q = Queue(maxsize=10)
t1 = threading.Thread(target=getter, args=(q,), daemon=True)
t1.start()

for i in range(10):
    time.sleep(2)
    q.put(i)
    print(threading.current_thread(), 'Put the element in queue')

# 3. priority

