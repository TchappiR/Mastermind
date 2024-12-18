# Mastermind
jeu de reflexion

  #                        Conway's Game of Life

# Description
Le Jeu de la Vie est un automate cellulaire inventé par John Horton Conway. Ce projet consiste à implémenter une simulation du Jeu de la Vie en Python. Le jeu simule l'évolution de cellules sur une grille selon des règles mathématiques simples.

# Objectif
L'objectif de ce projet est de coder un algorithme qui simule le comportement du Jeu de la Vie en suivant les règles définies.
Pour une meilleure compréhension, vous pouvez consulter cette vidéo : Qu'est-ce que le Jeu de la Vie ?.

# Règles
Une cellule peut être vivante (1) ou morte (0).
Chaque cellule possède 8 voisins adjacents (horizontalement, verticalement et diagonalement).
À chaque itération :
Une cellule morte avec exactement 3 voisins vivants devient vivante.
Une cellule vivante reste vivante si elle a 2 ou 3 voisins vivants, sinon elle meurt.

# Instructions
Pré-requis
Pour exécuter ce projet, vous aurez besoin de :

   . Python 3.x
   . Un environnement virtuel Python avec la bibliothèque NumPy installée.

# Étapes de Mise en Place
Créer un répertoire de projet:  Placez-y un fichier nommé main.py.
Installer NumPy :  pip install numpy

# Initialiser la grille :
Le jeu démarre avec une grille 7x7. Les cellules vivantes sont représentées par 1 et les cellules mortes par 0.
Gestion des bords de la grille
Pour résoudre le problème des cellules en bordure (qui n'ont pas 8 voisins), une technique appelée Zero Padding est utilisée. Elle consiste à entourer la grille d'une bordure de cellules mortes (0) pour simplifier les calculs.

# Fonctionnalités du Projet
    .Implémentation d'une grille 7x7.
    .Application des règles du Jeu de la Vie pour chaque cellule.
    .Utilisation du Zero Padding pour gérer les bordures.


# Ressources
Jeu de la Vie (Wikipédia)
Vidéo explicative
