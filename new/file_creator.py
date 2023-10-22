from pathlib import Path
import time
import datetime
import os
import sys
import pickle
sys.path.append(os.path.abspath("../"))
try:
    from app import clock, barre_chargement
except ModuleNotFoundError:
    print(" veillez executer new.py depuis son repertoire")



class CreateFileSystem:


   
    def __init__(self,nom,classe,cycle,subject):
        self.cycle=cycle
        self.subject=subject
        ROOT=Path("../data")
        self.ROOT=Path.absolute(ROOT)
        self.nom=nom
        self.classe=classe
        self.user={"nom":self.nom,"classe":self.classe ,"matieres":self.subject,"cycle":self.cycle}


        

    def CreateUserDir(self,):
        username=("_").join(self.nom)+("_"+self.classe)
        self.Dir=self.ROOT/username

        if self.Dir.exists():
           print(" ce nom est deja enregistré")
           os.system(f" tree {self.Dir} ")
           return True
        else:

            self.Dir.mkdir(exist_ok=True)
            return False

    def CreateSubjectFile(self,):
        """ cree un fichier pour chaque matiere"""
        for i in range(len( self.cycle_dir_list)):
            for m in range(len(self.subject)):
                 subject=self.Dir/self.cycle_dir_list[i]/self.subject[m]
                 subject.parent.mkdir(parents=True,exist_ok=True)
                 subject.touch(exist_ok=True)
        print(" creation des matieres ")
       
        print(" OK")
           
   
    def CreateCycle(self,):
        """ cree le dossier de chaque trimestre"""
        #self.cycle_dir=""
        self.cycle_dir_list=[]
        if self.cycle=="TRIMESTRE":
            for i in range(3):
                self.cycle_dir=(self.Dir/f"{i+1}E_TRIMESTRE")
                self.cycle_dir_list.append(self.cycle_dir)
                self.cycle_dir.mkdir(parents=True,exist_ok=True)
        elif self.cycle=="SEMESTRE":
            for i in range(2):
                self.cycle_dir=(self.Dir/f"{i+1}E_SEMESTRE")
                self.cycle_dir_list.append(self.cycle_dir)
                self.cycle_dir.mkdir(parents=True,exist_ok=True)
        
        
        self.CreateSubjectFile()
     #   self.PickelDump(
        barre_chargement()
        print(" les dossiers pour les "+str(self.cycle)+"S on été créé avec success")

    def CreatAgendaDir(self):
        self.agenda=self.Dir/"agenda.txt"
        self.agenda.parent.mkdir(exist_ok=True,parents=True)
        self.agenda.touch(exist_ok=True)
        print(" Agenda crée")
        art=(""". . .((
  . . . .)
  . . ( (
 ████╗
 ████║
 ████╝ """)

        print(art)
    def Tree(self):
        print(" tous les fichiers et repertoire on été crée")
        os.system(f"tree {self.Dir}")

