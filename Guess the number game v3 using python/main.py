import random 
import time 

def intro():
 number = random.randint(1,100) 
 global name 
 name = input("What's your name? ")
 time.sleep(1)
 print(name + " Welcome to number guessing game!")
 time.sleep(.5)
 print("We will be given a clue about the number in between 1 and 100.")
 time.sleep(.5)
 if (number%2==0):
     print("The number is an odd number")
 else:
     print("The number is an even number")    
 time.sleep(1) 
 print("Go Ahead!")   

def main():
   guess_taken = 0
   try:
     user_number = int(input("Enter an Integer between 1-100: "))
   except ValueError:
      print(f"Sorry the given input {user_number} isnt a number") 
   if user_number != number:
      print("try again")
      guess_taken += 1 
   if user_number > number: 
      print("Your guess is greater than the number")   
      guess_taken += 1
      if user_number > 100:
         print("You cant enter a number greater than 100")
         recall()
         guess_taken += 1
   if user_number < number: 
      print("Your guess is smaller than the number")
      guess_taken += 1
      if user_number < 1 or user_number == 0:
          print("You cant enter a smaller number than 1")
          recall()
          guess_taken += 1
   if user_number == number:
      print("You guessed the right number! Congrats") 
      time.sleep(1)
      try:
         try_again = str(input("Do you want to try again? Yes/No: "))
      except ValueError:
         print("You entered wrong value")   
        


def recall():
 time.sleep(2)
 if (number%2==0):
     print("The number is an odd number")
 else:
     print("The number is an even number")    
 time.sleep(1) 
 print("Go Ahead!")   
 main()

   
    
        

    