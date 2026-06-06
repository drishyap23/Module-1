class fruit:
    taste = 'sweet'

    def __init__(self, name, color):
        self.name = name
        self.color = color

    def intro(self):
        print("Hello, I am", self.name)

apple = fruit('Apple', 'Red')
orange = fruit('Orange', 'Orange')
apple.intro()
print(apple.color)
orange.intro()
print(orange.color)

print("Apples taste", apple.taste)
print("Oranges taste", orange.taste)