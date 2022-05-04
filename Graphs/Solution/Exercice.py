##  Exercice 1
# 1. Dessiner les Graphes suivants G1 ,G2 et G3 (remarque :99 signifié pas d’arc directe entre les deux nœuds )
G1={
    'a':['b','d','e'],
    'b':['a','c'],
    'c':['b','d'],
    'd' :['a','c','e'],
    'e' :['a','d','f','g'],
    'f' :['e','g'],
    'g' :['e','f','h'],
    'h' :['g']
}

G2=[[99 ,1 ,1, 99, 99, 99,99,99],
[ 99 ,99 ,99, 5 ,99 ,99,99,99],
[99 ,99, 99, 99 ,3, 1,99,99],
[ 99 ,99 ,99 ,99 ,99,99,99 ,10],
[ 99 ,99 ,99 ,99 ,99,2,99 ,99],
[ 99 ,99 ,99 ,99 ,99,99,1 ,99],
[ 99 ,99 ,99 ,99 ,99,99,99 ,2],
[ 99 ,99 ,99 ,99 ,99,99,99 ,99]]

G3=[[99 ,1 ,2, 99, 99, 99],
[ 99 ,99 ,99, 99 ,1 ,99],
[99 ,3, 99, 3 ,99, 99],
[ 99 ,99 ,99 ,99 ,99 ,2],
[99 ,99 ,99 ,2 ,99 ,5],
[ 99 ,99 ,99 ,99, 99 ,99]]

##  Exercice 2
# 1. def BFS(G,s): qui permet de parcourir un Graphe en largeur

def BFS(G,s):
    """ Valid only for dict """
    newGraph = {s:None}
    eyes = [s]
    Legend = [s]
    while(eyes):
        cpivot = eyes.pop(0);
        newGraph[cpivot] = [];
        for adj in G[cpivot]:
            if(adj not in Legend):
                newGraph[cpivot].append(adj);
                eyes.append(adj)
                Legend.append(adj)
        input(f"eyes = {eyes}: ")
    return newGraph
print(BFS(G1,'a'))