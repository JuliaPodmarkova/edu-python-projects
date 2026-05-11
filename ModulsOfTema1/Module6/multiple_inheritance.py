from tokenize import group


class Human:
    def __init__(self, name, group):
        self.name = name
        super().__init__(group)

    def info(self):
        print(f'Привет, меня зовут {self.name}')

class StudentGroup:
    def __init__(self, group):
        self.group = group

    def about(self):
        print(f'{self.name} учится в группе {self.group}')

class Student(Human, StudentGroup):
    def __init__(self, name, place, group):
        super().__init__(name, group)
        self.place = place
        super().info()

#human = Human("Denis")
#print(human.name)
student1 = Student("Maxim", "Urban", "Python1")
print(f'{student1.name} learning in {student1.place} at {student1.group} group')
##=print(Human.mro())
#print(Student.mro())