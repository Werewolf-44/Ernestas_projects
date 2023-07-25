#Simple number Guesser. You select a range of number: from 0 to your choosing. Computer makes a guess (random number) and a player chooses a number. Goal of the game: player have to
#correctly guess the number that the computer chose is as less tries as possible.

import random

print("Welcome to 'Number Guessing game'. It is a very simple game, just follow the instructions")

while True:

    answer = input("Type a number of your choosing. This number will be the upper limit in this game. Computer will choose a number between 0 and the number that you choose right now. ")

    if answer.isdigit():
        answer = int(answer)
        
        if answer <= 0:
            print("Please type a number larger than 0")
    else:
        print("Please type a number next time.")
        continue
    break
        
random_Number = random.randrange(0, answer) #.randint also works, if you want to include the last number.

guesses = 0

while True:
    guesses += 1
    user_guess = input("Make a guess. Write down a number of your choosing: ")
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print("Please type a number! Try again")
        continue

    if user_guess == random_Number:
        print("You are correct!")
        break
    elif user_guess >random_Number:
            print("You were above the number!")
    else: 
            print("You were below the number!")

print("You got it in", guesses, "guesses")
