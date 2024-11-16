import random
deck = [
    'As de Coeur', '2 de Coeur', '3 de Coeur', '4 de Coeur', '5 de Coeur', '6 de Coeur', '7 de Coeur', '8 de Coeur', '9 de Coeur', '10 de Coeur', 'Valet de Coeur', 'Dame de Coeur', 'Roi de Coeur',
    'As de Carreau', '2 de Carreau', '3 de Carreau', '4 de Carreau', '5 de Carreau', '6 de Carreau', '7 de Carreau', '8 de Carreau', '9 de Carreau', '10 de Carreau', 'Valet de Carreau', 'Dame de Carreau', 'Roi de Carreau',
    'As de Trèfle', '2 de Trèfle', '3 de Trèfle', '4 de Trèfle', '5 de Trèfle', '6 de Trèfle', '7 de Trèfle', '8 de Trèfle', '9 de Trèfle', '10 de Trèfle', 'Valet de Trèfle', 'Dame de Trèfle', 'Roi de Trèfle',
    'As de Pique', '2 de Pique', '3 de Pique', '4 de Pique', '5 de Pique', '6 de Pique', '7 de Pique', '8 de Pique', '9 de Pique', '10 de Pique', 'Valet de Pique', 'Dame de Pique', 'Roi de Pique'
]    # Afficher la liste des cartes

main_joueur1 = [] # Je crée le joueur 1
main_joueur2 = [] # Je crée le joueur 2
main_joueur3 = [] # Je crée le joueur 3

random.shuffle(deck) # Je mélange le deck 

main_joueur1.extend(deck[:10]) # J'ajoute 10 cartes du deck au main du joueur 1
del deck[:10] #Je supprime ensuite les valeurs du deck

main_joueur2.extend(deck[:10]) # J'ajoute 10 cartes du deck au main du joueur 2
del deck[:10] #Je supprime ensuite les valeurs du deck

main_joueur3.extend(deck[:10]) # J'ajoute 10 cartes du deck au main du joueur 3
del deck[:10] #Je supprime ensuite les valeurs du deck

pile_defausse = [] #Je crée une pile de défausse 

