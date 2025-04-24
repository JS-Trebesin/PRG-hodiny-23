class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.alive = True

    def greeting(self):
        print(f"Hello, I'm {self.name}")

    def parting(self):
        print(f"Bye, {self.name} is out!")



fridolin = Person("Fridolín", 102)

fridolin.greeting()
fridolin.parting()

radim = Person("Radim", 56)
radim.greeting()

class Student(Person):
    def __init__(self, name, age, class_name):
        super().__init__(name, age)
        self.class_name = class_name


svatoplukyne = Student("Svata", 17, "1.B")
svatoplukyne.greeting()

print(svatoplukyne.alive)
