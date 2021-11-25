from collections import OrderedDict


LISTE_ACTIONS = []
combinaisons_deja_existantes = []
dict_actions = {}
COUT_PAR_ACTION = [20, 30, 50, 70, 60, 80, 22, 26,
                   48, 34, 42, 110, 38, 14, 18, 8, 4, 10, 24,
                   114]
BENEFICE = [5, 10, 15, 20, 17, 25, 7, 11, 13, 27, 17, 9, 23, 1,
            3, 8, 12, 14, 21, 18]
i = 0

while i != 20:
    i += 1
    action = {'action_' + str(i):[COUT_PAR_ACTION[i-1],BENEFICE[i-1]]}
    LISTE_ACTIONS.append(action)
    dict_actions['action_' + str(i)] = {'cout' : COUT_PAR_ACTION[i-1], 'benefice' : BENEFICE[i-1]}



def trier_selon_cout():
    i = 1
    liste_action_trie_ordre_croissant = []
    dict_trie = sorted(dict_actions.items(), key=lambda t:t[1]['cout'], reverse=True)
    return dict(dict_trie)

def bruteforce():
    """
    La fonction doit creer des combinaisons qui vont vérifier que la somme ne depasse pas
    les 500e, et que la combinaison ne se trouve pas dans la liste des combinaisons deja créées
    """

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

d = {'marvin':10, 'ryu':20}
d2 = {'ryu':20, 'marvin':10}
Combinaisons_deja_existantes.append(d)
Combinaisons_deja_existantes.append(d2)
print(d)
print("\n")
print(d2)

if Combinaisons_deja_existantes[0] == Combinaisons_deja_existantes[1]:
    print("yes")
else:
    print('no')



