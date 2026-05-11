from threading import Thread

def count_up(name, n):
    for i in range(n):
        print(name, i, sep=": ")

t1 = Thread(target=count_up, args=("Thread1", 20))
t2 = Thread(target=count_up, args=("Thread2", 20))

t1.start()
t2.start()

t1.join()
t2.join()