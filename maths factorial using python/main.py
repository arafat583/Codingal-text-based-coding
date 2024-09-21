def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n-1)
    
num = int(input("Enter a number to turn it into factorial: "))

if num < 0:
    print("Factorial does not exists for negative numbers")
else:
    print(f"The factorial of {num} is {factorial(num)}")
