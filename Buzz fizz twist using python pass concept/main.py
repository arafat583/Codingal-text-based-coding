import time

x = int(input("Enter a number: "))
r = int(input("Enter a range: "))

time.sleep(1)
print("Processing number and range")
time.sleep(3)

if x >= 10000:
    print("Input not supported")
else:
    print("Number supported")

time.sleep(1)

if r >= 10000:
    print("Input not supported")
else:
    print("Range Supported")

time.sleep(1)
print("Converting...")
time.sleep(3)

for i in range(r):
    if x % 20 == 0:
        print("twist!")
    elif x % 15 == 0:
        pass     
    elif x % 5 == 0:
        print("fizz")
    elif x % 3 == 0:
        print("buzz")
    else:
        print("x")            


