import numpy as np


# 1. Écrire la fonction euler ( f,a,b,y0,h )

def euler(f,a,b,y0,h):
    Un, i = [y0], a
    while i < b:
        k = Un[-1]
        Un.append(k+f(i,k)*h)
        i += h
    return Un

# 2. Écrire la fonction heun ( f,a,b,y0,h )

def heun(f,a,b,y0,h):
    Un, i = [y0], a
    while i < b:
        un = Un[-1]
        Un.append(un+h/2*(f(i,un)+f(i+h,un+h*f(i,un))))
        i += h
    return Un

# 3. La méthode de Runge-Kutta (ou RK4) RK4 ( f,a,b,y0,h )

def RK4(f,a,b,y0,h):
    Un, i = [y0], a
    while i < b:
        un = Un[-1]
        k1 = f(i,un)
        k2 = f(i+h/2,un+h*k1/2)
        k3 = f(i+h/2,un+h*k2/2)
        k4 = f(i+h,un+h*k3)
        Un.append(un+h/6*(k1+k4+2*(k2+k3)))
        i += h
    return Un
    
def AdamsBashforth(f,a,b,y0,h):
    i = a
    Un = [y0]
    Un.append(y0+h*f(i,y0))
    while i <= b:
        un0 = Un[-1]
        un1 = Un[-2]
        res = un0 + 3/2*h*f(i,un0)-h/2*f(i-h,un1)
        Un.append(res)
        i+=h
    return Un



# 6. Résoudre y’=y entre 0 et 5 pour un pas de 0.1 avec y(0)=1
a,b,y0,h = 0,1,1,0.01
arg = (lambda x,y: y),a,b,y0,h

# 7. Résoudre y’=sin(t*y(t)) entre 0 et pi pour un pas de 0.1 avec y(0)=1
a,b,y0,h = 0,np.pi,1,0.1
arg = (lambda x,y: np.sin(x*y)),a,b,y0,h

# 8. Résoudre y’=-0.5y entre 0 et 5 pour un pas de 0.1 avec y(0)=1
a,b,y0,h = 0,5,1,0.1
arg = (lambda x,y: -0.5*y),a,b,y0,h

# 9. Résoudre l’équation de Lotka-Volterra (système proie-prédateur) x’=x(a-by) et y’=y(-c+dx) entre
# 0 et 1000 pour un pas de 0.1 (x0,y0)=(100,80) et a = 1,b = 0.005, c = 1.5,d = 0.01
a,b,y0,h = 0,20,(100,80),0.1
arg = (lambda x,y: np.array((y[0]*(1-0.005*y[1]),y[1]*(-1.5+0.01*y[0])))),a,b,y0,h

############################ TEST #######################
ru = RK4(*arg)
he = heun(*arg)
eu = euler(*arg)
ad = AdamsBashforth(*arg)
# v = []
length = len(ru)
for i in range(length):
    x = a+i*(b-a)/(length-1)
    # v.append(np.exp(x)) # Question 6
    print(f"For i = {x}")
    # e = eu[i]
    # print(f" Euler: {e}")
    # h = he[i]
    # print(f" Heun: {h:.3f}",end=" ")
    # r = ru[i]
    # print(f" runge: {r:.3f}",end=" ")
    A = ad[i]
    print(f" adams: {A}")

import matplotlib.pyplot as plt

# plt.plot(np.linspace(a,b,len(he)),he)
# plt.plot(np.linspace(a,b,len(v)),v,color="red")
# plt.plot(np.linspace(a,b,len(ru)),ru)
# plt.plot(np.linspace(a,b,len(he)),he)
plt.plot(np.linspace(a,b,len(ad)),ad)
# plt.plot(np.linspace(a,b,len(eu)),eu)
plt.grid()
plt.show()