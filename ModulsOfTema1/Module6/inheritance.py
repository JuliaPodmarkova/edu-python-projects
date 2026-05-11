class Human:
    head = True
    _legs = True
    __arms = True

    def sayHello(self):
        print("Hello")

    def about(self):
        print(self.head)
        print(self._legs)
        print(self.__arms)

class Student(Human):
    arms = False
    #pass
    #def about(self):
    #    print('Я студент.')

class Teacher(Human):
    pass

human = Human()
student = Student()
print(human.head)
student.about()
print(student.head)
teacher = Teacher()
teacher.sayHello()
student.sayHello()
human.about()
print(dir(human))
print(dir(student))
print(student._Human__arms)