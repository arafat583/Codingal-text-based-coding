class Dog:

    main_species = "Dog"

    def __init__(self,name,age,personality,lifespan,dog_species,price):
        self.name = name
        self.age = age
        self.personality = personality 
        self.lifespan = lifespan 
        self.dog_species = dog_species
        self.price = price 


kenny = Dog("Kenny",8,"Friendly, highly social and intelligent","10-12 years","Labrador Retriever","1800$")    
jenny = Dog("Jenny",6,"Loyal, protective, highly intelligent","9-13 years old","German Shephard","2500$")

print(f"{kenny.name} is a {kenny.main_species}. His age is {kenny.age} years old. He is {kenny.personality}. His Lifespan is {kenny.lifespan}. His breed is {kenny.dog_species}. His price is {kenny.price}")
print(f"{jenny.name} is a {jenny.main_species}. His age is {jenny.age} years old. He is {jenny.personality}. His Lifespan is {jenny.lifespan}. His breed is {jenny.dog_species}. His price is {jenny.price}")