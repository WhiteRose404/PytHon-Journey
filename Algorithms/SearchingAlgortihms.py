
from SortingAlgortihms import bubleSort,margeSort,selectionSort

def dichtomie(tab,x,sorted=False):
    if(not sorted):
        tab = margeSort(tab)
    if(len(tab)==0):
        return False
    mill = len(tab)//2
    if x==tab[mill]: return True
    elif(x>tab[mill]): return dichtomie(tab[mill+1:],x,True)
    else: return dichtomie(tab[:mill],x,True)

from random import randint
mylist = [randint(0,10) for i in range(10)]
x = randint(0,10)
print(f"searcing for {x} in {mylist} found {dichtomie(mylist,x,False)}")
