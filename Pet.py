# программа для работы с домашними животными

class Pet:
    def __init__(self, name, species, age, weight):
        self.name = name
        self.species = species
        self.age = age
        self.weight = weight

    def feed(self, food):
        print(f"{self.name} is eating {food}...")

    def exercise(self, duration):
        print(f"{self.name} is exercising for {duration} minutes...")

# создание объектов класса Pet
dog = Pet("Fido", "dog", 3, 20)
cat = Pet("Whiskers", "cat", 2, 10)

# вывод информации о домашних животных
print(f"{dog.name} is a {dog.species} and is {dog.age} years old.")
print(f"{cat.name} is a {cat.species} and weighs {cat.weight} pounds.")

# кормление и занятия животных
dog.feed("dog food")
cat.exercise(30)
