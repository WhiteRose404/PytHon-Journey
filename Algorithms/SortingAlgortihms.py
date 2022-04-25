
def margeSort(tab):
    lt = len(tab);
    if lt <= 1:
        return tab
    mi = len(tab)//2
    tab1 = margeSort(tab[:mi])
    lt1 = len(tab1)
    tab2 = margeSort(tab[mi:])
    lt2 = len(tab2)
    i = j = 0
    ntab = []
    while( i < lt1 and j < lt2):
        if(tab1[i]<tab2[j]):
            ntab.append(tab1[i])
            i+=1
        else:
            ntab.append(tab2[j])
            j+=1
    while( i < lt1):
        ntab.append(tab1[i])
        i+=1
    while( j < lt2):
        ntab.append(tab2[j])
        j+=1
    return ntab

def selectionSort(tab):
    ntab = tab[:]
    lt = len(tab) # len of tab
    for i in range(lt):    
        for j in range(i,len(tab)):
            if(tab[i]>tab[j]): tab[i],tab[j] = tab[j],tab[i]
    return tab

def bubleSort(tab):
    ntab = tab[:]
    lt = len(tab) # len of tab
    flag = True
    while flag:
        flag = False
        for i in range(len(tab)-1):
            if(tab[i]>tab[i+1]):
                tab[i],tab[i+1] = tab[i+1],tab[i]
                flag = True
    return tab


if __name__=="__main__":
    from random import randint
    mylist = [randint(0,10) for i in range(10)]

    print(mylist)
    print(f"buble sort :{bubleSort(mylist)}")
    print(f"Selection sort :{selectionSort(mylist)}")
    print(f"merge sort :{margeSort(mylist)}")
