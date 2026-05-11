import threading
import time


print(threading.current_thread()) # Вернёт объект потока, и в случае с основным потоком
                                  # результатом будет ‘MainThread’. (Объект)

print(threading.enumerate()) # возвращает список всех активных потоков в программе (Список)

def func1():
    for i in range(10):
        time.sleep(0.5)
        print(i, threading.current_thread())

def func2(x):
    for i in range(10):
        time.sleep(1)
        print(i, threading.current_thread())
        print(threading.current_thread().is_alive())

thread = threading.Thread(target=func2, args=(1, ), daemon=True)
thread.start() # Метод запуска потока
thread.join() # Главный поток создает вспомогательный,
# запускает его и приостанавливается, ожидая завершения работы
# вспомогательного потока.
print(thread.is_alive()) #  Этот метод позволяет определить, активен
# ли поток в данный момент, то есть выполняет ли он ещё какие-то задачи
func1()
print(threading.enumerate())
print(threading.current_thread())