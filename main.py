import random

general_color_list = ["noir", "rouge", "bleu", "vert", "jaune", "blanc"]
max_party_number = 10
party_counter = 1
player_color_list = [] 
    

#Fonction de creation de la liste secrete à deviner par le joueur
def generate_secret_list():
    return random.sample(general_color_list, 4)
#print(secret_color_list)

# Fonction de création de la liste couleur du joueur
def create_player_list():  
    return [
        input(f"Entrez la couleur {color_rang} : ").lower().replace(" ", "")
        for color_rang in range(1, 5)
        
    ]


# Creation de la partie
secret_color_list = generate_secret_list()

while party_counter < max_party_number and player_color_list != secret_color_list:
    
    correct_color_position = 0
    bad_color_position = 0
    
    print(f"\nEssai {party_counter} sur {max_party_number}. Il vous reste {max_party_number - party_counter} essais.\n")

    player_color_list = create_player_list()
    
    print(f"Votre proposition est : {player_color_list}")
    
    for index_player_color, player_color in enumerate(player_color_list):
        for index_secret_color, secret_color in enumerate(secret_color_list):
            if index_player_color == index_secret_color and player_color == secret_color:
                correct_color_position += 1
                break
            elif index_player_color != index_secret_color and player_color == secret_color:
                bad_color_position += 1
    
    party_counter += 1
    
    print(f"Vous avez :\n\t* {correct_color_position}")
    if correct_color_position < 4:
        print(f"\t- {bad_color_position}")
    print('_'*65,'\n')

if player_color_list == secret_color_list:
    print("Bravo vous avez trouvé la liste secrète.....")
else :
    print("Vous avez perdu la partie...\nLa combinaison secrète etait {secret_color_list}")