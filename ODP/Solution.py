

# 1. Écrire la fonction euler ( f,a,b,y0,h )

def euler(f,a,b,y0,h):
    Un, i = [y0], a
    while i < b:
        k = Un[-1]
        print(k)
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
    

############################ TEST #######################
a,b,y0,h = 1,2,2,0.001
arg = (lambda x,y: -x**4*y**3),a,b,y0,h
runge = RK4(*arg)
he = heun(*arg)
eu = euler(*arg)
for i in range(len(he)):
    print(f"For i = {a+i*h}")
    print(f"\t Heun: {he[i]}",end=" ")
    print(f"\t Euler: {eu[i]}",end=" ")
    print(f"\t runge: {runge[i]}")