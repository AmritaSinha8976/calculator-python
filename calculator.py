import math

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y

def power(x, y):
    return x ** y

def square_root(x):
    return math.sqrt(x)

def logarithm(x):
    return math.log10(x)

def sine(x):
    return math.sin(math.radians(x))

def cosine(x):
    return math.cos(math.radians(x))

def tangent(x):
    return math.tan(math.radians(x))

def exponent(x):
    return math.exp(x)

def factorial(x):
    return math.factorial(x)

print("Select operation.")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")
print("5. Power")
print("6. Square Root")
print("7. Logarithm")
print("8. Sine")
print("9. Cosine")
print("10. Tangent")
print("11. Exponent")
print("12. Factorial")
print("0. Exit")

while True:
    choice = input("Enter choice (0-12): ")

    if choice == '0':
        print("Exiting the calculator...")
        break

    if choice in ('1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12'):
        if choice == '1':
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            print(num1, "+", num2, "=", add(num1, num2))

        elif choice == '2':
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            print(num1, "-", num2, "=", subtract(num1, num2))

        elif choice == '3':
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            print(num1, "*", num2, "=", multiply(num1, num2))

        elif choice == '4':
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            print(num1, "/", num2, "=", divide(num1, num2))

        elif choice == '5':
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            print(num1, "^", num2, "=", power(num1, num2))

        elif choice == '6':
            num = float(input("Enter a number: "))
            print("Square root of", num, "=", square_root(num))

        elif choice == '7':
            num = float(input("Enter a number: "))
            print("Logarithm of", num, "=", logarithm(num))

        elif choice == '8':
            num = float(input("Enter a number: "))
            print("Sine of", num, "degrees =", sine(num))

        elif choice == '9':
            num = float(input("Enter a number: "))
            print("Cosine of", num, "degrees =", cosine(num))

        elif choice == '10':
            num = float(input("Enter a number: "))
            print("Tangent of", num, "degrees =", tangent(num))

        elif choice == '11':
            num = float(input("Enter a number: "))
            print("Exponential value of", num, "=", exponent(num))

        elif choice == '12':
            num = int(input("Enter a number: "))
            print("Factorial of", num, "=", factorial(num))

    else:
        print("Invalid input. Please enter a valid choice.")
