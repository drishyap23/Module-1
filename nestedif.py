number = float(input("Enter Age "))
if number >= 0:
    if number > 18:
        print("Adult")
    elif number < 18:
        print("Underage")
else:
    print("Enter Valid Age")