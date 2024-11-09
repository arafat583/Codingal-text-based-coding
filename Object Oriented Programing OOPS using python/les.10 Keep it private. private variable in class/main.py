class Myclass:
    __privateVar = 27 

    def __privMeth(self):
        print("I'm inside my class")

    def hello(self):
        print("Private value: ", Myclass.__privateVar)

foo = Myclass()
foo.hello()

print("-------------")

class computer:

    def __init__(self):
        self.__maxprice = 500


    def sell(self):
        print("Selling price: {}".format(self.__maxprice))

     # To change private variable:
    def setmaxprice(self, price):
        self.__maxprice = price     


c = computer()
c.sell()

c.__maxprice = 1000
c.sell()

c.setmaxprice(1000)
c.sell()


