import random

# Définition des valeurs et des enseignes
valeurs = ['As', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Valet', 'Dame', 'Roi']
familles = ['Pique', 'Coeur', 'Carreau', 'Trèfle']

# Création du deck de cartes
deck = [(v, f) for v in valeurs for f in familles]

# Initialisation d'une pile vide
pile = []

# Création d'une main pour chaque joueur (3 joueurs)
mains = [random.sample(deck, 10) for _ in range(3)]

# Afficher la main initiale pour chaque joueur
def afficher_main(main, joueur):
    print(f"Main du Joueur {joueur + 1}:")
    for i, carte in enumerate(main, start=1):
        print(f"{i}. {carte[0]} de {carte[1]}")

for i, main in enumerate(mains):
    afficher_main(main, i)

# Fonction pour proposer une carte aléatoire
def proposer_carte(main, source):
    if source == "deck":
        carte_proposee = random.choice(deck)
    else:
        if not pile:
            print("La pile est vide.")
            return None
        carte_proposee = pile.pop()
    print(f"La carte proposée est : {carte_proposee[0]} de {carte_proposee[1]}")
    choix = input("Voulez-vous garder cette carte ? (oui/non): ").lower()
    if choix == "oui":
        return carte_proposee
    else:
        pile.append(carte_proposee)  # Placer la carte dans la pile
        return None

# Continuer le jeu jusqu'à ce qu'un joueur ait toutes ses cartes de la même famille
joueur_actuel = 0
while True:
    if all(carte[1] == mains[joueur_actuel][0][1] for carte in mains[joueur_actuel]):
        print(f"Le Joueur {joueur_actuel + 1} a toutes ses cartes de la famille {mains[joueur_actuel][0][1]} ! Il a gagné !")
        break

    choix_source = input(f"Joueur {joueur_actuel + 1}, voulez-vous piocher dans le 'Deck' ou la 'Pile'? ").lower()
    if choix_source not in ['deck', 'pile']:
        print("Choix invalide. Veuillez choisir entre 'Deck' et 'Pile'.")
        continue

    choix = input(f"Joueur {joueur_actuel + 1}, voulez-vous une nouvelle carte ? (oui/non): ").lower()

    if choix == "oui":
        carte = proposer_carte(mains[joueur_actuel], choix_source)
        if carte:
            choix_carte = int(input(f"Entrez le numéro de la carte que vous souhaitez remplacer (1-10): ")) - 1
            if 0 <= choix_carte < len(mains[joueur_actuel]):
                mains[joueur_actuel][choix_carte] = carte
                afficher_main(mains[joueur_actuel], joueur_actuel)
            else:
                print("Veuillez entrer un numéro de carte valide.")
        else:
            print("Vous avez choisi de ne pas remplacer de carte.")
    else:
        print("Vous avez choisi de ne pas garder la carte.")
        carte = proposer_carte(mains[joueur_actuel], choix_source)
        if carte:
            pile.append(carte)
        afficher_main(mains[joueur_actuel], joueur_actuel) # Fin du tour du joueur

    joueur_actuel = (joueur_actuel + 1) % 3 # Changement de joueur