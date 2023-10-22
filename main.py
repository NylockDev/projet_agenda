import os,sys

from colorama import Style,Back,Fore
sys.path.append(os.path.abspath("./app"))
sys.path.append(os.path.abspath("./"))
sys.path.append(os.path.abspath("./new"))
from app import *
from new import information
from time import sleep
import shutil,copy
from pathlib import Path


def open_file(trimestre,matiere):
    pass


def evenement(choix,matiere,trimestre):
    
    cycle= file_system.cycle.index(trimestre)
    matiere=file_system.subject.index(matiere)
    date=input("quelle est la date de/du {} ".format(choix))
    descr=input(" quel est le tritre ")

def note():
    pass
def moyenne():
    pass

# fonction principale
def main():

    print(" si tu n'es pas encore enregistrer tapez n")
    while True:
        utilisateur=input(Fore.MAGENTA+" entrez votre nom d'utilisateur "+Fore.RESET)       
        if utilisateur=="n":
            os.system(" cd new && python new.py")
        if utilisateur == "":
            print(" vous ne pouvez pas ne rien entrez ")
        else:
            break
    if_locked=open("./_src/.locked_user.txt",'r')
    lock=if_locked.readlines()
    if utilisateur in lock:
        print(Fore.RED+" ce profile est bloqué"+Fore.RESET)
        print(" vous pouvez le debloque en tapant 'd' ou alors recree votre profile en tapant 'n' ")
        ok=input()
        if_locked.close()
        if ok=="d":
            pass

            #  os.system("python debug.py")
        elif ok=="n":
            # print(" tapez 'q' à la fin du programme")
            os.system("cd new && python new.py")
            quit()
        

    liste_utilisateurs=[] 
    with open("./_src/.list_utilisateurs.txt",'r') as file:
        for i in file.readlines():
            liste_utilisateurs.append(i)
   # print(("\n").join(liste_utilisateurs))
    if utilisateur in (("\n ").join(liste_utilisateurs)):
        print(Fore.GREEN+" ok "+utilisateur+Fore.RESET)
        
        
        
        try_left=5
        while try_left>=0:

            file_system=util.pickel_load(utilisateur)
            nom=("").join(file_system.nom)
            password=input(Style.BRIGHT+f"{nom} entrez votre mot de passe "+Style.RESET_ALL)           
            if password != file_system.user["password"]:
                print(Fore.RED+" mot de passe incorrect"+Fore.RESET)
                try_left-= 1
                print(" nombre d'essaie restant",try_left)
               # nbre_requete+=1
            
                if try_left==0:
                    print(Style.BRIGHT+" nombre d'essaie atteint vous n'avez plus acces au profil"+Style.RESET_ALL)                  
                    # liste contenant les utilisateur bloqués
                     
                    locked=open("./_src/.locked_user.txt","a")
                    locked.writelines(utilisateur)
                    exit()
                    
            elif password==file_system.password:
                print(Fore.GREEN+" mot de passe correcte, BIENVENUE ",file_system.nom)
                print(Fore.RESET)
                break
        
    else:
        print(Fore.RED+" utilisateur inexistant"+Fore.RESET)
        util.barre_chargement()
        main()
    util.barre_chargement_advanced()
    util.clear()
    sleep(0.8)
    print(Fore.YELLOW+" UTILISATEUR:",file_system.nom+Fore.RESET)
    requete=user.menu()
    
    if requete=="1":
        choix=user.menu_evenement()

        agenda=file_system.agenda.open(mode="a")
        while True:
            print(" entrer 'r' pour reprendre en cas d'erreur")
            print(Fore.CYAN+" titre de l'evènement")
            choix=input()
            ok=input(" tapez 'enter' pour continuer et 'e'  pour annuler")
            if choix  =='r':
                print(Fore.BLUE+" ok reprenez",end='\r')
            elif choix != "":
                break
            
            else:
                print(Fore.RED+" option ",choix," inexistante"+Fore.RESET)

            if ok == '':
                break
            elif ok == 'e':
                sys.exit("bye...")
    agenda.write_text(f''' {util.afficher_date()}              {choix} ''')                     





# module principale
if __name__=="__main__":
    main()
