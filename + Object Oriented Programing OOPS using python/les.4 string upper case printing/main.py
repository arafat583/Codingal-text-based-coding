class IOString():

 def __init__(self):
      self.str1 = ""
 
 def get_string(self):
      self.str1 = input("What's your name?")

 def print_string(self):
     print("Your name is", self.str1.upper())  


str1 = IOString()
str1.get_string()
str1.print_string()



  