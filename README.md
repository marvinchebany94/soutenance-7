# soutenance-7
Pour ce projet là il fallait créer un script en python qui allait d'une part être un brut force brute, donc pas du tout optimisé qui allait tester toutes les combinaisons possibles,
puis d'autre part créer un script python avec un algorithme optimisé qui allait sortir le meilleur résultat dans un temps record.

Pour lancer le programme :
-lancer cmd
-se rendre dans le dossier en entrant : cd chemin_du_fichier
- python -m venv env
- cd env/Scripts
- activate ou activate.bat
- cd .. 
- cd ..
- python pip install -r requirements.txt (pour installer tous les modules nécéssaires au lancement du script)

Nous disposerons de 2 fichiers .py : bruteforce.py et optimized.py

Un diaporama au format .pptx qui explique les 2 algortihmes, la meilleure solution etc.

3 fichiers .csv qui contiennent des tableaux avec le nom des actions, le prix et leur bénéfice   


Pour les utiliser il faudra mettre dans le cmd chemin/bruteforce.py ou optimized.py "chemin du fichiers csv à analyser"
le fichier csv devra avoir 3 cases : nom de l'action | prix | benefice 

à l'aide du fichier csv une fonction construira un dictionnaire en python, c'est sur ce dictionnaire que nos bruteforces fonctionneront.

Fonctionnement du fichier bruteforce.py :
Une fois le fichier csv indiqué après bruteforce.py dans le cmd, une fonction sera utilisée afin de créer un dictionnaire en python ayant comme clé le nom de l'action et comme
valeurs 'cout' et 'benefice finale'.
Ce dictionnaire passera ensuite en paramètre de la fonction brut_force_non_optimise() 
Une boucle while va commencer avec while x < len(dictionnaire) :
  utilisation de combinaison qui prend en compte une liste et le nombre d'item à rentrer pour chaque combinaisons. 
  Le nombnre d'item est egal à x qui au départ vaut 0. 
    On utilisera une boucle for pour enumerer les actions se trouvant dans la combinaisons
    Si le prix total de la combinaison est plus grande que 500 euros, on continue l'opération pour les combinaisons suivantes, sinon on va comparer le bénéfice finale et si celui-ci est plus grand que le benefice que l'on a trouvé juste avant, on remplace celui-ci par le nouveau.
    La fonction prend fin lorsque que toutes les combinaisons possibles ont été faites avec toutes les actions.
    
    
Fonctionnement du fichier optimized.py :
Une fois le fichier csv indiqué après bruteforce.py dans le cmd, une fonction sera utilisée afin de créer un dictionnaire en python ayant comme clé le nom de l'action et comme
valeurs 'cout' et 'benefice finale'.
à la suite de cela 3 dictionnaire seront créés à l'aide de fonction servant à trier le dictionnaire principal de plusieurs manières : selon le prix par ordre décroissant/croissant et selon le bénéfice finale par ordre décroissant.
Pour chacun de ces nouveaux dictionnaires on va utiliser la fonction algo_optimised() qui va acheter une par une les actions dans l'ordre dans lequel elles apparaissent tout en vérifiant que le prix n'est jamais au-dessus de l'argent qui nous reste. Une fois que l'argent ne suffit plus à payer l'action suivante, la fonction se termine en affichant les actions achetées, le bénéfice totale, l'argent depensé et le temps d'execution de la fonction.



