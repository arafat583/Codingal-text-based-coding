try:
    num = int(input("Enter a normal number"))
    print(num)
except ValueError as ex: 
    print("You entered wrong format") 
    print(f"Exception: {ex}")   