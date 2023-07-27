#This is your personal Password Manager. You can use it to add log in and password information in a txt file called "passwords"

print("Welcome to you personal Password Manager. Here you can add and view your log in and password information. All passwords are save into a text file called 'passwords'")

def add():
    name = input("Account Name: ")
    pwd = input("Password: ")


    with open("passwords.txt", "a") as f:
        f.write(name + "|" + pwd + "\n")

def view():
    with open("passwords.txt", 'r') as f:
        for line in f.readlines():
            data = line.rstrip()
            log_in, password = data.split("|")
            print("Log in: ", log_in, "| Password: ", password)


while True:
    mode = input("Would like to add a new password or view existing ones? You can also exit the program by clicking 'q' ")
    if mode == "q":
        print("Exiting the program now. Have a nice day!")
        break

    if mode == "view":
        view()
    elif mode == "add":
        add()
    else:
        print("Invalid mode.")
        continue