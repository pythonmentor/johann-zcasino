
from random import randint
# Le joueur mise sur un numéro compris entre 0 et 49
# il y dépose la somme qu'il souhaite miser.
# Si le numéro gagnant est celui sur lequel le joueur a misé (probabilité de 1/50, plutôt faible), le croupier lui remet 3 fois la somme misée.
# Sinon, le croupier regarde si le numéro misé par le joueur est de la même couleur que le numéro gagnant (s'ils sont tous les deux pairs ou tous les deux impairs). Si c'est le cas, le croupier lui remet 50 % de la somme misée. Si ce n'est pas le cas, le joueur perd sa mise.

#-tc- Pas de self si on n'est pas dans une classe
# -tc- Techniquement, la fonction est un peu longue. Si une fonction fait plus de 20 lignes,
# -tc- essaie de factoriser le code
def roulette(self):
    sold = 5000
    # -tc- Que se passe-t-il si l'utilisateur entre du texte ou un nombre négatoire ou encore
    # -tc- un nomnbre supérieur à 49?
    choice_player = int(input("Veuillez choisir un numero entre 0 et 49\n"))
    # -tc- Si l'utilisateur entre du texte, tu aura une exception
    mise_player = int(input("Veuillez saisir une mise\n"))

    # creer une roulette qui choisit aleatoirement entre 0 et 49
    roulette = randint(0, 49)
    # pour montrer le choix de la roulette
    print("votre Choix :\n", choice_player, " \nChoix de la roulette :\n", roulette)
    # verifier si choix player = choix roulette et si ok gagné et rajouté 3 fois la mise
    # -tc- C'est choice_player qui doit être égal à roulette
    if mise_player == roulette:
        gain = mise_player * 3
        sold = sold + gain
        print("You Win !!")
        print("Vous avez gagné", gain, " € et votre solde est de ")

    # sinon si pair ou impair (rouge ou noir) ajouter la moitié de la mise
    elif (choice_player % 2 == 0 and roulette % 2 == 0) or (choice_player % 3 == 0 and roulette % 3 == 0):
        # -tc- pourquoi ne pas simplement réutiliser la variable gain?
        gain2 = mise_player / 2
        sold = sold + gain2
        print("Vous avez gagné 50% de votre mise, soit : ", mise_player / 2)
        print("Votre solde actuelle est de ", sold + gain2)


    #si pas bon perdu
    else:
        sold = sold - mise_player
        print("Vous avez perdu")
        # afficher solde avec gain de la mise
        print("Votre solde actuelle est de ", sold - mise_player,"euros")



# -tc- mettre également le code principal dans une fonction, généralement appelée main()
continuer = True
while continuer:
    roulette(roulette)
    continuer = input("Voulez vous recommencez une partie, oui ou non..?").lower() in ("o", "oui")


