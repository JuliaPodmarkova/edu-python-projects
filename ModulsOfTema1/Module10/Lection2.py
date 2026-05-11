import threading
import time

class MyThread(threading.Thread):
    def __init__(self, name, counter, delay):
        threading.Thread.__init__(self)
        # super().__init__(name=name)
        self.name = name
        self.counter = counter
        self.delay = delay

    def timer(self, name, counter, delay):
        while counter:
            time.sleep(delay)
            print(f'{name} {time.ctime(time.time())}')
            counter -= 1

    def run(self):
        print(f'Thread {self.name} started')
        self.timer(self.name, self.counter, self.delay)
        print(f'Thread {self.name} stopped')



tread1 = MyThread('tread1', 5, 1)
tread2 = MyThread("tread2", 3, 0.5)
tread1.start()
tread2.start()