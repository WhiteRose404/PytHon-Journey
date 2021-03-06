# La représentation d'un arbre sous forme de classe

# 1. Définir une classe Arbre permettant de déclarer des objets de type Arbre

class Arbre:
    def __init__(self,info=None,gauche=None,droit=None):
        self.info = info;
        self.droit = droit;
        self.gauche = gauche;

# 2.Insertion dans un arbre

def inserer(A,info,pos):
    """
        Insert into the tree in three specifc ways:
            Here , left, right
    """
    N = Arbre(info);
    if(pos == 'right'): A.droit = N
    elif(pos == 'left'): A.gauche = N
    elif(pos == 'Here'): A.info = info
    else: raise LookupError

# 3. Affichage d’un arbre (parcours en profondeur)

def inordre(A):
    if(A == None): return;
    inordre(A.gauche)
    print(A.info)
    inordre(A.droit)

def preordre(A):
    if(A == None): return;
    print(A.info)
    preordre(A.gauche)
    preordre(A.droit)

def postordre(A):
    if(A == None): return;
    postordre(A.gauche)
    postordre(A.droit)
    print(A.info)

    # 4. Affichage d’un arbre (parcours en largeur)

# a) def niveau (A,N) :qui permet d’afficher le niveau N

def niveau(A,N):
    if(A == None): return;
    niveau(A.gauche,N-1)
    niveau(A.droit,N-1)
    if(N==0):
        print(A.info, end=' ')
        return;    
# b) def nombreDeNœudsParNiveau (A,n): qui retourne le nombre de Nœuds d’un niveau N

def nombreDeNœudsParNiveau (A,N):
    if(A == None): return 0;
    count = nombreDeNœudsParNiveau(A.gauche,N-1)
    count += nombreDeNœudsParNiveau(A.droit,N-1)
    if(N==0):
        return 1;
    return count;

# c) def nombreDeNiveaux (A): qui retourne le nombre de niveaux

def nombreDeNiveaux(A):
    Niv = 0;
    while(nombreDeNœudsParNiveau(A,Niv+1) != 0): Niv+=1
    return Niv;

# d) def nombreDeNœuds (A): qui retourne le nombre de Nœuds dans un arbre

def nombreDeNœuds(A):
    if(A == None): return 0;
    Noeuds = 1;
    Noeuds += nombreDeNœuds(A.gauche)
    Noeuds += nombreDeNœuds(A.droit)
    return Noeuds;

# e) def affichageEnLargeur(A):qui affiche un arbre en largeur

def affichageEnLargeur(A):
    nbrNiv =nombreDeNiveaux(A);
    for i in range(nbrNiv+1):
        print(' '*((2**nbrNiv)-2**i),end="")
        niveau(A,i)
        print("")
# 5. def chercher(x,A) :qui retourne True si x existe dans A ,False sinon

def chercher(x,A):
    if(A == None): return False;
    elif(A.info == x): return True;
    if(chercher(x,A.gauche)): return True
    return chercher(x,A.droit)

# 6. def listeDenoeudsParNiveau(A,N) : qui retourne une liste de Nœuds d’un niveau donnée

def listeDenoeudsParNiveau(A,N):
    lis = []
    if(A == None): return [];
    lis.extend(listeDenoeudsParNiveau(A.gauche,N-1))
    lis.extend(listeDenoeudsParNiveau(A.droit,N-1))
    if(N==0):
        return [A.info];
    return lis

# 7. def parfaitComplet(A): qui retourne True si l’arbre A est parfait complet, False sinon
def parfaitComplet(A):
    for i in range(nombreDeNiveaux(A)+1):
        if nombreDeNœudsParNiveau(A,i) != 2**i: return False
    return True

# 8. def parfait(A): qui retourne True si l’arbre A est parfait ,False sinon
def parfait(A):
    for i in range(nombreDeNiveaux(A)):
        if nombreDeNœudsParNiveau(A,i) != 2**i: return False
    return True


# 9. def arbreDerecherche(A): qui retourne True si l’arbre A est un arbre de recherche, False sinon
def arbreDerecherche(A):
    if A == None:
        return True
    if A.gauche != None:
        if A.info < A.gauche.info:
            return False;
    if A.droit != None:
        if A.info > A.droit.info:
            return False    
    return arbreDerecherche(A.gauche) and arbreDerecherche(A.droit)

# 10. def transformerListe(L,A,i=0) :qui permet de transformer une liste simple vers un arbre binaire parfait.
def transformerListe(L,A,i=0):
    pass


# 11. def transformerArbre(A,L) :qui permet de transformer un arbre binaire parfait vers une liste simple.
def transformerArbre(A,L) :
    pass
















################## TEST Cases #########################


A=Arbre()
inserer(A,10,'Here')
inserer(A,5,'left')
inserer(A,15,'right')
inserer(A.gauche ,2,'left')
inserer(A.gauche,7,'right')
inserer(A.droit,12,'left')
inserer(A.droit,17,'right')
inserer(A.gauche.gauche ,1,'left')
inserer(A.gauche.gauche,3,'right')
inserer(A.gauche.droit,6,'left')
inserer(A.gauche.droit,8,'right')
inserer(A.droit.gauche,11,'left')
inserer(A.droit.gauche,7,'right')
inserer(A.droit.droit,16,'left')
inserer(A.droit.droit,18,'right')


affichageEnLargeur(A)

x = 'X'

print(f"Does {x} exists ?",chercher(x,A));
print(listeDenoeudsParNiveau(A,2));
print(parfaitComplet(A));
print(arbreDerecherche(A))