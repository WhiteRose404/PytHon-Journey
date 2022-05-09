from matplotlib.pyplot import connect
import numpy as np

# Exercice 01

# Q1
## si a = 1 et b = 0 on va trouver euler explicite
## si a = 0 et b = 1 on va trouver euler implicite

# Q2 

def euler(f,t0,T,y0,N):
    res = [y0]
    i , h = t0, T/N;
    li = np.linspace(t0,t0+T,N-1)
    for i in li:
        res.append(res[-1]+h*f(res[-1],i))
    return res

# Q3 

def heun(f,t0,T,y0,N):
    res = [y0]
    i , h = t0, T/N;
    li = np.linspace(t0,t0+T,N-1)
    for i in li:
        res.append(res[-1]+0.5*h*(f(res[-1],i)+f(res[-1]+h*f(res[-1],i),i+h)))
    return res


#Q4

## Soit z(t) = (y,y') donc z'(t) = F(t,z(t)) = (y',-4pi**2cos(2*pi*t)-y-y') 
from scipy.integrate import odeint
import pylab as pl
# Q5
# t0,T,y0,N = 0,3,[0,0],10000
# f = (lambda y,t: np.array([y[1],-4*np.pi**2*np.cos(2*np.pi*t)-y[0]-y[1]]))
# arg = f,t0,T,y0,N
# eu = euler(*arg)
# he = heun(*arg)

# best = odeint(f,y0,np.linspace(t0,t0+T,N))
# pl.plot(title="circuit RLC tension bobine")
# pl.plot(np.linspace(t0,t0+T,N),he,label="heun")
# pl.plot(np.linspace(t0,t0+T,N),eu,label="euler")
# pl.plot(np.linspace(t0,t0+T,N),best,label="best")
# pl.legend(loc="best")

# pl.show()

# Exercice 2

# Q6. la methode de Newton s'ecrit sous la forme Xn+1 = Xn -f(xn)/f'(xn)
# ou f'(Xn) peut etre appoximé par la valeur f(xn)-f(xn-1)/(xn)-(xn-1)

# Q7. Non, considrant la fonction f(x) = x**2-1 alors si on choiser des valeur assez grand alors
# Xn va tend vers infini comme le montre la figure suivant:

# Q8.
# recursive:
def rsecante(f,xi,xj,eps=1e-10):
    if f(xi) == 0: return xi
    if abs(xi-xj)<eps: return xi
    x = xi - (xi-xj)/(f(xi)-f(xj))
    print(x)

    return rsecante(f,x,xi,eps)

# iterative
def isecante(f,xi,xj,eps=1e-10):
    while abs(xi-xj)>eps:
        x = xi - (xi-xj)/(f(xi)-f(xj))
        xj = xi
        xi = x
    return xi

# Q9
def sqrt(N):
    return rsecante(lambda x: x*x - N,N,1)

# Q 10
def trapez(f,tfinal,N):
    h = abs(tfinal)/N
    x = np.linspace(0,tfinal+h,N);
    sum = 0
    for i in x: sum += f(i)
    sum -= (f(0)+f(tfinal))/2
    return sum*h/tfinal

# Q 11
def ecartype(f,tfinal,N):
    return sqrt(trapez((f-trapez(f,tfinal,N)),tfinal,N))

# Exercice 3
## Base de données
#Q 12
import sqlite3 as sql

def afficherBD():
    connection = sql.connect("./DB/base.sqlite")
    cursor = connection.cursor()
    res = cursor.execute("select * from production").fetchall()
    connection.close()
    return res;

# hada mn 3ndi hh
def remplie(num,nserie,date,typo):
    connection = sql.connect("./DB/base.sqlite")
    cursor = connection.cursor()
    res = cursor.execute("create table if not exists  production(num int,nserie int,dataProduction date,type VARCHAR(14))").fetchall()
    res = cursor.execute("insert into production values (?,?,?,?)",(num,nserie,date,typo)).fetchall()
    connection.commit()
    connection.close()
    return res;

def tofile(data):
    with open("./Files/data.txt",mode="w") as opener:
        for i in data:
            opener.write(str(i))
            opener.write("\n")

# Exercice 04
# Q 13
def f(x):
    return x**2 * np.cos(x**5 * np.exp(x**2)) - x - 1
# Q 14
def deriver(f,x0,h):
    return (f(x0+h)-f(x0))/(h)
# Q 15
h = 0.001
N = int(20//h)
list1 = [ -10+i*h for i in range(N)]
list2 = [ f(x) for x in list1]
list3 = [ deriver(f,x,h) for x in list1]

# Q16
pl.xlabel("sardine")
pl.ylabel("arithmétique")
pl.title("intéligent")
pl.plot(list1,list2)
pl.plot(list1,list3)
pl.show()

#####################################################################################
#Test

# arg =  (lambda x,y: 1),0,1,0,10
# print(heun(*arg))
# num,nserie,date,typo = [0,1,2,3,4,5,6,7,8,9],[12,14,5,47,48,78,98,54,21,12],['1998-02-12','1088-02-12','1998-04-12','2020-02-04','1788-02-12','1798-02-12','1128-02-12','1458-04-12','2032-02-04','1788-02-12'],(['jenkins']*10)
# # for i in range(10): remplie(num[i],nserie[i],date[i],typo[i])
# res = afficherBD()
# dump = tofile(res)