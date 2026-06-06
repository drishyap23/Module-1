class student:
    grade = 8
    name = "Drishya"

    def introduction(self):
        print("Hi I am a student")

    def display(self):
        print("My name is", self.name, "and I am in Grade", self.grade)
s1 = student()
s1.introduction()
s1.display()