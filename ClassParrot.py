class parrot:
    species = "bird"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def intro(self):
        print("This is", self.name)
        print("This bird is", self.age, "years old")

p1 = parrot("Blu", 10)
p1.intro()
print("Parrot species is", p1.species)        