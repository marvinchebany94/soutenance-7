import sys
import os
current_path = sys.argv[0]
current_path = os.path.dirname(current_path)
current_path = os.path.dirname(current_path)
sys.path.append(current_path)


def input_verification():
    """
    La fonction va vérifier l'existence d'un parametre passé après le lancement de la commande dans l'invite de
    commandes. Pour qu'il n'y ait aucun problème il faut entrer le chemin du fichier entre " ".
    :return: tu n'as pas entré de fichier si aucun fichier n'a été entré, fichier introuvable si le path est incorrect
    puis retoune le chemin complet si celui-ci est correct.
    """
    try:
        sys.argv[1]
    except:
        return "Tu n'as pas entré de fichier"
        sys.exit()
    if os.path.exists(sys.argv[1]):
        return sys.argv[1]
    else:
        return "fichier introuvable"
        sys.exit()


