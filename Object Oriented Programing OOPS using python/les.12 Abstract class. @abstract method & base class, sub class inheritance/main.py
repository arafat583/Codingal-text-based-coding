from abc import ABC, abstractmethod 

class absclass(ABC):
    
    def print(self,x):
        print("Passed value: {}".format(x))

    # ABstracT method    
    @abstractmethod
    def task(self):
        print("WE are inside abstract task")

class test_class(absclass):
    def task(self):
        print("We are inside abstract task")


obj = test_class()
obj.task()
try:
 x = int(input("give a number to print"))
except ValueError:
    print("Wrong format") 
obj.print(x)   
