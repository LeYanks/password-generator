import random 

# Déclaration variables
letter = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
number = "0123456789"
symbol = "§£$%@#{}[]()!"
character = letter + letter.lower() + number + symbol
character_without_symbols = letter + letter.lower() + number

while True:
    pass_length = int(input("Entrez la longueur du mot de passe : "))
    pass_number = int(input("Entrez le nombre de mot de passe à générer : "))
    special_character = str(input("Mot de passe avec caractères spéciaux ou non ? : "))

    if special_character == "oui":
        for i in range(0,pass_number):
            passw = ""
            for i in range(0,pass_length):
                pass_character = random.choice(character)
                passw = passw + pass_character
            print("Votre mot de passe est: ", passw)

    elif special_character == "non":
        for i in range(0,pass_number):
            passw = ""
            for i in range(0,pass_length):
                pass_character = random.choice(character_without_symbols)
                passw = passw + pass_character
            print("Votre mot de passe est: ", passw)


    elif special_character != "oui"| "non":
        print("Error")