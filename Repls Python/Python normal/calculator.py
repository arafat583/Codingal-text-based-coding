num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
operator = input("Enter an operation (*,/,+,-): ")

def multiplication(num1, num2):
    if operator == "*":
        result = num1 * num2
        print(num1, "*", num2, "=", result)

def division(num1, num2):
    if operator == "/":
        if num2 != 0:
            result = num1 / num2
            print(num1, "/", num2, "=", result)
        else:
            print("Error: Division by zero is not allowed.")

def addition(num1, num2):
    if operator == "+":
        result = num1 + num2
        print(num1, "+", num2, "=", result)

def subtraction(num1, num2):
    if operator == "-":
        result = num1 - num2
        print(num1, "-", num2, "=", result)

if operator == "*":
    multiplication(num1, num2)
elif operator == "/":
    division(num1, num2)
elif operator == "+":
    addition(num1, num2)
elif operator == "-":
    subtraction(num1, num2)
else:
    print("Invalid operator.")
