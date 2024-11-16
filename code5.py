import random

# création  du deck
""" jeu de carte en python """
deck = ["As de coeur", "2 de coeur", "3 de coeur", "4 de coeur", "5 de coeur", "6 de coeur", "7 de coeur", "8 de coeur", "9 de coeur", "10 de coeur", "valet de coeur", "dame de coeur", "roi de coeur",
        "As de pique", "2 de pique", "3 de pique", "4 de pique","5 de pique", "6 de pique", "7 de pique", "8 de pique", "9 de pique", "10 de pique", "valet de pique", "dame de pique", "roi de pique",
        "As de trefle", "2 de trefle", "3 de trefle", "4 de trefle", "5 de trefle", "6 de trefle", "7 de trefle", "8 de trefle", "9 de trefle", "10 de trefle", "valet de trefle", "dame de trefle", "roi de trefle",
        "As de carreau", "2 de carreau", "3 de carreau", "4 de carreau", "5 de carreau", "6 de carreau", "7 de carreau", "8 de carreau", "9 de carreau", "10 de carreau", "valet de carreau", "dame de carreau", "roi de carreau"]
random.shuffle(deck)
# fin création  du deck




# création des variables pour détecter la potentielle victoire
coeur = 0
pique = 0
trefle = 0
carreau = 0


  # création des 3 mains
main_joueur1 = []
main_joueur2 = []
main_joueur3 = []

main_joueurs = [main_joueur1, main_joueur2, main_joueur3]
for i in range (10):
    main_joueur1.append(deck.pop())
for i in range (10):
    main_joueur2.append(deck.pop())
for i in range (10):
    main_joueur3.append(deck.pop())
print(main_joueur1)
print(main_joueur2)
print(main_joueur3)
# création pile défausse
defausse = []
joueur_actuelle = 0

# création de la boucle du jeu
while True:

  
    # compte le nombre de symbole dans la main du joueur
    for carte in main_joueurs[joueur_actuelle]:
        if "coeur" in carte:
            coeur += 1
        elif "pique" in carte:
            pique += 1
        elif "trefle" in carte:
            trefle += 1
        else:
            carreau += 1       




    # mélange la defausse et la vide à la place de la pioche quand cette dernière est vide
    if deck == []:
        random.shuffle(defausse)
        while defausse != []:
            deck.append(defausse.pop())


    # choix entre pile et défausse et récupération de la carte
    print(f"Au tour du joueur numéro joueurs {joueur_actuelle + 1} de jouer")
    choix = int(input("Entrez 1 pour la défausse sinon le choix se fera obligatoirement dans la pioche"))
    if choix == 1 and defausse != []:
        main_joueurs[joueur_actuelle].append(defausse.pop(-1))
        print(main_joueurs[joueur_actuelle])
    else: 
        main_joueurs[joueur_actuelle].append(deck.pop())
        print(main_joueurs[joueur_actuelle])

    # création de la variable indiquant le joueur qui doit jouer à ce tour
    joueur_actuelle += 1
    if joueur_actuelle == 3:
        joueur_actuelle = 0
    


    # ajout de la carte en trop dans la défausse
    place = int(input("Entrer un chiffre de 0 à 10 indiquant la place de la carte dont vous voulez vous séparer"))
    try :
        defausse.append(main_joueurs[joueur_actuelle].pop(place))
    except IndexError:
        print("Liste Vide")
    # on retire le carte qui part à la défausse du compte des cartes
    for carte in main_joueurs[joueur_actuelle]:
        if "coeur" in carte:
            coeur -= 1
        elif "pique" in carte:
            pique -= 1
        elif "trefle" in carte:
            trefle -= 1
        else:
            carreau -= 1

    # détecte s'il y a une victoire ou non
    if coeur == 10 or pique == 10 or trefle == 10 or carreau == 10:
        print("You won")




