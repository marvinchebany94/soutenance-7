import os
import sys
import time
from itertools import combinations

current_path = sys.argv[0]
current_path = os.path.dirname(current_path)
current_path = os.path.dirname(current_path)
sys.path.append(current_path)
from contrôle.contrôle import input_verification


def creation_dictionnaire(fichier):
    """
    Cette fonction va nous permettre de créer une dictionnaire contenant toutes les actions présentes dans un fichier
    en prenant le nom de l'action, son prix et le bénéfice qu'on en tire.
    Elle vérifie aussi l'existence d'actions qui n'auraient pas de prix.
    :param fichier: La fonction a besoin d'un chemin menant à un fichier csv muni de 3 colonnes (name, price
    et benefice). Les noms sont facultatifs mais les 3 colonnes doivent donner ces infos et dans le bon ordre
    :return: Un dictionnaire contenant les actions avec comme clé le nom de l'action, et comme valeurs le prix et
    le bénéfice.
    """
    dictionnaire = {}
    with open(fichier) as f:
        first_ligne = 0
        for line in f:

            line = line.split(',')

            if line[1] == 'price' or line[0] == "p":
                continue
            else:

                name = line[0]

                try:
                    price = float(line[1])
                except:
                    price = int(line[1])
                if price == 0.0 or price < 0:
                    continue
                else:
                    try:
                        profit = float(line[2])
                    except:
                        profit = int(line[2])
                    dictionnaire[name] = {'cout': price, 'benefice finale': profit}
    return dictionnaire


def brute_force_non_optimise(dictionnaire):
    """
    Cette fonction va faire tourner une boucle while tant que x est plus petit que la longueur de la liste. Pour chaque
    nombre allant de 0 à la longueur maximale de la liste, elle va créer une liste de toutes les combinaisons possibles.
    si le cout de la combinaison est au dessus de 500e elle continue, sinon elle regarde la valeur de benefice_totale
    et si celle-ci est plus petite que la valeur trouvée, elle sera remplacée, à l'inverse l'algorithme continuera de
    tourner.
    Sur une petite liste c'est très efficace car on est sur d'avoir le meilleur rendement, mais sur une longue liste
    cette fonction ne marchera pas.
    :param dictionnaire: un dictionnaire ayant comme clé le nom des actions et comme valeurs 'cout' et
    'benefice finale'
    :return:
    """
    nombre_d_actions = len(dictionnaire)
    x = 0
    new_liste = [0]
    benefice_totale = [0]
    start = time.time()
    while x < nombre_d_actions:
        x += 1
        liste_combinaisons = combinations(dictionnaire, x)
        for combinaison in liste_combinaisons:
            prix_totale = 0
            for action in combinaison:
                cout = dictionnaire[action]['cout']
                prix_totale += cout
            if prix_totale <= 500:
                benefice_action_actuelle = 0
                for action in combinaison:
                    cout = dictionnaire[action]['benefice finale']
                    benefice_action_actuelle += cout
                if benefice_totale[-1] > benefice_action_actuelle:
                    continue
                else:
                    benefice_totale[-1] = benefice_action_actuelle

                    new_liste[0] = combinaison
            else:
                prix_totale = 0
    end = time.time()
    return new_liste, benefice_totale[0], end-start

fichier = input_verification()
dictionnaire = creation_dictionnaire(fichier)
resultats = brute_force_non_optimise(dictionnaire)

print("""
    ----------- Best Actions Choice 1.0 -----------
    """)

print("le fichier est le suivant : {}".format(fichier))

print("""
LA LISTE DES ACTIONS : {}
         TEMPS D EXECUTION DE L ALGORITHME : {}
         
         LE BENEFICE TOTALE : {}

""".format(resultats[0], resultats[2], resultats[1]))


