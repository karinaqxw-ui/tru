class Transport:
    def __init__(self, speed):
        self.speed = speed

    def move(self):
        print("Їде зі швидкістю", self.speed)


class Car(Transport):
    pass


class Bike(Transport):
    pass


c1 = Car(100)
b1 = Bike(25)

c1.move()
b1.move()
