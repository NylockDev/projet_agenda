from colorama import Fore,Back, Style
import sys,os
sys.path.append("../")
from app.util import barre_chargement,clear
from time import sleep
import sys

""" l'enregistreur  note les matières ensuite leurs moyenne et coefficient  dans une liste
"""


def canet_matieres(n):
    carnet_matieres = []
    print("Entrez vos différentes matières une par une")
    
    while len(carnet_matieres) < n:
        matieres = input(Style.BRIGHT + " >>  " + Style.RESET_ALL)
        
        if matieres in carnet_matieres:
            print(Fore.RED + f"Vous avez déjà entré {matieres}." + Fore.RESET)
        elif len(matieres) < 2:
            is_true = input(Fore.CYAN + "Êtes-vous sûr que c'est ça (oui/non) " + Fore.RESET)
            
            if is_true == 'oui':
                print("Ok")
            elif is_true == "non":
                print("okay entrez en une autre")
            else:
                print("ERREUR : Répondez par 'oui' ou 'non'. On recommence.")
                continue  # Continuez la boucle sans ajouter la matière en cas d'erreur de saisie
        else:
            carnet_matieres.append(matieres)
    
    barre_chargement()
    print(Fore.GREEN + "Vos matières ont bien été enregistrées" + Fore.RESET)
    return carnet_matieres


def carnet_moyennes(matieres:list):
    """ carnet des moyennes de chaque matieres
    :param list matieres: constitue les matieres de l'utilisateur retourné par la fonction carnet_matieres
    """
    moyennes=[]
    for matiere in matieres:
        contener=[]   # contener ressence la moyenne et le coefficient
        try:
            moyenne=float( input(Fore.CYAN+" entrez la moyenne pour {} ".format(matiere)+Fore.RESET))
            coeff=int(input(" entrez le coefficient "))
        except ValueError:
            print(Back.YELLOW+Fore.RED+" ERREUR: vous devez entrez une valeur numerique"+Style.RESET_ALL)
            exit()
        contener.append(moyenne)
        contener.append(coeff)
        moyennes.append(contener)
    return moyennes


