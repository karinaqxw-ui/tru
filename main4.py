class Language:
    def __init__(self, name):
        self.name = name

    def hello(self):
        print("Привіт від", self.name)


class PythonLang(Language):
    pass


class JavaLang(Language):
    pass


p1 = PythonLang("Python")
j1 = JavaLang("Java")

p1.hello()
j1.hello()
