def addition(n1,n2):
    sum = n1 + n2
    return sum
def subtraction(n1,n2):
    difference = n1 - n2
    return difference
num1 = int(input("Enter your first number: "))
num2 = int(input("Enter your second number: "))
result = addition(num1, num2)
print("The sum of your two numbers is", result)
result = subtraction(num1, num2)
print("The difference of your two numbers is", result)