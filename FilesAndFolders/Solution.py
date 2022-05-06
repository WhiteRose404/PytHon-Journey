from pathlib import Path
from random import randint


# Exercice 01 :
def init(file):
    with file.open(mode='a') as pen:
        for i in range(2000):
            if i%30 == 0: pen.write("\n")
            elif i%5 == 0: pen.write(' ')
            pen.write(chr(randint(97,122)))

# Copier un fichier texte dans un autre :
# 1. Caractère par caractère
def caractére(src,dest):
    with open(dest,mode="a") as Write:
        with open(src,mode='r') as Read:
            for i in Read.read():
                Write.write(i)
        Write.write("\nwritting with dest function")
                
# 2. Ligne par ligne
def ligne(src,dest):
    with open(dest,mode="w") as Write:
        with open(src,mode='r') as Read:
            for i in Read.readlines():
                Write.write(i)
        Write.write("\nwritting with ligne function")

# 3. La totalité du fichier
def all(src,dest):
    with open(dest,mode="w") as Write:
        with open(src,mode='r') as Read:
            Write.write(Read.read())
        Write.write("\nwritting with All function")



# Exercice 02 :
def check(pfile):
    if not pfile.exists():
        print("Error: The file does not exist")
        return False
    elif pfile.is_dir():
        print("Error: this is a directory")
        return False
    return True
    
# 1. Lire un fichier texte, avec un contrôle d'erreur: L'utilisateur saisit le nom du fichier, la machine retourne
# le listing du fichier s'il existe et un message d'erreur s'il n'existe pas.

def Lire(file):
    pfile = Path(file)
    if not check(pfile):
        return False
    contant = ''
    with pfile.open(mode='r') as ofile:
        contant = ofile.read()
    return contant

# 2. Calculer et afficher le nombre de caractères d'un fichier ASCII (un fichier texte)

def occurance(file):
    pfile = Path(file)
    if not check(pfile):
        return False
    count = 0
    with pfile.open(mode='r') as ofile:
        count = len(ofile.read())
    return count


#Exercice 3
# 1. Créer un fichier texte de 5 chaînes de caractères (chacune par ligne).

# 2. Ajouter une fiche (c'est à dire une chaîne de caractères) au fichier précédent
# 3. Rechercher une fiche dans le fichier précédent.




# Exercice 04 (CNC 2012) Chiffrement d'un fichier texte par l'algorithme RC4
# Il s'agit de reprendre l'algorithme RC4 pour chiffrer les lignes d'un fichier texte donné.
# Pour ce faire on suppose avoir définie la fonction d'entête suivante : RC4Chaine(Claire,Clef)
# Cette fonction a pour paramètres :
# • Claire : Une chaine de caractères contenant le texte clair qu'on désire chiffrer
# • Clef : Une chaine de caractères contenant la clé de chiffrement
# La fonction RC4Chaine retourne une chaine de caractères contenant le texte chiffré par l'algorithme RC4, de la
# chaine Claire en utilisant la clé de chiffrement Clef.
#  Question : Chiffrement d'un fichier
# En utilisant la fonction RC4Chaine décrite ci dessus,
#  Écrire la fonction de prototype : def RC4Fichier(fich, Clef, fichChiffre) :Cette fonction permet de
# chiffrer en utilisant la chaine Clef( 2ème paramètre) les lignes du fichier texte de nom physique fich (le
# fichier fich en premier paramètre est supposé existant). Les lignes chiffrées du fichier fich seront mises dans
# un nouveau fichier texte de nom physique fichChiffre( 3ème paramètre) sera crée dans la fonction.


def RC4Chaine(Claire,Clef):
    """we used RSA Algorithm """
    from rc4 import encrypt
    return encrypt(Claire,Clef)

def RC4Fichier(fich,Clef,fichChiffre):
    pfile = Path(fich)
    if not check(pfile): return "ERROR the file does not exist"
    pfichChiffre = Path(fichChiffre)
    pfichChiffre.touch()
    with pfichChiffre.open(mode="wb") as Pen:
        with pfile.open(mode="r") as Book:
            for i in Book.readlines():
                if i=='\n': continue
                Pen.write(RC4Chaine(i,Clef))
    return "Done."


# Le but de cet exercice est de réaliser une application de gestion de notes des élèves d’un centre de CPGE .
# • Un élève sera représenté dans ce programme par : numIns, nom, classe, niveau.
# • Une matière sera représentée dans ce programme par : codeMat, intitulé,coeff.
# • Un examen sera représenté dans ce programme par : numIns, codeMat ,note .

