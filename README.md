 # Mastermind 

 # Description du Projet
Ce projet consiste à créer une version jouable du célèbre jeu de déduction Mastermind, fonctionnant dans un terminal. Le but du jeu est de deviner une combinaison secrète de couleurs ou de chiffres. Le projet comporte également une possibilité de bonus : implémenter une interface graphique utilisant Pygame pour une expérience utilisateur améliorée.

   # Règles du Jeu
But du jeu : Deviner une combinaison secrète générée aléatoirement par le programme.

   # Combinaison secrète :

Composée de 4 couleurs (ou chiffres) sélectionnées aléatoirement parmi 6 possibilités.
La combinaison peut contenir des doublons.
Tours et indices :

Le joueur dispose de 10 tentatives maximum pour deviner la combinaison.
Après chaque tentative, des indices sont donnés :
    (*) : Indique une couleur (ou chiffre) correcte et bien placée.
    (-) : Indique une couleur (ou chiffre) correcte mais mal placée.
    Aucun indice n’est donné pour les couleurs (ou chiffres) incorrects.

 # Conditions de victoire :

Le joueur gagne s’il devine la combinaison avant d’épuiser ses 10 essais.
Sinon, il perd et la combinaison secrète est révélée.