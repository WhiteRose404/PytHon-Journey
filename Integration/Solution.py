import numpy as np


class integrate:
    integral = 0
    def __init__(self,start,end,step = 1000,fun=lambda x: x**2):
        import matplotlib.pyplot as plt
        index = self._MENU(fun)-1
        method = [self.rectangle,self.trapez,self.simpson]
        x = np.linspace(start,end,step)
        y = np.array([fun(i) for i in x])
        method[index](fun,x,step)
        print(self.integral)
        plt.plot(x,y)
        plt.grid(True)
        plt.show()

    def rectangle(self,fun, x, step):
        sum = 0
        space = (x[-1]-x[0])/(step*2)
        for i in range(len(x)-1):
            sum += fun(x[i]+space)
        self.integral = sum*(2*space)
    def trapez(self,fun,x,step):
        sui = sum([ fun(i) for i in x[1:-1] ])
        sui += (x[0]+x[-1])/2
        self.integral = sui * (x[-1]-x[0])/step
    def simpson(self,fun,x,step):
        res = (x[0]+x[-1])
        sui = sum([ fun(i) for i in x[1:-1] ])
        res += 4*sui + 2*sui + 4*x[0]
        self.integral = res * (x[-1]-x[0])/(6*step)
    
    def _MENU(self,fun):
        print("chose Which method to integrate with:")
        print("\t1+ Rectangle")
        print("\t2+ Trapez")
        print("\t3+ Simpson")
        k =  input(">")
        while (not k.isdigit()) or int(k) > 3 or int(k) < 1:
            print("Please enter a valid number")
            k = input('>')
        return int(k)


Tra = integrate(0,1, fun=lambda x: np.log(x+1)-x**3+4)

# REFACTOR