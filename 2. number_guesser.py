#Simple number guesser. You select a range of number: from 0 to your choosing. Computer makes a guess (random number) and a player chooses a number. Goal of the game: player have to
#correctly guess the number that the computer chose is as less tries as possible.

import random

print("Welcome to 'Number Guessing game'. It is a very simple game, just follow the instructions. ")

while True:

    answer = input("Think of a number. This number will be the upper limit in this game. Computer will choose a number between 0 and the number that you choose right now. Type a number of your choosing: ")

    if answer.isdigit():
        answer = int(answer)
        
        if answer <= 0:
            print("Please type a number larger than 0")
    else:
        print("Please type a number next time.")
        continue
    break
        
random_number = random.randrange(0, answer) #.randint also works, if you want to include the last number.

guesses = 0

while True:
    guesses += 1
    user_guess = input("Computer has chosen a number. Make your guess: ")
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print("Please type a number! Try again")
        continue

    if user_guess == random_number:
        print("You are correct!")
        break
    elif user_guess > random_number:
            print("You were above the number. Try again!")
    else: 
            print("You were below the number. Try again!")

print("You got it in {} guesses.".format(guesses))
