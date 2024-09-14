import random

attempts_list = []

def show_score():
    if len(attempts_list) <= 0:
        print("There is currently no high score")
    else:
        print("The current high score is", min(attempts_list), " attempts")

def start_game():
    random_number = int(random.randint(1, 10))
    print("Hey There! Welcome to the game of guesses!") 
    player_name = input("Input your username here: ")
    wanna_play = input("Hi, {}, would you like to play the guessing game? yes/no: ".format(player_name))
    attempts = 0
    show_score()

    while wanna_play.lower() == "yes":
        try:
            guess = int(input("Pick a number between 1 and 10: "))

            if guess < 1 or guess > 10:
                raise ValueError("Please guess a number within the given range")

            attempts += 1

            if guess == random_number:
                print("Congrats! You guessed it right!")
                attempts_list.append(attempts)
                print("It took you {} attempts".format(attempts))
                play_again = input("Would you like to play again? yes/no: ")

                if play_again.lower() == "no":
                    print("That's cool, have a nice day!")
                    break
                else:
                    attempts = 0
                    show_score()
                    random_number = int(random.randint(1, 10))

            elif guess < random_number:
                print("It's higher")

            elif guess > random_number:
                print("It's lower")

        except ValueError as err:
            print("Invalid input! ({})".format(err))

    else:
        print("That's cool, have a nice day!")

if __name__ == '__main__':
    start_game()


              

                     