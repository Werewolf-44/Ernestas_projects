#Simply Quiz game. Writing down last names of famous people. At the end score is printed out.

print("Welcome to 'Famous People' quiz! You need to write their last name")


while True:
    playing = input("Do you want to play 'Famous people' game? Type 'yes' or 'no' ")

    if playing.lower() == "yes":
        print("Great, let's move on to the first question!")
        break
    elif playing.lower() == "no":
        print("Sad to hear that...Well, maybe next time! Game ends here")
        exit()
    else:
        print("Invalid answer. Type 'yes' or 'no'. Please try again")


score = 0

answer = input("First question: His name is Brad? ")
if answer.lower() == "pitt":
    print("Brad {}. That is correct!".format(answer.capitalize()))
    score += 1
else: 
    print("Incorrect!")

answer = input("Second question: Her name is Angelina? ")
if answer.lower() == "jolie":
    print("Angelina {}. That is correct!".format(answer.capitalize()))
    score += 1
else: 
    print("Incorrect!")

answer = input("His name is Johny? ")
if answer.lower() == "depp":
    print("Johnny {}. That is correct!".format(answer.capitalize()))
    score += 1
else: 
    print("Incorrect!")

answer = input("His name is Orlando? ")
if answer.lower() == "bloom":
    print("Orlando {}. That is correct!".format(answer.capitalize()))
    score += 1
else: 
    print("Incorrect!")

answer = input("Her names is Catherine Zeta- ")
if answer.lower() == "jones":
    print("Catherine {}. That is correct!".format(answer.capitalize()))
    score +=1
else:
    print("Incorrect!")

print("You got " + str(score) + " questions correct! That is " + str((score/5) * 100) + "%.")
print("Thank you for playing the game!")