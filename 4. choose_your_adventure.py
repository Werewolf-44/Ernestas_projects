#Short adventure game to practice nested is/else statments.
name = input("Type in your name ")
print("Welcome",name, "to this adventure!")

answer = input("You are on a dirt road, it has come to an end and you can go left or right. Which way would you like to go (left/right)? "
               ).lower()

if answer == "left":
    answer = input("You come to a river, you can walk around it or swim across. Type walk or swim: ")

    if answer == "swim":
        print("You entered the water, started to swim BUT were eaten by an alligator")
    elif answer == "walk":
        print("You walked for many miles, ran out of water and you lost the game")
    else:
        print("Not a valid option. You lose!")

elif answer == "right":
    answer = input("You come to a bridge, it looks woobly, do you want to cross it or wait (cross/wait)? ")

    if answer == "wait":
        print("You have waited for hours, but no one came to help you. You lose the game!")
    elif answer  == "cross":
        answer = input("You cross the bridge and meet a stranger. Do you talk to them (yes/no)? ")

        if answer == "yes":
            print("You talked to the stranger and they give you gold. You WIN!")
        elif answer == "no":
            print("You ignored the stranger and they are offended. You LOSE!")
        else:
            print("Not a valid option. You lose!")
else:
    print("Not a valid option. You lose")

print("Thank you for playing! Try again!")