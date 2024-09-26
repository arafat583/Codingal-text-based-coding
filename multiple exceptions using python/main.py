try:
    num1, num2 = eval(input("Enter two numbers, put comma between every number: "))
    result = num1 / num2
    print(f"The result is {result}")
except ZeroDivisionError:
    print("Division by 0 is error")
except ValueError:
    print("Wrong Value or form") 
except SyntaxError:
    print("Comma is missing, enter commas between every number")       
finally:
    print("Have a great day")

         