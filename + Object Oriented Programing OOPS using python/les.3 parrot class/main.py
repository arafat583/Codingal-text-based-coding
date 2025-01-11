class Parrot:

    # class attribute / global varibale in class 
    species = "bird"

    def __init__(self,name,age,color):
        self.name = name
        self.age = age
        self.color = color

blu = Parrot("Blu",12,"Red")    
woo = Parrot("Woo",15,"Blue")

print("Blu is a {}".format(Parrot.species))
print("Woo is a {}".format(Parrot.species))

print("{} is {} years old".format(blu.name,blu.age))
print(f"Blue's color is {blu.color}")

print("{} is {} years old".format(woo.name,woo.age))
print(f"Blue's color is {woo.color}")

