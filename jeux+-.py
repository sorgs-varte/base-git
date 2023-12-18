import random

menu_value = True


def jeu_plus_moins(nombre_max_tentative=10):
    print("Bienvenue dans le jeu +/- !")
    print("Je vais choisir un nombre entre 1 et 100, et vous devez deviner ce nombre.")

    # Choisir un nombre aléatoire entre 1 et 100
    nombre_a_deviner = random.randint(1, 100)
    tentative = 0

    continuer = True

    while continuer :
        tentative += 1
        try:
            devinette = int(input("Entrez votre devinette : "))
        except ValueError:
            print("Erreur : Veuillez entrer un nombre entier.")
            continue
        

        # Vérifier la devinette du joueur
        if devinette < nombre_a_deviner:
            print("Plus grand !")
        elif devinette > nombre_a_deviner:
            print("Plus petit !")
        else:
            print(f"Félicitations ! Vous avez deviné le nombre en {tentative} tentatives.")
            continuer = False

        if tentative == nombre_max_tentative:
            print(f"Dommage ! Vous n'avez pas réussi à deviner le nombre en {nombre_max_tentative} tentatives. Le nombre était {nombre_a_deviner}.")
            continuer = False


while menu_value:
        print("Menu :")
        print("1. Nouvelle partie")
        print("2. Quitter")
        choix_menu = input("Entrez le numéro de votre choix : ")

        if choix_menu == "1":
            jeu_plus_moins()
        elif choix_menu == "2":
            print("Au revoir !")
            menu_value = False
        else:
            print("Choix invalide. Veuillez entrer 1 pour une nouvelle partie ou 2 pour quitter.")
