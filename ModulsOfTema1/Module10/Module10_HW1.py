import threading
from random import randint
import requests
import time

class Bank():
    def __init__(self):
        self.balance = 0
        self.lock = threading.Lock()
        super().__init__()

    def deposit(self):
        for i in range(1, 101):
            if self.balance >= 500 and self.lock.locked():
                self.lock.release()
            transaction_d = randint(50, 500)
            self.balance += transaction_d
            print(f'Пополнение №: {i}')
            print(f'Пополнение: {transaction_d}. Баланс: {self.balance}')
            time.sleep(0.001)

    def take(self):
        for j in range(1, 101):
            transaction_t = randint(50, 500)
            print(f'Запрос на {transaction_t}')
            if transaction_t <= self.balance:
                self.balance -= transaction_t
                print(f'снятие №: {j}')
                print(f'Снятие: {transaction_t}. Баланс: {self.balance}')
            else:
                print(f'Запрос № {j} отклонен, недостаточно средств')
                self.lock.acquire()
bk = Bank()

th1 = threading.Thread(target=Bank.deposit, args=(bk,))
th2 = threading.Thread(target=Bank.take, args=(bk,))
th1.start()
th2.start()
th1.join()
th2.join()
print(f'Итоговый баланс: {bk.balance}')