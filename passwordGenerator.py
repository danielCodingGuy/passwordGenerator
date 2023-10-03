#Program that generates random password after entering length of the password
#Author: DanielCodingGuy

import random

def generatePassword(n):
    #Defining which characters can be used in order to create a password
    characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789!@#$%^&*()"

    chosenLetter = random.sample(characters, n)

    #Converting list to string
    password = "".join(chosenLetter)

    return password


if __name__ == "__main__":
    #If we dont like the password user can choose if he want to generate another one or end the program
    while True:
        usersChoice = input(
            "If you want to generate password enter 'yes' otherwise enter 'no' to exit ")
        if usersChoice == 'no':
            break
        else:
            n = int(input("Enter the length of the password: "))
            password = generatePassword(n)
            print("Generated password:", password)