import random 

class fruitquiz:

    def __init__(self):

        self.fruits = {'apple':'red', 'orange':"orange", 'watermelon':'green', 'banana':'yellow'}

    def quiz(self):
        while True:

            fruit, color = random.choice(list(self.fruits.items()))

            print(f"what is the color of {fruit}")
            user_answer = input()

            if user_answer.lower() == color:
                print("Correct answer") 
            else:
                print("Incorrect answer")

            option = int(input("enter 0 if you want to play again else 1"))   
            if option:break 

print("welcome to fruitquiz")
fq = fruitquiz()
fq.quiz()                   