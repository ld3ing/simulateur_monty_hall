import random
print("Bienvenue dans le simulateur qui te permettra d'experimenter le paradoxe de Monty Hall ! ")

DEBUG = False
nb_gagne=0
nb_perdu=0
continue_game = True
automatique = False
nb_parties_automatiques = 0
strategie = False

#On propose au joueur de jouer eu mode automatique
choix_automatique = input("Veux-tu jouer en mode automatique ? (oui/non) : ").lower()
if choix_automatique in ["oui", "o"]:
    automatique = True
    #On demande combien de parties automatiques il veut jouer
    while nb_parties_automatiques <= 0:
        try:
            nb_parties_automatiques = int(input("Combien de parties automatiques veux-tu jouer ? : "))
            if nb_parties_automatiques <= 0:
                print("Choix invalide. Veuillez entrer un nombre positif.")
        except ValueError:
            print("Veuillez entrer un nombre valide.")
    #On propose au joueur de changer de porte à chaque fois
    reponse_strategie = input("Veux-tu changer de porte à chaque fois ? (oui/non) : ").lower()
    if reponse_strategie in ["oui", "o"]:
        strategie = True

while continue_game:
    #on défini ou se trouve la voiture
    tableau = [False, False, False]
    tableau[random.randint(0, 2)] = True
    if DEBUG:
        print(tableau)

    #On demande à l'utilisateur de choisir une porte
    choix = 5
    if automatique == True:
            choix = random.randint(1, 3)
    else:
        while choix < 1 or choix > 3:
            choix = int(input("Choisis une porte (1, 2 ou 3) : "))
            if choix < 1 or choix > 3:
                if not automatique:
                    print("Choix invalide. Veuillez choisir une porte entre 1 et 3.")

    #On lui montre une porte qui ne contient pas la voiture et qui n'est pas celle qu'il a choisie
    porte_revelee = 0
    for i in range(3):
        if not tableau[i] and i != choix - 1:
            if not automatique:
                print("La voiture n'est pas derrière la porte", i + 1)
            porte_revelee = i + 1
            break

    #On lui demande s'il veut changer de porte
    changement = ""
    if automatique and strategie:
        changement = "oui"
    elif automatique and not strategie:
        changement = "non"
    else:
        changement = input("Veux-tu changer de porte ? (oui/non) : ").lower()
    if changement in ["oui", "o"]:
        #On change de porte
        for i in range(3):
            if i != choix - 1 and i != porte_revelee - 1:
                choix = i + 1
                if not automatique:
                    print("Tu as changé de porte. Tu as maintenant choisi la porte", choix)
                break

    #On vérifie si l'utilisateur a gagné ou perdu
    if tableau[choix - 1]:
        if not automatique:
            print("Félicitations ! Tu as gagné la voiture !")
        nb_gagne += 1
    else:
        if not automatique:
            print("Désolé, tu as perdu. La voiture était derrière la porte", tableau.index(True) + 1)
        nb_perdu += 1

    #On lui affiche la statistique de ses parties
    print("Statistiques :", nb_gagne,"/",nb_gagne + nb_perdu, "gagné(s) soit ", round(nb_gagne / (nb_gagne + nb_perdu) * 100, 2), "% de victoires." )

    #On lui demande s'il veut continuer à jouer
    if automatique and nb_parties_automatiques > 0:
        nb_parties_automatiques -= 1
        if nb_parties_automatiques == 0:
            continue_game = False
            print("Merci d'avoir joué ! À bientôt !")
    else:
        reponse_continue = input("Veux-tu continuer à jouer ? (oui/non) : ").lower()
        if reponse_continue not in ["oui", "o"]:
            continue_game = False
            print("Merci d'avoir joué ! À bientôt !")