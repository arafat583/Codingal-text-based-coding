d = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}


key = int(input("Enter the key: "))

if key in d:
    print(f"The value for key {key} is {d[key]}")
else:
    print("Key not found in the dictionary.")