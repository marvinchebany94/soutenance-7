import os
import sys
current_path = sys.argv[0]
current_path = os.path.dirname(current_path)
current_path = os.path.dirname(current_path)
sys.path.append(current_path)
from contrôle.contrôle import input_verification
from modèle.modèle import dictionnaire, resultat_dict_ordre_decroissant, resultat_dict_ordre_croissant, \
    resultat_dict_benefice_par_ordre_decroissant


PATH = input_verification()
liste_de_resultats = [resultat_dict_ordre_decroissant, resultat_dict_ordre_croissant,
                      resultat_dict_benefice_par_ordre_decroissant]

def main():

    print("""
    ----------- Best Actions Choice 1.0 -----------
    """)

    print("le fichier est le suivant : {}".format(PATH))


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

