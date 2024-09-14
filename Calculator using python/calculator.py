def calculator(operator, first_number, second_number):
    if operator == "/":
        print("Result: ", first_number / second_number)
    elif operator == "*":
        print("Result: ", first_number * second_number)
    elif operator == "+":
        print("Result: ", first_number + second_number)
    elif operator == "-":
        print("Result: ", first_number - second_number)
    else:
        print("Invalid operator!")

def wait():
    a = 1
    b = 0
    while a == 1:
        b += 1
        if b > 1015:
            break

def open_again():
    print("Opening")
    wait()
    start_calculator()

def restart_or_break():
    restart = input("Restart Calculator?: yes/no: ")   
    if restart == "yes":
        print("Restarting")
        wait()
        start_calculator()
    else:
        print("Stopped Calculator")
        start_again = input("Do you want to open Calculator again?: yes/no: ")
        if start_again == "yes":
            print("Cool! Calculator Opening again")
            wait()
            open_again()
        else:   
            print("OK, Cool")

def start_calculator():
    operator = input("Please enter any operator: /, *, +, -: ")
    first_number = int(input("Enter your first number: "))
    second_number = int(input("Enter your second number: "))
    
    calculator(operator, first_number, second_number)
    restart_or_break()

start_calculator()
