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

#     Étapes pour Exécuter le Jeu
        Mode Terminal

        Clonez ce dépôt sur votre machine locale :
1-Copier le code
    .git clone <url_du_dépôt>
2-Naviguez dans le répertoire du projet :
    .cd mastermind-python
3-Lancez le fichier Python principal :
    .python mastermind.py

   # Organisation du Code

Le projet est structuré en étapes modulaires pour faciliter le développement et la maintenance :

1-Initialisation du jeu :
    .Génération aléatoire de la combinaison secrète.
    .Définition des constantes du jeu (longueur de la combinaison, nombre d’essais, valeurs autorisées).

2-Interaction avec le joueur :
    .Saisie sécurisée et validation de la proposition.

3-Vérification des combinaisons :
    .Calcul des indices * et -.
    .Gestion des doublons.

4-Boucle principale :
    .Gestion des tours.
    .Affichage des résultats intermédiaires.
    .Détection de la victoire ou de la défaite.

5-Interface graphique (optionnelle) :
    .Création d’une fenêtre avec Pygame.
    .Affichage des tentatives et des indices.

  #  LICENCE
Ce projet est sous licence libre (par exemple, MIT). Vous êtes libre de l’utiliser, le modifier et le redistribuer.
