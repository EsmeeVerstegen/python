import random

def start():
    # here you type in all the characters you want to use for your passwords.
    characters = "abcdefghijklmnopqrstuvwxyz1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*"

    # here you can type in how many characters you want your password to be.
    input_length = input("How many characters would you like your password to have? (minimal 8)    ")
    length = int(input_length)
    return(length)

def passlength():
    if (length >= 8):
        print("Your length is valid")
        make_passwd()
    
    else:
        print("not long enough")
        passlength()
    
def make_passwd():
    # we make a variable called password where the password will be to print out.
    password = ' '
                    
    # the "c" is a variable and stands for characters. 
    for c in range(length):
        password += random.choice(characters)

    # this is your output
    print(password)

# here you can decide if you want to generate another password or if you want to quit the program
def start_again():    
    restart = input("Would you like to generate another password? type yes or y if not type no or n      ")
    restart = str(restart)
    if (restart == "Yes" or "yes" or "Y" or "y"):
        start()

    if (restart == "No" or "no" or "N" or "n"):
        exit()
    
    else:
        print("Please type yes or no.")
        start_again()
                        
start()
