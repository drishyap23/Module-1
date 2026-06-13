class Animal:
    def __init__(self, name, habitat):
        self.name    = name
        self.habitat = habitat
        
class Dog(Animal):
    def __init__(self, name, habitat, breed):
        super().__init__(name, habitat)
        self.breed = breed

class Parrot(Animal):
    def __init__(self, name, habitat, phrase):
        super().__init__(name, habitat)
        self.phrase = phrase

d = Dog("Bruno", "Home", "Labrador")
p = Parrot("Rio", "Brazil", "Spix's Macaw")
print("Dog Name:", d.name, "Dog Habitat:", d.habitat, "Dog Breed:", d.breed) 
print("Parrot Name:", p.name, "Parrot Habitat:", p.habitat, "Parrot Species:", p.phrase)