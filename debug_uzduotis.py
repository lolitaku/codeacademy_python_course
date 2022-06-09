class Human:
    def __init__(self, name: str, age: int, location: str):
        self.name = name
        self.age = age
        self.location = location

    def beautiful_soul(self):
        print('My soul is very beautiful')

class Child(Human):
    def description(self):
        return f"My name is {self.name}. I'm {self.age} years old and I live in {self.location}"

human1 = Human('Petras', 33, "Kaunas")
human2 = Child('Maryte', 13, "Varena")

print(human2.description())