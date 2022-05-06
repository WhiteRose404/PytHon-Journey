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






#########################Test
#exercice 1

# Folder = Path.cwd() / "Exercice1Lab"
# Folder.mkdir(exist_ok=True)
# src =  Folder / "OldOne.txt"
# dest = Folder / "NewOne.txt"
# init(src), init(dest);
# all(src,dest)
# ligne(src,dest)

#exercice 2

Folder = Path.cwd() / "Exercice2Lab"
Folder.mkdir(exist_ok=True)

ficher = Folder / "encryptedWords.txt"
ficher.touch(exist_ok=True)


pat = input("enter the path to your folder :")
# print(Lire(pat))
# print(occurance(pat))

print(RC4Fichier(pat,"NightWalker",ficher))