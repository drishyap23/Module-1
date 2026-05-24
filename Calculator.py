def addition(n1,n2):
    sum = n1 + n2
    return sum
def subtraction(n1,n2):
    difference = n1 - n2
    return difference
def multiplication(n1,n2):
    product = n1 * n2
    return product
def division(n1,n2):
    quotient = n1 / n2
    return quotient
num1 = int(input("Enter your first number: "))
num2 = int(input("Enter your second number: "))
result = addition(num1, num2)
print("The sum of your two numbers is", result)
result = subtraction(num1, num2)
print("The difference of your two numbers is", result)
result = multiplication(num1, num2)
print("The product of your two numbers is", result)
result = division(num1, num2)
print("The quotient of your two numbers is", result)