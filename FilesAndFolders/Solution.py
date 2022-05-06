from pathlib import Path
from random import randint


# Exercice 01 :
def init(file):
    file.touch(exists_ok=True)
    for i in range(2000):
        if i%30 == 0: file.write("\n")
        elif i%5 == 0: file.write(' ')
        file.write(chr(randint(97,122)))# Copier un fichier texte dans un autre :
# 1. Caractère par caractère
def caractére(src,dest):
    with open(dest,mode="w") as Write:
        with open(src,mode='r') as Read:
            for i in Read.read():
                Write.write(i)

        
# 2. Ligne par ligne
def ligne(src,dest):
    with open(dest,mode="w") as Write:
        with open(src,mode='r') as Read:
            for i in Read.readlines():
                Write.write(i)


# 3. La totalité du fichier
def all(src,dest):
    with open(dest,mode="w") as Write:
        with open(src,mode='r') as Read:
            Write.write(Read.read())

src = "/home/youssef/Documents/studies/Master/PythonCourse/FilesAndFolders/OldOne.txt"
dest = "/home/youssef/Documents/studies/Master/PythonCourse/FilesAndFolders/NewOne.txt"
init(src), init(dest);