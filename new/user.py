from colorama import Back, Fore, Style
import sys
import os

sys.path.append(os.path.abspath("../"))
from app import barre_chargement
from time import sleep
class Etudiant:
    """ la class etudiànt es un objet c'es a dire un etudiant ou un eleve qui utilise l'appication pour calculer ses moyennes scolaire on stocke les info de l'utilisateur ici 
    nom: naturellement le nom de l'etudiant
    class: sa classe frequenter 
    pour pouvoir l'ecrire dans son bulletin a l'entête"""


    def __init__(self,nom,classe):
        self.nom=nom.upper()
        self.classe=classe.upper()
    def SePresenter(self):
        """ ici l'etudiant ou l'eleve se presente avec son nom et sa classe"""
        print(Fore.CYAN+f" Nom:{self.nom}\nClasse:{self.classe} "+Fore.RESET)
    
    
def information():
    """ ici cette methode renseigne les information de l'utilisateur"""
    #! le nom de l'uilisateur
    nom=input(Fore.LIGHTBLUE_EX+" Hello 😎 quelle est ton nom complet? ")
    nom=nom.upper()
    print(Fore.RESET)
    #! la classe de l'utilisateur
    classe=input(Fore.CYAN+" Quelle est ta classe ?"+ Back.BLACK+Fore.WHITE+" ")
    print(Style.RESET_ALL)
    barre_chargement()
    art=("""
☆┌─┐  ─┐☆
　│▒│ /▒/
　│▒│/▒/
　│▒ /▒/─┬─┐◯
　│▒│▒|▒│▒│
┌┴─┴─┐-┘─┘
│▒┌──┘▒▒▒│◯
└┐▒▒▒▒▒▒┌┘
◯└┐▒▒▒▒┌
        """)
    print(art)
    print(Fore.GREEN+":)"+Fore.CYAN+"ok",nom,"comme ça vous etes en",classe+" tres bien 😁😁")
    print(Style.RESET_ALL)
    sleep(0.7)

    nom=nom.strip()

   
    return nom, classe


def ask_cycle():
    """ cette fonction demande le systeme de decoupage de l'année scolaire à l'utilisateur
    :returns str : retour trimestre ou semestre selon son choix(lutilisateur)"""
    while True:
        cycle=input(Fore.CYAN+" QUEL SYSTEME UTILISEZ VOUS TAPEZ 1 POUR TRIMESTRE ET 2 POUR SEMESTRE "+ Fore.RESET)
        if cycle=="1":
            
            return "TRIMESTRE"
            break
        elif cycle=="2":
            
            return "SEMESTRE"
            break
        else:
            print(Fore.RED+" entrée invalide reesayez !!"+ Fore.RESET)
            