# Eleve = {
#     'numIns':[],
#     'nom':[],
#     'classe':[],
#     'niveau':[]
# }
# Matiere = {
#     'codeMat':[],
#     'intitule':[],
#     'coef':[],
# }
# Examen = {
#     'numIns':[],
#     'codeMat':[],
#     'note':[],
# }
import json
#           Questions :Ecrire les fonctions suivantes :
#   • def ajouterEtudiant (numIns, nom, classe, niveau, fichEtudiants) qui permet d’ajouter un nouvel
#   élève .

def ajouterEtudiant(numIns,nom,classe,niveau,fichEtudiants):
    print("Writing...")
    table = json.load(open(fichEtudiants,mode="r"))
    table['Eleve']['numIns'].append(numIns)
    table['Eleve']['nom'].append(nom)
    table['Eleve']['classe'].append(classe)
    table['Eleve']['niveau'].append(niveau)
    json.dump(table,open(fichEtudiants,mode="w"))
    print("Done.")


# • def afficherEtudiant (numIns, fichEtudiants) qui permet d’afficher un éléve donné par son numIns

def afficherEtudiant(numIns, fichEtudiants):
    table = json.load(open(fichEtudiants,mode='r'))
    index = table['Eleve']['numIns'].index(numIns)
    EleveTable = table['Eleve']
    print(f"Name: {EleveTable['nom'][index]} Class = {EleveTable['classe'][index]} Niveau = {EleveTable['niveau'][index]}")




# • def ajouterMatiere (codeMat, intitulé,coeff, fichMatieres) qui permet d’ajouter une nouvel matière .

def ajouterMatiere(codeMat,intitule,coeff,fichEtudiants):
    print("Writing...")
    table = json.load(open(fichEtudiants,mode="r"))
    table['Matiere']['codeMat'].append(codeMat)
    table['Matiere']['intitule'].append(intitule)
    table['Matiere']['coef'].append(coeff)
    json.dump(table,open(fichEtudiants,mode="w"))
    print("Done.")


# • def afficherMatiere (codeMat, fichMatieres ) qui permet d’afficher une matière donnée par son
# codeMat.

def afficherMatiere (codeMat, fichMatieres ):
    table = json.load(open(fichMatieres,mode='r'))
    EleveTable = table['Matiere']
    index = EleveTable['codeMat'].index(codeMat)
    print(f"intitulé: {EleveTable['intitule'][index]} Coef = {EleveTable['coef'][index]}")






######################### Test Cases
#exercice 1

# Folder = Path.cwd() / "Exercice1Lab"
# Folder.mkdir(exist_ok=True)
# src =  Folder / "OldOne.txt"
# dest = Folder / "NewOne.txt"
# init(src), init(dest);
# all(src,dest)
# ligne(src,dest)

#exercice 2

# Folder = Path.cwd() / "Exercice2Lab"
# Folder.mkdir(exist_ok=True)

# ficher = Folder / "encryptedWords.txt"
# ficher.touch(exist_ok=True)


# pat = input("enter the path to your folder :")
# # print(Lire(pat))
# # print(occurance(pat))

# print(RC4Fichier(pat,"NightWalker",ficher))


#exercice 3


Folder = Path.cwd() / "Exercice3Lab"
Folder.mkdir(exist_ok=True)

ficher = Folder / "Database.json"
# ficher.touch(exist_ok=True)
if not ficher.exists():
    print("ERROR: the database does not exist")
    exit(0)

# ajouterEtudiant(0,"Ahmed","Math","9",ficher)
# ajouterEtudiant(1,"toufiq","physic","5",ficher)
# ajouterEtudiant(3,"Right","Arabic","9",ficher)
# ajouterEtudiant(2,"Peaky","French","9",ficher)
# ajouterEtudiant(4,"Tom","Useless","8",ficher)
# ajouterEtudiant(5,"Arthur","Happend","12",ficher)
afficherEtudiant(5,ficher)

ajouterMatiere(0,"Philosophy",15,ficher)
ajouterMatiere(1,"Arabic",5,ficher)
ajouterMatiere(3,"Francais",3,ficher)
ajouterMatiere(2,"Math",7,ficher)
ajouterMatiere(4,"Physiq",8,ficher)
afficherMatiere(1,ficher)