import random

print("La partie peut commencer")
#On crée le jeu de carte en indiquant les valeurs des cartes de l'as au roi, et leur catégorie, du coeur au trèfle
valeurs = ["As", "2", "3", "4", "5", "6", "7", "8", "9","10", "Valet", "Dame", "Roi"]
categories = ["♥", "♠", "♦", "♣"] 
deck=[] #On initie notre deck en créant une liste vide
for valeur in valeurs:#Pour toute valeur dans les valeurs possibles
    for categorie in categories:#Et pour toute catégorie dans les catégories possibles
        deck.append(f"{valeur}{categorie}")#On rajoute une carte au deck. Donc on ajoute une carte de chaque valeur par catégorie
random.shuffle(deck) #On mélange notre deck
defausse = [] #On initie notre défausse

joueur_actuel = 0 #Le joueur 0, donc le premier joueur, démarre la partie
main_joueurs = [] #On crée la liste qui contient les mains de chaque joueur

for joueur in range(3): #Pour 3 joueurs,
    main_joueur=[]#On crée une main individuelle au joueur
    for i in range (10):#Pour 10 cartes
        main_joueur.append(deck.pop()) #On ajoute la dernière carte de la pioche à la main du joueur
    main_joueurs.append(main_joueur)#On ajoute cette nouvelle main à la liste de mains de tous les joueurs
    print(f"La main du Joueur {joueur} contient {main_joueur})")#On montre ce que contient la main du joueur

while True:#Tant que les conditions sont remplies
    print(f"C'est le tour du Joueur {joueur_actuel}")
    if not deck: #Lorsque la pioche est épuisée, on récupère le contenu de la défausse pour créer une nouvelle pioche
        deck=defausse
        defausse=[] #La pioche redevient une liste vide
        random.shuffle(deck) #Puis on mélange la nouvelle pioche
    if defausse:#On affiche deux messages au début du tour, si la défausse contient des cartes
        print(f"Voici votre main: {main_joueurs[joueur_actuel]}")#On montre sa main au joueur
        action=input(f"Joueur {joueur_actuel}, que souhaitez-vous faire pour ce tour? La dernière carte de la défausse est: {defausse[-1]}")#On demande au joueur ce qu'il souhaite faire, en lui montrant la dernière carte de la défausse s'il souhaite la récupérer
    else:#Ou si la défausse est vide
        print(f"Voici votre main: {main_joueurs[joueur_actuel]}")
        action=input(f"Joueur {joueur_actuel}, que souhaitez-vous faire pour ce tour? La défausse est vide")#La défausse étant vide, on demande au joueur ce qu'il veut faire
    if action == "Piocher": #Si le joueur choisit de piocher
        if deck:#Et si la pioche contient des cartes
            main_joueurs[joueur_actuel].append(deck.pop()) #On ajoute la dernière carte de la pioche à la main du joueur
            print(f"Votre main contient désormais {main_joueurs[joueur_actuel]}")#Et on lui montre sa nouvelle main
        else:#Si la pioche est vide
            print("La pioche est vide, effectuez une autre action")

    elif action == "Récupérer":#Si le joueur choisit de récupérer la dernière carte de la défausse
        if defausse:#Et si la défausse n'est pas vide
            main_joueurs[joueur_actuel].append(defausse.pop())#On ajoute la dernière carte de la défausse à la main du joueur
            print(f"Votre main contient désormais {main_joueurs[joueur_actuel]}")#Et on lui montre sa nouvelle main
        else:#Si la défausse est vide
            print("La défausse est vide, choisissez une autre action")
    else:#Si le joueur ne choisit pas une action valide
        print("Action invalide, réessayez")
    carte_defaussee=(input("Choisissez la carte que vous souhaitez défausser"))#On oblige le joueur à défausser une carte quelle que soit l'action qu'il a effectuée
    if carte_defaussee in main_joueurs[joueur_actuel]:#On vérifie que la carte choisie est bien dans la main du joueur
        main_joueurs[joueur_actuel].remove(carte_defaussee)#Si oui, on retire la carte choisie de la main du joueur...
        defausse.append(carte_defaussee)#...puis on l'ajoute à la fin de la défausse
        print(f"Votre main contient désormais {main_joueurs[joueur_actuel]}")#On montre à nouveau sa main au joueur
    else:
        print("Vous ne possédez pas cette carte, réessayez")
    
    
    joueur_actuel += 1 #On change de joueur à la fin de la boucle. On ajoute 1 au numéro du joueur.
    if joueur_actuel > 2: #Si le numéro du joueur dépasse 2, donc si on dépasse les trois joueurs prévus,
        joueur_actuel = 0#On revient au tour du premier joueur
    
    categorie_carte = main_joueurs[joueur_actuel][0][:-2]#Une tentative de condition de victoire
    if all(carte[:-2] == categorie_carte for carte in main_joueurs[joueur_actuel]):
        print(f"La partie est terminée! le Joueur {joueur_actuel} a gagné!")
        break

print(main_joueurs) #On affiche les mains des joueurs à la fin de la partie