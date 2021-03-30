import random

def start():

                    # here you type in all the characters you want to use for your passwords.
                    characters = "abcdefghijklmnopqrstuvwxyz1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*"

                    # here you can type in how many characters you want your password to be.
                    length = input("How many characters would you like your password to have?     ")
                    length = int(length)

                    # we make a variable called password where the password will be to print out.
                    password = ' '

                    # the "c" is a variable and stands for characters. 
                    for c in range(length):
                        password += random.choice(characters)

                    # this is your output
                    print(password)

                    # here you can decide if you want to generate another password or if you want to quit the program
                    restart = input("Would you like to generate another password? type Yes if not type No      ")
                    restart = str(restart)
                    if (restart == "Yes"):
                        start()

                    if (restart == "No"):
                        exit()

start()
