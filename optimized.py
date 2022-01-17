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


def trier_prix_ordre_decroissant(dictionnaire):
    """
    La fonction va trier le dictionnaire selon les prix par ordre decroissant
    :param dictionnaire: un dictionnaire contenant une clé ainsi que les valeurs 'cout' et 'benefice finale'
    :return: le dictionnaire rangé par ordre décroissant
    """
    i = 1
    dict_trie = sorted(dictionnaire.items(), key=lambda t: t[1]['cout'], reverse=True)
    return dict(dict_trie)


def trier_prix_ordre_croissant(dictionnaire):
    """
    La fonction va trier le dictionnaire selon les prix par ordre croissant.
    :param dictionnaire: un dictionnaire contenant les clés ainsi que les valeurs 'cout' et 'benefice finale'
    :return: le dictionnaire rangé par ordre croissant
    """
    dict_trie = sorted(dictionnaire.items(), key=lambda t: t[1]['cout'])
    return dict(dict_trie)


def trier_selon_benefice_maximal_par_ordre_decroissant(dictionnaire):
    """
    La fonction va trier le dictionnaire selon le bénéfice maximale de chaque actions par ordre decroissant.
    :param dictionnaire: un dictionnaire contenant les clés ainsi que les valeurs 'cout' et 'benefice finale'
    :return: un dictionnaire trié par ordre decroissant selon le bénéfice totale
    """
    dict_trie = sorted(dictionnaire.items(), key=lambda t: t[1]['benefice finale'], reverse=True)
    return dict(dict_trie)


def algo_optimised(dictionnaire):
    """
    Cette fonction va prendre en param un dictionnaire qui doit avoir des clés portant le nom de chaque actions
    puis comme valeurs 'cout' et 'benefice finale'
    La fonction va acheter les actions dans l'ordre d'apparition dans la liste tout en verifiant que le cout n'est pas
    plus elevé que 500 euros, puis pour chaque action elle va soustraire le cout à l'argent qu'il nous reste, puis
    additioner son benefice finale à la variable "benefice_finale"
    Une fois que l'argent ne suffit plus pour acheter l'action suivante, la fonction nous retourne le benefice finale,
    la somme depensée et la liste des actions achetées.
    :param dictionnaire: dictionnaire ayant comme clé le nom des actions et comme valeurs 'cout' et 'benefice finale'
    :return: le benefice finale, la somme depensée, liste des actions achetées et le temps d'execution
    """

    start = time.time()
    liste_actions_du_dictionnaire = []
    for action in dictionnaire:
        liste_actions_du_dictionnaire.append(action)

    liste_actions = []
    argent = 500
    somme_depensee = 0
    benefice_finale = 0
    i = 0
    while True:

        action = liste_actions_du_dictionnaire[i]
        cout = dictionnaire[action]['cout']
        benefice = dictionnaire[action]['benefice finale']
        if cout <= argent:
            argent -= cout
            somme_depensee += cout
            liste_actions.append(action)
            benefice_finale += benefice
            i += 1

        else:
            end = time.time()
            temps_d_execution = end - start
            return benefice_finale, somme_depensee, liste_actions, temps_d_execution


fichier = input_verification()
dictionnaire = creation_dictionnaire(fichier)

dictionnaire_trier_par_ordre_decroissant = trier_prix_ordre_decroissant(dictionnaire)
dictionnaire_trier_par_ordre_croissant = trier_prix_ordre_croissant(dictionnaire)
dictionnaire_trier_benef_maximale_ordre_decroissant = trier_selon_benefice_maximal_par_ordre_decroissant(dictionnaire)

resultat_dict_ordre_decroissant = algo_optimised(dictionnaire_trier_par_ordre_decroissant)
resultat_dict_ordre_croissant = algo_optimised(dictionnaire_trier_par_ordre_croissant)
resultat_dict_benefice_par_ordre_decroissant = algo_optimised(dictionnaire_trier_benef_maximale_ordre_decroissant)

liste_de_resultats = [resultat_dict_ordre_decroissant, resultat_dict_ordre_croissant,
                      resultat_dict_benefice_par_ordre_decroissant]



print("""
----------- Best Actions Choice 1.0 -----------
""")

print("le fichier est le suivant : {}".format(fichier))

i = 0
liste_mode_de_triage = ['triées selon le prix par ordre decroissant', 'triées selon le prix par ordre croissant',
                        'triées selon le benefice par ordre decroissant']
for resultat in liste_de_resultats:
    print("""



    Les résultats de l'algorithme ont été fait sur le dictionnaire contenant la liste des actions {}


        LA LISTE DES ACTIONS : {}
        LA SOMME TOTALE DEPENSEE : {}
        TEMPS D EXECUTION DE L ALGORITHME : {}

        LE BENEFICE TOTALE : {}




    """.format(liste_mode_de_triage[i], resultat[2], resultat[1], resultat[3], resultat[0]))
    i += 1