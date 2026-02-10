class Animal:
    def __init__(self, name):
        self.name = name


class Dog(Animal):
    def say(self):
        print(self.name, "гав")


class Cat(Animal):
    def say(self):
        print(self.name, "мяу")


d1 = Dog("Бобік")
c1 = Cat("Мурка")

d1.say()
c1.say()
