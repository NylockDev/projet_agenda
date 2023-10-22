from colorama import Fore, Back, Style
import os, datetime,sys
from time import sleep
sys.path.append(os.path.abspath("projet_agenda/new"))
sys.path.append(os.path.abspath("projet_agenda/"))
from new import *
from user import information, ask_cycle
from enregisteur import canet_matieres 
from file_creator import CreateFileSystem
from app  import barre_chargement, clock,clear,pickel_dump,pickel_load
from random import randint
import pickle





art=("""
   ╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╭╮╱   ╭━━━╮╭━━━╮╭━━━╮╭━╮╱╭╮╭━━━╮╭━━━╮
   ╱╱╱╱╱╱╱╱╱╱╱╱╭╮╱╱╱╱╭╯╰╮   ┃╭━╮┃┃╭━╮┃┃╭━━╯┃┃╰╮┃┃╰╮╭╮┃┃╭━╮┃
   ╭━━╮╭━╮╭━━╮╱╰╯╭━━╮╰╮╭╯   ┃┃╱┃┃┃┃╱╰╯┃╰━━╮┃╭╮╰╯┃╱┃┃┃┃┃┃╱┃┃
   ┃╭╮┃┃╭╯┃╭╮┃╱╭╮┃┃━┫╱┃┃╱   ┃╰━╯┃┃┃╭━╮┃╭━━╯┃┃╰╮┃┃╱┃┃┃┃┃╰━╯┃
   ┃╰╯┃┃┃╱┃╰╯┃╱┃┃┃┃━┫╱┃╰╮   ┃╭━╮┃┃╰┻━┃┃╰━━╮┃┃╱┃┃┃╭╯╰╯┃┃╭━╮┃
   ┃╭━╯╰╯╱╰━━╯╱┃┃╰━━╯╱╰━╯   ╰╯╱╰╯╰━━━╯╰━━━╯╰╯╱╰━╯╰━━━╯╰╯╱╰╯
   ┃┃╱╱╱╱╱╱╱╱╱╭╯┃╱╱╱╱╱╱╱╱   ╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱
   ╰╯╱╱╱╱╱╱╱╱╱╰━╯╱╱╱╱╱╱╱╱   ╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱
""")
    
print(art)

print(Back.YELLOW+Fore.RED+ " BIENVENUE DANS LE PROJET AGENDA VOTRE AGENDA SCOLAIRE QUI VOUS AIDE TOUTE AU LONG DE VOTRE ANNEE"+Style.RESET_ALL)

print(" veuillez vous enregistrer")
nom,classe=information()
ask_cycle=ask_cycle()
try:
    nbre_matiere=int(input(Fore.CYAN+" entrez le nombre de matiere "+ Fore.RESET))
except ValueError:
    sys.stderr.write(Fore.RED+" ERREUR: vous devez entrez une valeur numerique entiere( pas de virgule)"+Fore.RESET)
    sys.exit("redemarez le programme")
list_matieres=canet_matieres(nbre_matiere)
# instanciation de l'objet systeme de fichier
file_system=CreateFileSystem(nom,classe,ask_cycle,list_matieres)

# creations des systemes de fichiers
is_exist=file_system.CreateUserDir()
 
# si le repertoire  pour ne pas dire l'utilisateur existe deja, propose d'enregistrer une autre personne ou de sortir du programme
if is_exist:
    print(" voulez vous quité le programme ou enregistre une autre personne")
    choix=input(" tapez q pour quité et n pour enregistrer quelqun d'autre")
    while True:
        if choix=="q":
            quit()
        elif choix=="n":
             os.system(" python new.py")
             quit()
            
        else:
            print(Fore.RED+" ENTREE INVALIDE"+ Fore.RESET)
            exit(30)


file_system.CreateCycle()
barre_chargement()
print(Fore.GREEN+" tout le systeme de fichier a été cree pour vos matières"+ Fore.RESET)
clock()
print (" creation des repertoires pour l'agenda",end="")
#clock()
file_system.CreatAgendaDir()
# affiche l'aborescance de dossiers et fichiers crée
file_system.Tree()

print(Fore.GREEN+" OK 👍 tout es en place"+ Fore.RESET)
password=f"{file_system.nom[:1]}{ randint(1,100)}{classe[0]}"
username=((nom[:3]).upper())+str(randint(1,200))
print(Style.BRIGHT+Back.BLACK+Fore.CYAN+f" votre nom d'utilisateur est {username}")
print(f" votre mot de passe est {password}"+Style.RESET_ALL)

file_system.password=password
file_system.username=username

file_system.user["username"]=username
file_system.user["password"]=password

pickel_dump(file_system,username)
file=open("../_src/.utilisateurs.txt","r")
user=file.readlines()
if username in user:
    print(" nom utilisateur existant")

    quit()
else:
    
    file=open("../_src/.list_utilisateurs.txt","a")
    file.write(username+"\n")
    file.close()

with open("../_src/.utilisateurs.txt",'a') as file:
    file.write(f" {file_system.username}_{file_system.password}")

print(Style.BRIGHT+Fore.BLUE)
print(" vous pouvez maitenant effectuer vos taches ajouter des notes, des evenement etc.. ")
exit(0)

