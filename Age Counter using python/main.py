# Age counter

import time


print("This is an age counter")
print("It checks your age and give info's about your age")
print("Lets go...")
time.sleep(1)

try: 
  age = int(input("Enter your age"))
except ValueError:
  print("Invalid Input")

print("Checking Your age...")
time.sleep(2)

if age <= 9:
  print("You are a child")
elif age >= 10 and age <= 19:
  print("You are a teenager")
elif age >= 20 and age <= 28:
  print("You are a youngstar") 
elif age >= 29 and age <= 55:
  print("You are an adult")
elif age >= 55:
  print("You are an elder citizen")

print("Checking odd or even")
time.sleep(1)

if age % 2 == 0:
  print("Your age is an even number")
else:
  print("Your age is an odd number")


 




     
  

   