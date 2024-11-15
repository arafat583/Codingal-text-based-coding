class Ind():
    def capital(self):
       print("Delhi is my capital city")

    def language(self):
      print("Hindi is my main language.")

    def type(self):
       print("I am a Developing country")

class Bd():
    def capital(self):
        print("My capital is Dhaka")
    def language(self): 
        print("My main language is Bangla")
    def type(self):
        print("I am a developing country")

obj_ind = Ind()
obj_bd = Bd()

for country in obj_ind, obj_bd:
     country.capital()
     country.language()
     country.type()


  