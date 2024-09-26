import time
import sys
def main():
 print("Welcome to Shop-99 Store")
 print("This is a grocery shop")
 time.sleep(1)
 wannabuy = str(input("Do you wanna buy something? yes/no: ")).lower()
 if wannabuy == "yes":
     print("Loading Available items....")
     time.sleep(2)
 else:
     print("Leaving the store....")
     time.sleep(1)
     sys.exit()

 available_items = ["tomato", "potato", "ginger", "eggplant", "beans", "onions", "carrots", "steak", "milk", "egg", "fish", "spices", "rice", "biscuit"]
 print(f"The available items are: {available_items}")
 time.sleep(1)
 
 bought = str(input("What item you wanna buy from the available items? format: item, item")).lower()

 cost = 0

 if bought in available_items:
     print("Loading the full cost...")
     if "tomato" in bought:
         cost += 12
     if "potato" in bought:
         cost += 18
     if "ginger" in bought:
         cost += 8
     if "eggplant" in bought:
         cost += 16
     if "beans" in bought:
         cost += 10
     if "onions" in bought:
         cost += 10
     if "carrots" in bought:
         cost += 12
     if "steak" in bought:
         cost += 30
     if "milk" in bought:
         cost += 18
     if "egg" in bought:
         cost += 18
     if "fish" in bought:
         cost += 32
     if "spices" in bought:
         cost += 22
     if "rice" in bought:
         cost += 95
     if "biscuit" in bought:
         cost += 14      

     time.sleep(3)
     print(f"The due amount is {cost}")
 else:
     print("Item not available in the store")
     check_again = str(input("Wanna check again? yes/no")).lower()
     if check_again == "yes":
         main()
     else:
         print("Great! exiting the shop. Your taken items will be returned")
         sys.exit()    









