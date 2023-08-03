#This code let's you cipher and decipher a message. This is an example of 'Caesar cipher'.

def cipher():
    ciphered_message = []
    for letter in message:
        if letter.isalpha():
            base_letters = ord('a') if letter.islower() else ord('A')
            ciphered_letter = chr((ord(letter) - base_letters + code) % 26 + base_letters)
            ciphered_message.append(ciphered_letter)
        else:
            ciphered_message.append(letter)
    print('Your ciphered message: ' + "".join(ciphered_message))


def decipher():
    deciphered_message = []
    for letter in message:
        if letter.isalpha():
            base_letters = ord('a') if letter.islower() else ord('A')
            deciphered_letter = chr((ord(letter) - base_letters - code) % 26 + base_letters)
            deciphered_message.append(deciphered_letter)
        else:
            deciphered_message.append(letter)
    print('Your deciphered message: ' + ''.join(deciphered_message))



print("Welcome! This program let's you cipher and decipher message in order to keep a secret.")
while(True):

    choice = input("If you've like to cipher a message, type 'cipher', if you want to decipher, type 'decipher': ")
    if choice == "cipher":
        message = input("Type your message: ")
        code = int(input("Type a number of you choosing: "))
        print('According to this number each letter in your message was shifted to the right side. DO NOT disclose this number to anyone else, except the person your message is intended to')
        cipher()
    elif choice == "decipher":
        message = input('Type in the message you want to decipher: ')
        code = int(input("Type a number to decipher the message: "))
        decipher()
    else:
        print('Invalid input. Please try again')