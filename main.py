import random

general_color_list = ["noir", "rouge", "bleu", "vert", "jaune", "blanc"]

#creation de la liste secrete à deviner par le joueur

secret_color_list = random.sample(general_color_list, 4)
print(secret_color_list)