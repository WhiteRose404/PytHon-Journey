from decimal import DivisionByZero
import numpy as np

# 1- Ecrire la fonction dichotomie(f,a,b,epsilon) qui permet d’encadrer la solution cherchée dans un
# intervalle d’amplitude epsilon par la méthode dichotomie. La fonction retourne le point milieu de
# l’intervalle final (solution de l’équation f(x)=0), avec deux méthodes: L’itération et La
# récursivité


def dichotomie(f,a,b,epsilon):
    if f(a)*f(b) > 0: return 'the function has no focal point'
    if f(a)<f(b):
        g = lambda x: -f(x);
        f = g
    """"Suppose that the function fun is decressing if not we tried to fix it above"""
    mi = (b+a)/2
    if abs(b-a)<epsilon or f(mi) == 0:
        return mi
    if f(mi) > 0: a = mi
    else: b = mi
    print(f(mi))
    return dichotomie(f,a,b,epsilon)


def newton(f,s,epsilon):
    """ f must be symplic 
    f must be C1"""
    val_f = f.evalf(subs={x:s});
    val_df = f.diff(x).evalf(subs={x:s});
    if val_f<epsilon:
        return s
    return newton(f,s - val_f/val_df ,epsilon)

def lagrange(f,a,fixe,epsilon):
    """
            f must be symplic 
                    f must be convexe
                            """
    eval = f.evalf(subs={x:fixe})
    val_f = f.evalf(subs={x:a})
    if abs(val_f) < epsilon:
        return a
    y = a - ((fixe - a)/(eval - val_f))*val_f
    if y*a > 0: a = y
    else: fixe = y
    return lagrange(f,y,fixe,epsilon)

def dervie(f,x,h):
    if(h == 0): raise DivisionByZero
    return (f(x+h)-f(x))/h


def secante(f,a,b,epsilon):
    y = a - ((a-b)/(f(a)-f(b)))*f(a)
    if abs(f(y)) < epsilon:
        return y
    b = a
    a = y
    return secante(f,a,b,epsilon)    
    
# Test
import sympy as spy
import numpy as np
x = spy.symbols('x')
f = x**2-3
print(f"the result is {lagrange(f,1.5,2,0.01)}")
print(f"the result is {secante(lambda x: x**2-3,1.5,2,0.01)}")
print(f"the result of divide function is {f.diff().evalf(subs={x:5})} , {dervie((lambda x: x**2-3),5,0.00001)}")
# print(dichotomie( lambda x: np.cos(x)+np.sin(x), 0, np.pi, 1e-10))
