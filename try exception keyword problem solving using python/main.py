try:
    num = int(input("Enter a normal number"))
    print(num)
except ValueError as ex:
    print(f"You entered wrong format")    