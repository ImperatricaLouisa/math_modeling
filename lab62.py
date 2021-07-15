import matplotlib.pyplot as plt
import numpy as np

def parabola( a, b, c, title='парабола'):
    
    xa = float(input('xa '))
    xb = float(input('xb '))
    N = float(input('N '))
 
    x = np.arange( xa , xb , N )

    y = a*x**2 + b*x + c

    plt.plot(x,y)
    plt.title(title)
    plt.legend()
    plt.show()


parabola( int(input('a ')) , int(input('b ')), int(input('c ')) )

def giperbola( title='гипербола'):
    
    xc = float(input('xc '))
    xd = float(input('xd '))
    M = float(input('M '))
    k = float(input('k '))
 
    x = np.arange( xc, xd, M )
    y =  k / x


    plt.plot(x,y)
    plt.title(title)
    plt.legend()
    plt.show()


giperbola( )