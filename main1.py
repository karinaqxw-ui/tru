class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


class Driver(Person):
    def __init__(self, name, age, license_num):
        self.name = name
        self.age = age
        self.license_num = license_num


d = Driver("Іван", 30, "AB1234")
print(d.name, d.age, d.license_num)
