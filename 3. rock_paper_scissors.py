#Simple Rock/Paper/Sciccors game

print("This game is called Rock/Paper/Scissors. If you want to play the game - choose Rock, Paper or Scissors. If you do not want to play this game, type Q")
import random

player_wins = 0
computer_wins = 0
options = ["rock", "paper", "scissors"]

while True:
    player_input = input("Choose: Rock, Paper, Scissors or Q ").lower()
    if player_input == "q":
        break

    if player_input not in options:
        print("Invalid. You have to choose Rock, Paper or Scissors. Try again")
        continue

    random_guess = random.randint(0, 2)
    # 0 is Rock
    # 1 is Paper
    # 2 is Scissors

    computer_choice = options[random_guess]
    print("Computer choose", computer_choice + ".")

    if player_input == "rock" and computer_choice == "scissors":
        print("You've won!")
        player_wins += 1
    elif player_input == "paper" and computer_choice == "rock":
        print("You've won!")
        player_wins +=1
    elif player_input == "scissors" and computer_choice == "paper":
        print("You've won!")
        player_wins +=1
    elif player_input == computer_choice:
        print("It is a tie. Go again!")
    else:
        print("Computer wins!")
        computer_wins += 1

print("You won", player_wins, "times")
print("Computer won", computer_wins, "times")
print("Thank you for playing the game! You can play again by restarting. Goodbye!")


