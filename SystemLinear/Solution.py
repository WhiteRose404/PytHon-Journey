import numpy as np

# 1. Écrire une fonction Pivot qui prend en paramètre une matrice A et un entier j et qui renvoie
# l'indice
# i € [|j,n-1|] tel que |ai,j|=max{|ak,j| }, k € [|j,n-1|]

def pivot(A,j):
    max = j
    for i in range(j,len(A)):
        if A[i,j]>A[max,j]: max = i
    return max;

# 2. Écrire une fonction Echanger qui prend en paramètre une matrice A et deux entier i et j et qui
# permet d'échanger la ligne Li avec ligne Lj .

def echanger(A,i,j):
    temp = np.array(A[j,:])
    A[j,:] = A[i,:]
    A[i,:] = temp

# 3. Écrire une fonction Transvection qui prend en paramètre une matrice A, deux entier i et j et un
# réel c et qui renvoie la matrice A après l'opération Li Li - C Lj c'est-à-dire que l'on retranche à
# la i-ième ligne C fois la j-ième ligne.

def transaction(A,i,j,c):
    Lj = np.array(A[j,:])
    A[j,:] = A[i,:] - c*Lj;
    return A
    
# 4. Écrire une fonction Triang qui prend en paramètre une matrice A et un vecteur b, et qui revoie A0
# et b0 tels que A0 soit triangulaire supérieure et que les systèmes Ax = b et A0 x = b0 soient
# équivalents.

def traing(A,b):
    length = len(A)
    All = np.zeros((length,length+1),dtype=int)
    All[:length,:length]+=A
    All[:,length] = b
    for i in range(length):
        p = pivot(All,i)
        echanger(All,i,p)
        pivo = All[i,i]
        for j in range(i+1,length):
            deno = All[j,i]
            if deno == 0: continue
            transaction(All,i,j,pivo/deno)
    return (np.array(All[:,:len(A)]),np.array(All[:,len(A)]).reshape(len(A),1))

# 5. Écrire une fonction ResolutionT qui prend en paramètre une matrice triangulaire supérieure A et
# un vecteur b et qui, sous réserve que le système soit de Cramer, revoie l'unique vecteur x tel que
# Ax = b


#######################TEST
def show(*arg):
    print(*arg,sep="\n")
A = np.array([[1,0,-1,54],
            [2,3,-1,54],
            [0,4,4,12],
            [1,1,2,0]])
show(A)

show("pivot of the current matrice ",pivot(A,0))
echanger(A,0,1);
show("echange ligne 0 avec ligne 1",A)


show(traing(A,np.array([1,2,3,4])))
