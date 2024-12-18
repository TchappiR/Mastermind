import random

general_color_list = ["noir", "rouge", "bleu", "vert", "jaune", "blanc"]
max_party_number = 10
party_counter = 0

#creation de la liste secrete à deviner par le joueur

secret_color_list = random.sample(general_color_list, 4)
print(secret_color_list)

# Liste du joueur

player_color_list = [input(f"Entrez la coleur{color_rang} : ").lower() for color_rang in range(1, 5)]

print('_'*65,'\n')
print(f"Votre proposition est : {player_color_list}")

# Verification des couleurs du joueur

correct_color_position = 0
bad_color_position = 0

for index_player_color, player_color in enumerate(player_color_list):
    for index_secret_color, secret_color in enumerate(secret_color_list):
        if index_player_color == index_secret_color and player_color == secret_color:
            correct_color_position += 1
        elif index_player_color != index_secret_color and player_color == secret_color:
            bad_color_position += 1

print('_'*65,'\n')
print(f"Vous avez :\n\t{correct_color_position} coleurs placées au bon endroit\n\t{bad_color_position} coleurs correctes mais placées au mauvais endroit.")