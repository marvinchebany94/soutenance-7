from collections import OrderedDict
import random
from itertools import combinations

LISTE_ACTIONS = []
combinaisons_deja_existantes = []
dict_actions = {}
COUT_PAR_ACTION = [20, 30, 50, 70, 60, 80, 22, 26,
                   48, 34, 42, 110, 38, 14, 18, 8, 4, 10, 24,
                   114]
BENEFICE = [5, 10, 15, 20, 17, 25, 7, 11, 13, 27, 17, 9, 23, 1,
            3, 8, 12, 14, 21, 18]
i = 0


def calcule_benefice(somme_depensee, pourcentage_benefice):
    resultat = somme_depensee * (pourcentage_benefice / 100)
    return resultat


while i != 20:
    i += 1
    action = {'action_' + str(i):[COUT_PAR_ACTION[i-1],BENEFICE[i-1]]}
    LISTE_ACTIONS.append(action)
    benefice_finale = calcule_benefice(COUT_PAR_ACTION[i-1], BENEFICE[i-1])
    dict_actions['action_' + str(i)] = {'cout' : COUT_PAR_ACTION[i-1], 'benefice' : BENEFICE[i-1],
                                        'benefice finale':benefice_finale}




def trier_selon_benefice_totale():
    i = 1
    liste_action_trie_ordre_croissant = []
    dict_trie = sorted(dict_actions.items(), key=lambda t: t[1]['benefice finale'], reverse=True)
    return dict(dict_trie)



def trier_selon_cout():
    i = 1
    liste_action_trie_ordre_croissant = []
    dict_trie = sorted(dict_actions.items(), key=lambda t:t[1]['cout'], reverse=True)
    return dict(dict_trie)

def trier_prix_ordre_croissant():
    liste_action_trie_ordre_croissant = []
    dict_trie = sorted(dict_actions.items(), key=lambda t: t[1]['cout'])
    return dict(dict_trie)


def verification_combinaison_doesnt_exists(dict):
    """
    La fonction va comparer le dictionnaire "dict" à tout ceux étant dans la liste "combinaison_deja_existantes.
    """
    if not combinaisons_deja_existantes:
        return True
    else:
        for dictionnaire in combinaisons_deja_existantes:
            if dict != dictionnaire:
                continue
            else:
                return False


def brute_force():
    argent = 500
    liste_actions = []
    actions_triees_benefice_croissant = trier_selon_cout()
    actions_cout = trier_selon_cout()
    print(actions_triees_benefice_croissant)
    i = 0
    while argent > 0:
        for action, value in actions_triees_benefice_croissant.items():
            cout = value['cout']
            benefice = value['benefice']
            benefice_finale = value['benefice finale']

            if cout <= argent:
                print("cout : ", cout, " benefice : ", benefice, " benefice finale : ", benefice_finale)
                liste_actions.append(benefice_finale)
                argent -= cout
                print("argent : ", argent)
                i += 1
            elif argent == 0:
                print("Tu n'as plus d'argent.")
                break
            else:
                benef_totale = sum(liste_actions)

        print("Tu n'as plus d'argent, lé bénéfice totale est de : {}".format(benef_totale))
        print("Nombre d'action = {}".format(i))
        break


def bruteforce_2():

    actions = []
    liste_actions = trier_selon_benefice_totale()
    argent = 500
    score_finale = 0
    while True:

        numero_action = random.randint(1, 20)
        action = "action_" + str(numero_action)

        if action not in actions:
            cout = liste_actions[action]['cout']
            benefice = liste_actions[action]['benefice']

            if cout <= argent:
                argent -= cout
                score_finale += benefice
                actions.append(action)
            elif argent == 0:

                return score_finale, actions
                break
            else:

                return score_finale, actions
                break
        else:
            continue



def peuimporte():
    resultat = []
    while True:
        resultat = sorted(resultat)
        if not resultat:
            benefice = bruteforce_2()
            resultat.append(benefice[0])
        else:
            benefice = bruteforce_2()
            if benefice[0] not in resultat and benefice[0] > resultat[-1]:
                resultat.append(benefice[0])
                print("bénéfice totale : ", resultat[-1])
                print("liste des actions : ")
                for action in benefice[1]:
                    print(action)
            else:
                continue

def calculer_nombres_de_possibilités():
    i = 0

    liste_combinaisons = []
    while True:
        x = bruteforce_2()[0]
        if liste_combinaisons == []:
            liste_combinaisons.append(x)
            i += 1
            print(i)

        else:
            if x in liste_combinaisons:
                print("dans la liste")
            elif x <= liste_combinaisons[-1]:
                print("plus petit ou egal")
            else:
                liste_combinaisons[-1] = x
                i += 1
                print(liste_combinaisons)
        print(i)





def trouver_le_maximum_actions_a_acheter():
    liste_combinaison = [4,1,2,3]
    liste = [2,3,1,4]
    i = 0
    if set(liste) == set(liste_combinaison):
        print("egal")
    else:
        print("pas egal")


brute_force()
x = 0
a = dict_actions

new_liste = [0]
benefice_totale = [0]
while x < len(a):
    x += 1
    liste_combinaisons = combinations(a, x)
    for combinaison in liste_combinaisons:
        prix_totale = 0
        for action in combinaison:
            cout = dict_actions[action]['cout']
            prix_totale += cout
        if prix_totale <= 500:
            benefice_action_actuelle = 0
            for action in combinaison:
                cout = dict_actions[action]['benefice finale']
                benefice_action_actuelle += cout
            if benefice_totale[-1] > benefice_action_actuelle:
                continue
            else:
                print(benefice_action_actuelle)
                benefice_totale[-1] = benefice_action_actuelle

                new_liste[0] = combinaison
        else:
            prix_totale = 0


print(new_liste)
print(benefice_totale)





"""
Dans un premier temps on va creer une liste qui contient les actions dans l'ordre du plus petit au plus grand cout afin
de voir combien d'actions maximum on va pouvoir acheter avec 500 euros
Une fois ce chiffre trouver on va pouvoir créer une boucle while i < chiffre trouver afin de creer toutes les 
combinaisons possibles et de voir la quelle est la meilleure.
"""

"""
cours sur le debugging
verifier l'existence d'un module pour faire des brutes force avec python
"""


"""
nombre d'actions minimum 7, maximum 16, on va donc faire un brute force pour creer toutes les combinaisons possibles
de 7 à 16 choix
"""
"""
faire en sorte que la fonction  qui calcule le nombre maximum de combinaisons retourne ce chiffre et que ce chiffre
soit utilisé dans une autre fonction afin de ne pas donner des chiffres qui sortent de notre tête
"""