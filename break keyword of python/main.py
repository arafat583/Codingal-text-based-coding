name = str(input("Enter a name:")).upper()

for i in name:
    if i == "A":
        print("A found")
        break
    else:
        print("A not found")