while True:
#Je crée une liste contenant les valeurs que doivent avoir les joueurs pour gagner la partie
    v_coeur = ['As de Coeur', '2 de Coeur', '3 de Coeur', '4 de Coeur', '5 de Coeur', '6 de Coeur', '7 de Coeur', '8 de Coeur', '9 de Coeur', '10 de Coeur', 'Valet de Coeur', 'Dame de Coeur', 'Roi de Coeur']
    v_carreau = ['As de Carreau', '2 de Carreau', '3 de Carreau', '4 de Carreau', '5 de Carreau', '6 de Carreau', '7 de Carreau', '8 de Carreau', '9 de Carreau', '10 de Carreau', 'Valet de Carreau', 'Dame de Carreau', 'Roi de Carreau']
    v_trèfle = ['As de Trèfle', '2 de Trèfle', '3 de Trèfle', '4 de Trèfle', '5 de Trèfle', '6 de Trèfle', '7 de Trèfle', '8 de Trèfle', '9 de Trèfle', '10 de Trèfle', 'Valet de Trèfle', 'Dame de Trèfle', 'Roi de Trèfle']
    v_pique = ['As de Pique', '2 de Pique', '3 de Pique', '4 de Pique', '5 de Pique', '6 de Pique', '7 de Pique', '8 de Pique', '9 de Pique', '10 de Pique', 'Valet de Pique', 'Dame de Pique', 'Roi de Pique']

    
     # Tour du Joueur 1 
    print("\nMain_du_joueur 1:",main_joueur1) # J'affiche la main du joueur 1
    print("\nPile :",pile_defausse)# J'affiche la pile 
    
    choix = None 
    while choix not in [1, 2]: # Tant que le choix n'est ni 1, ni 2 
        try:
            choix = int(input("Tapez 1 pour piocher dans le deck, Tapez 2 pour piocher dans la pile: ")) # On demande au joueur de pioche r
        except ValueError:
            print("Veuillez entrer un nombre valide (1 ou 2).") # On affiche qu'il faut qu'il entre un nombre valide, soit 1, soit 2
    if choix == 1:
        if deck:  # Vérifier si le deck n'est pas vide
            valeur_a_ajouter = deck.pop(0)  # Piocher la première carte du deck
            main_joueur1.append(valeur_a_ajouter) # On ajoute cette carte à la main du joueur
            print("Vous avez pioché :",valeur_a_ajouter) # On affiche la carte pioché 
        else:
            print("Valeur non présente dans le deck") # On affiche que la valeur n'est pas présente dans le deck 

    elif choix == 2: # Si le joueur prend le choix 2
        if pile_defausse: # Si la pile n'est pas vide 
            valeur_piochee = pile_defausse[-1] # La valeur pioché est la dernière valeur de la pile
            main_joueur1.append(valeur_piochee) # Cette valeur est ajoutée à la main du joueur
            pile_defausse.pop(-1) # On supprime cette même valeur de la pile
            print("Vous avez pioché :", valeur_piochee) # On affiche la carte 
        else:
            print("La pile de défausse est vide. Vous êtes obligé de piocher dans le deck.") # On affiche que la pile de défausse est vide et que par conséquent, le joueur doit piocher dans le deck
            valeur_a_ajouter = deck.pop(0)  # Piocher la première carte du deck
            main_joueur1.append(valeur_a_ajouter) # On ajoute cette carte à la main du joueur
            print("Vous avez pioché :",valeur_a_ajouter) # On affiche la carte 

   
    valeur_a_enlever = input("Choisis la valeur à enlever") # On lui demande quelle valeur il choisit d'enlever et on stock cette leur 
    if valeur_a_enlever in main_joueur1: # Si la valeur est dans la main du joueur
        pile_defausse.append(valeur_a_enlever) # On ajoute cette valeur à la pile
        main_joueur1.remove(valeur_a_enlever) # On enlève cette valeur de la main du joueur 
    
    #Tour du Joueur 2

    print("\nMain_du_joueur 2 :", main_joueur2) # On affiche la main du joueur 1 
    print("\nPile :", pile_defausse) # On affiche la pile 
    
    choix = None
    while choix not in [1, 2]:
        try:
            choix = int(input("Tapez 1 pour piocher dans le deck, Tapez 2 pour piocher dans la pile: "))
        except ValueError:
            print("Veuillez entrer un nombre valide (1 ou 2).")
    if choix == 1: # Si le joueur choisit de piocher dans le deck 
        if deck: # Si le deck n'est pas vide
            valeur_a_ajouter = deck.pop(0) # La valeur à ajouter est la première valeur du deck 
            main_joueur2.append(valeur_a_ajouter) # On ajoute cette valeur à la main du joueur 
            print("Vous avez pioché :", valeur_a_ajouter) # On affiche la carte pioché 
        else:
            print("Valeur non présente dans le deck") # On affiche que la valeur n'est pas présente dans le deck 

    elif choix == 2: # Si le joueur choisit de piocher dans la pile 
        if pile_defausse: # Si la pile de défausse n'est pas vide 
            valeur_piochee = pile_defausse[-1] # La valeur piochée est la dernière valeur de la pile défausse 
            main_joueur2.append(valeur_piochee) # On ajoute cette valeur à la main du joueur
            pile_defausse.pop(-1) # On supprime cette valeur de la pile 
            print("Vous avez pioché :", valeur_piochee) # On affiche la valeur piochée
        else:
            print("La pile de défausse est vide. Vous êtes obligé de piocher dans le deck.")
            valeur_a_ajouter = deck.pop(0)  # Piocher la première carte du deck
            main_joueur2.append(valeur_a_ajouter) # On ajoute cette valeur à la main du joueur 
            print("Vous avez pioché :",valeur_a_ajouter) # On affiche la valeur piochée

    valeur_a_enlever = input("Choisis la valeur à enlever") # On demande la valeur à enlever au joueur 
    if valeur_a_enlever in main_joueur2: # Si la valeur à enlever est présente dans la main du joueur
        pile_defausse.append(valeur_a_enlever) # On ajoute cette valeur à la pile défausse
        main_joueur2.remove(valeur_a_enlever) # On enlève cette valeur de la main du joueur 

    #Tour du Joueur 3
    print("\nMain_du_joueur 3 :", main_joueur3) # On affiche la main du joueur 3
    print("\nPile :", pile_defausse) # On affiche la pile 
    
    choix = None
    while choix not in [1, 2]:
        try:
            choix = int(input("Tapez 1 pour piocher dans le deck, Tapez 2 pour piocher dans la pile: "))
        except ValueError:
            print("Veuillez entrer un nombre valide (1 ou 2).")

    if choix == 1: # Si le joueur choisit de piocher dans le deck
        if deck: # Si le deck n'est pas vide
            valeur_a_ajouter = deck.pop(0) # La valeur à ajouter est la première carte du deck 
            main_joueur3.append(valeur_a_ajouter) # On ajoute cette valeur à la main du joueur 
            print("Vous avez pioché :", valeur_a_ajouter) # On affiche la carte piochée
        else:
            print("Valeur non présente dans le deck") # On affiche que la valeur n'est pas présente dans le deck

    elif choix == 2: # Si le joueur choisit de piocher dans la pile
        if pile_defausse: # Si la pile n'est pas vide 
            valeur_piochee = pile_defausse[-1] # La valeur piochée est la dernière carte de la pile
            main_joueur3.append(valeur_piochee) # On ajoute cette valeur à la main du joueur 
            pile_defausse.pop(-1) # On supprime cette même valeur de la pile 
            print("Vous avez pioché :", valeur_piochee) # On affich ela valeur piochée 
        else:
            print("La pile de défausse est vide. Vous êtes obligé de piocher dans le deck.") # On affiche que la pile est vide et que le joueur doit donc piocher dans le deck
            valeur_a_ajouter = deck.pop(0)  # Piocher la première carte du deck
            main_joueur3.append(valeur_a_ajouter) # On ajoute la valeur à la main du joueur
            print("Vous avez pioché :",valeur_a_ajouter) # On affiche la valeur piochée

    valeur_a_enlever = input("Choisis la valeur à enlever") # On demande la carte que le joueur doit enleber
    if valeur_a_enlever in main_joueur3: # Si la catye est dans la main du joueur 
        pile_defausse.append(valeur_a_enlever) # On ajoute cette valeur à la pile defausse
        main_joueur3.remove(valeur_a_enlever) # On enlève cette valeur de la main du joueur 

    # Les conditions en question pour que le joueur 1 gagne la partie
    if all(carte in v_coeur for carte in main_joueur1):
        print("Le Joueur 1 gagne la partie car toutes les cartes sont de la famille Coeur.")
        break
    elif all(carte in v_carreau for carte in main_joueur1):
        print("Le Joueur 1 gagne la partie car toutes les cartes sont de la famille Carreau.")
        break
    elif all(carte in v_trèfle for carte in main_joueur1):
        print("Le Joueur 1 gagne la partie car toutes les cartes sont de la famille Trèfle.")
        break
    elif all(carte in v_pique for carte in main_joueur1):
        print("Le Joueur 1 gagne la partie car toutes les cartes sont de la famille Pique.")
        break


    # Les conditions en question pour que le joueur 2 gagne la partie
    if all(carte in v_coeur for carte in main_joueur2):
        print("Le Joueur 2 gagne la partie car toutes les cartes sont de la famille Coeur.")
        break
    elif all(carte in v_carreau for carte in main_joueur2):
        print("Le Joueur 2 gagne la partie car toutes les cartes sont de la famille Carreau.")
        break
    elif all(carte in v_trèfle for carte in main_joueur2):
        print("Le Joueur 2 gagne la partie car toutes les cartes sont de la famille Trèfle.")
        break
    elif all(carte in v_pique for carte in main_joueur2):
        print("Le Joueur 2 gagne la partie car toutes les cartes sont de la famille Pique.")

    # Les conditions en question pour que le joueur 3 gagne la partie
    if all(carte in v_coeur for carte in main_joueur3):
        print("Le Joueur 3 gagne la partie car toutes les cartes sont de la famille Coeur.")
        break
    elif all(carte in v_carreau for carte in main_joueur3):
        print("Le Joueur 3 gagne la partie car toutes les cartes sont de la famille Carreau.")
        break
    elif all(carte in v_trèfle for carte in main_joueur3):
        print("Le Joueur 3 gagne la partie car toutes les cartes sont de la famille Trèfle.")
        break
    elif all(carte in v_pique for carte in main_joueur3):
        print("Le Joueur 3 gagne la partie car toutes les cartes sont de la famille Pique.")
        break
