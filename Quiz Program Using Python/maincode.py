import time
print("Hey there! welcome to quiz app")
username = str(input("To continue input an username: ").lower())
print("Loading...")
time.sleep(5)
print("Your points start from 0")
time.sleep(1)

point = 0

q1 = input("Which city is the capital of the france?")
q1_choices = ['lyon', 'paris', 'lille', 'nantes']
q1_answer = str(input("Select 1 city: {q1_choices}.").lower())
if q1_answer == q1_choices[1]:
    print("Correct! Your point increases by 1 :)")
    point += 1
else:
    print("You'r incorrect, Your point decreases by 1")
    point -= 1

q2 = input("")    