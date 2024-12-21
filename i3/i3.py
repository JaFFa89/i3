class Animal:
    def __init__(self, name):
        self.name = name

    def sound(self):
        print(f"{self.name} дає звук")

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed

    def sound(self):
        print(f"{self.name} гавкає")

    def a(self):
        print(f"{self.name} приносить палку")

class Cat(Animal):
    def __init__(self, name, color):
        super().__init__(name)
        self.color = color

    def sound(self):
        print(f"{self.name} мяукая")

    def b(self):
        print(f"{self.name} карабкається на дерево")

dog = Dog("пончик", "хаски")
cat = Cat("мурка", "білий")

dog.sound()
dog.a()

cat.sound()
cat.b()
