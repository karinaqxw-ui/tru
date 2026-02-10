class Device:
    def on(self):
        print("Увімкнено")

    def off(self):
        print("Вимкнено")


class Phone(Device):
    pass


class Laptop(Device):
    pass


p1 = Phone()
p1.on()
p1.off()
