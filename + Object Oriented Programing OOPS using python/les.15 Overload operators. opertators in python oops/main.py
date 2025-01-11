class a:

    def __init__(self,a):
        self. a = a 

    def __lt__(self, other):
        if self.a < other.a:
            return "obj 1 is less than 2"
        else:
            return "obj2 is less than obj 1"
        
    def __eq__(self, other):
       if self.a == other.a:
         return "Both are equal"
       else:
        return "Both are unequal"
       
      
ob1 = a(2)
ob2 = a(3)

print("passed values: {}".format(ob1.a, ob2.a))

ob3 = a(4)           
ob4 = a(4)

print("passed values: {}".format(ob3.a, ob4.a))
print(ob3 == ob4)
        

        