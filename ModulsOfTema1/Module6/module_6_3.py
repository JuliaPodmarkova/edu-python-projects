import random as rd

class Animal:
    live = True
    sound = None
    _DEGREE_OF_DANGER = 0

    def __init__(self, speed):
        self.speed = speed
        self._coords = [0, 0, 0]

    def move(self, dx, dy, dz):
        new_x = self._coords[0] + dx * self.speed
        new_y = self._coords[1] + dy * self.speed
        new_z = self._coords[2] + dz * self.speed
        if new_z < 0:
            print("It's too deep, i can't dive :(")
        else:
            self._coords = [new_x, new_y, new_z]

    def get_coords(self):
        print(f'X: {self._coords[0]}, Y: {self._coords[1]}, Z: {self._coords[2]}')

    def attack(self):
        if self._DEGREE_OF_DANGER < 5:
           print("Sorry, i'm peaceful :)")
        else:
            print("Be careful, i'm attacking you 0_0")

    def speak(self):
        self.sound = str()

class Birds(Animal):
    beak = True
    def lay_eggs(self):
        number_of_eggs = rd.randint(1, 4)
        print(f'Here are(is) {number_of_eggs} eggs for you')

class AquaticAnimal(Animal):
    _DEGREE_OF_DANGER = 3
    def dive_in(self, dz):
        new_z = self._coords[2] - abs(dz) * .5 * self.speed
        self._coords[2] = int(max(new_z, 0))

class PoisonousAnimal(Animal):
    _DEGREE_OF_DANGER = 8

class Duckbill(PoisonousAnimal, Birds, AquaticAnimal):
    sound = 'Click-click-click'

db = Duckbill(10)
print(db.live)
print(db.beak)

db.speak()

db.attack()

db.move(1, 2, 3)

db.get_coords()

db.dive_in(6)

db.get_coords()

db.lay_eggs()