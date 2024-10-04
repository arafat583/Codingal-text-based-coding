
def hotel_cost():
  try: 
     spend_nights = int(input("How many nights do you want to spend? Input Integer only: "))
  except ValueError:
     print("Wrong Input") 

  return 140 * spend_nights

def plane_ride_cost():
   try:
     city = str(input("What city you wanna go among these? Dhaka, Delhi, Saint Martin, Kolkata. Use Given Form: "))
   except ValueError:
      print("Wrong Input")  
   
   if "Dhaka" == city:
      return 10124  
   elif "Delhi" == city:
      return 10608
   elif "Saint Martin" == city:
      return 10890
   elif "Kolkata" == city:
      return 10308
   
def rental_car_cost():
   try:
      days = int(input("How many days you wanna spend? "))
   except ValueError:
      print("Wrong Input") 

      if days >= 7:
         return 8090 * days - 50
      elif days >= 3:
          return 7000 * days - 20
      else:
         return 6000 * days - 15
    
hc = hotel_cost()
prc = plane_ride_cost()
rcc = rental_car_cost()

def trip_cost():
   return hc + prc + rcc

print(f"Cost of hotel: {hc}")
print(f"Cost of car rental: {rcc}")
print(f"Cost of plane ride: {prc}")


      

   


