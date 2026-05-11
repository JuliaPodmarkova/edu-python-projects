#Задача "Range - это просто"
from turtledemo.penrose import start


class StepValueError(ValueError):
    def __init__(self, message):
        self.message = message

class Iterator:
    def __init__(self, start, stop, step = 1):
        if self._step(step):
            self.step = step
        self.start = start
        self.stop = stop

    def _step(self, stp):
        if stp == 0:
            raise StepValueError("Step must be greater than 0")
        return True

    def __iter__(self):
        self.pointer = self.start
        return self

    def __next__(self):
        res = self.pointer

        if ((self.step > 0 and self.pointer > self.stop) or
                (self.step < 0 and self.pointer < self.stop)):
            raise StopIteration()
        self.pointer += self.step
        return res

try:
    iter1 = Iterator(100, 200, 0)
    for i in iter1:
        print(i, end=' ')
except StepValueError:
    print('Шаг указан неверно')

iter2 = Iterator(-5, 1)
iter3 = Iterator(6, 15, 2)
iter4 = Iterator(5, 1, -1)
iter5 = Iterator(10, 1)

for i in iter2:
    print(i, end=' ')
print()

for i in iter3:
    print(i, end=' ')
print()

for i in iter4:
    print(i, end=' ')
print()

for i in iter5:
    print(i, end=' ')
print()

