import random

#Définition des familles et des valeurs des cartes
familles = ["❤","☘","♦️","♠️"]
valeurs = ["As","2","3","4","5","6","7","8","9","10","Valet","Dame","Roi"]

#Création du jeu de cartes
jeu_de_cartes = [(valeur,famille)for valeur in valeurs for famille in familles] 

#Mélanger le jeu de cartes
random.shuffle(jeu_de_cartes)

#Création d'une liste vide pour chaque joueur
joueur1 = []
joueur2 = []
joueur3 = []
joueurs = [joueur1, joueur2, joueur3] 

#Distribution du jeu de cartes aux joueurs
for i in range(10):
    for joueur in joueurs:
        distribution_joueurs = random.choice(jeu_de_cartes)
        joueur.append(distribution_joueurs)
        jeu_de_cartes.remove(distribution_joueurs)


#Début du jeu de cartes
defausse = []

#Définir la victoire par la famille de cartes
def la_meme_famille(main):
    familles_main = set([carte[1] for carte in main])
    return len(familles_main) == 1

#Définir quel joueur joue 
joueur_actuel = 0

# Affichage de la main de chaque joueur
for index, joueur in enumerate(joueurs, start=1):
    print(f"Main du joueur {index}: {joueur}")

#Boucle du jeu

while not la_meme_famille(joueurs[joueur_actuel]):
    joueur = joueurs[joueur_actuel]
    
    #Demande au joueur l'action qu'il veut faire
    debut_jeu = input(f"Joueur {joueur_actuel +1}, ecrivez 1 pour piocher une carte dans le deck ou 2 pour piocher une carte dans la defausse: ")
    
    #Création de la variable permettant au joueur de piocher une carte dans le deck
    if debut_jeu == "1":
        #Le joueur pioche une carte dans le deck
        distribution_joueurs = random.choice(jeu_de_cartes)
        joueur.append(distribution_joueurs)
        jeu_de_cartes.remove(distribution_joueurs)
        print(f"Voici votre nouvelle main : {joueur}")
        
        #Le joueur dépose une de ses cartes dans la défausse
        
        #Code pour déposer une carte de la main du joueur dans la défausse
        indice_carte_defausser = input(f"Joueur {joueur_actuel +1}, entrez l'indice de la carte à déposer (dans votre main actuelle) : ")

        if indice_carte_defausser.isdigit():
            indice_carte_defausser = int(indice_carte_defausser)
            if 0 <= indice_carte_defausser < len(joueur):
                carte_defaussee = joueur.pop(indice_carte_defausser)
                defausse.append(carte_defaussee)
                print(f"Carte déposée dans la défausse : {carte_defaussee}")
            else:
                print("Indice invalide.")
        else:
            print("Veuillez entrer un indice valide.")

 
    #Création de la variable permettant au joueur de piocher une carte dans la defausse
    elif debut_jeu == "2":
        #Le joueur pioche une carte dans la défausse
        if defausse:
        #Piocher la carte du dessus de la défausse
            carte_piochee = defausse.pop()
            joueur.append(carte_piochee)
            print(f"Voici votre nouvelle main : {joueur}")
        else:
            print("Il n'y a aucune carte dans la defausse")
            continue
        #Le joueur dépose une de ses cartes dans la défausse
        
        #Code pour déposer une carte de la main du joueur dans la défausse
        indice_carte_defausser = input(f"Joueur {joueur_actuel +1}, entrez l'indice de la carte à déposer (dans votre main actuelle) : ")

        if indice_carte_defausser.isdigit():
            indice_carte_defausser = int(indice_carte_defausser)
            if 0 <= indice_carte_defausser < len(joueur):
                carte_defaussee = joueur.pop(indice_carte_defausser)
                defausse.append(carte_defaussee)
                print(f"Carte déposée dans la défausse : {carte_defaussee}")
            else:
                print("Indice invalide.")
        else:
            print("Veuillez entrer un indice valide.")
    #Cas où le joueur s'est trompé
    else:
        print("Veuillez recommencer action impossible")
        
    #Affichage de la victoire du joueur
    if la_meme_famille(joueur):
        print(f"Le joueur {joueur_actuel + 1} a remporté la partie avec une main composée uniquement de la famille {joueur[0][1]} !")
        break
    #Changement de joueur actuel
    joueur_actuel = (joueur_actuel + 1) % len(joueurs)

