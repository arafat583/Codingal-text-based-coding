from abc import ABC 

class animal(ABC):
    def move(self):
        pass


class human(animal):
    def move(Self):
        print("I can walk and run")

class snake(animal):
    def move(Self):
        print("I crawl")

class parrot(animal):
    def move(Self):
        print("I can fly and walk")

class cat(animal):
    def move(Self):
        print("I can walk and run")

class dog(animal):
    def move(Self):
        print("I can walk and run")                                

human = human()
human.move()

snake = snake()
snake.move()

parrot = parrot()
parrot.move()

cat = cat()
cat.move()

dog = dog()
dog.move()

print("end")