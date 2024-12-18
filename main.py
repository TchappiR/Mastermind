import random

general_color_list = ["noir", "rouge", "bleu", "vert", "jaune", "blanc"]
max_party_number = 10
party_counter = 1
player_color_list = []

#creation de la liste secrete à deviner par le joueur

secret_color_list = random.sample(general_color_list, 4)
print(secret_color_list)

# Fonction de création de la liste couleur du joueur
def create_player_list():  # sourcery skip: inline-immediately-returned-variable
    player_list = [input(f"Entrez la couleur {color_rang} : ").lower() for color_rang in range(1, 5)]
    return player_list

# Verification des couleurs du joueur
while party_counter < max_party_number and player_color_list != secret_color_list:
    
    correct_color_position = 0
    bad_color_position = 0
    
    player_color_list = create_player_list()
    
    print('_'*65,'\n')
    print(f"Votre proposition est : {player_color_list}")
    
    for index_player_color, player_color in enumerate(player_color_list):
        for index_secret_color, secret_color in enumerate(secret_color_list):
            if index_player_color == index_secret_color and player_color == secret_color:
                correct_color_position += 1
            elif index_player_color != index_secret_color and player_color == secret_color:
                bad_color_position += 1
    
    party_counter += 1
    print('_'*65,'\n')
    print(f"Vous avez :\n\t{correct_color_position} coleurs placées au bon endroit")
    if correct_color_position < 4:
        print(f"\t{bad_color_position} coleurs correctes mais placées au mauvais endroit.")
    print(f"\nEssai {party_counter} sur {max_party_number}. Il vous reste {max_party_number - party_counter} essais.\n")


if player_color_list == secret_color_list:
    print("Bravo vous avez trouvez la liste secrète...")

else :
    print("Vous avez perdu la partie...")