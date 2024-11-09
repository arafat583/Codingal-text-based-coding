class Myclass:
    __privateVar = 27 

    def __privMeth(self):
        print("I'm inside my class")

    def hello(self):
        print("Private value: ", Myclass.__privateVar)

foo = Myclass()
foo.hello()
