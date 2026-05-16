number = int(input("Enter Number: "))
if number>50:
    print("Your number is greater than 50")
    if number%2 == 0:
       print("Your number is even")
    else:
       print("Your number is odd")
else:
   print("Your number is less than 50")