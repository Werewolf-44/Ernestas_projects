#This is your personal Password Manager. You can use it to add log in and password information in a txt file called "passwords". Also, you can generate new passwords
# if you can't think of anything yourself.

import string
import random

print("Welcome to you personal Password Manager. Here you can generate, add and view your log in and password information. All passwords are save into a text file called 'passwords'")

def add():
    name = input("Account Name: ")
    pwd = input("Password: ")


    with open("passwords.txt", "a") as f:
        f.write(name + "|" + pwd + "\n")

    print("Your new password has been saved")

def view():
    with open("passwords.txt", 'r') as f:
        for line in f.readlines():
            data = line.rstrip()
            log_in, password = data.split("|")
            print("Log in: ", log_in, "| Password: ", password)

def generate(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    random_pwd = "".join(random.choice(characters) for _ in range(int(length)))
    print("Your new password is: " + random_pwd + " .Copy this password. You can now type 'add', create new log in and paste this password")


def user_choice():
    while True:
        mode = input("If you like to generate new password, add a new password or view existing ones type: 'generate', 'add' or 'view'. You can also exit the program by typing 'q' ")
        if mode == "q":
            print("Exiting the program now. Have a nice day!")
            exit()

        if mode == "view":
            view()
            continue
        elif mode == "add":
            add()
            continue

        elif mode == "generate":
            mode_2 = input("Type 'create'. You can go back to Main menu (type 'back') or Quit program (type 'q') ")
            if mode_2 == "create":
                mode_3 = input("How long do you want your character to be? Type a number: ")
                generate(mode_3)
                continue
            elif mode_2 == "back":
                continue
            elif mode_2 == "q":
                print("Exiting the program now. Have a nice day!")
                exit()
            else:
                print("Invalid mode.")
                continue

        else:
            print("Invalid mode.")
            continue
    
user_choice()