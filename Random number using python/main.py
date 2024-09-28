def main():
 
 import random
 import sys
 import time

 randomm = random.randint(0,9)

 print("Welcome to Number guessing game")
 print("You have to Guess the right number")
 time.sleep(1)

 try:
     numberr = int(input("Enter your number"))
 except ValueError:
     print("Wrong format") 
     time.sleep(1)
     print("Loading again...")
     time.sleep(1)
     main()

 if numberr == randomm:
    print("Your guess is correct")
 else:
    print("You are wrong!")
    
    try:
     try_again = str(input("Do you wanna try again? yes/no: ")).lower()
    except ValueError:
     print("Wrong format")
     time.sleep(1)
     print("Loading again...")
     time.sleep(1)
     main()
       
    
    if try_again == "yes":
       print("Great!")
       time.sleep(1)
       print("Loading game...")
       time.sleep(2)
       main()
    else:
       print("Cool!")
       sys.exit()   

main()

