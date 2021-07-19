import matplotlib.pyplot as plt
import numpy as np
from math import pi,sin,cos

def okru(radius):
    N = float(input('N '))
    M = float(input('M '))
    xa = float(input('xa '))
    xb = float(input('xb '))
    xc = float(input('xc '))
    xd = float(input('xd '))
    
    x = np.arange( xa , xb , N )
    y = np.arange( xc , xd , M )

    X, Y = np.meshgrid(x, y)

    fxy = X**2 + Y**2 
   
    plt.contour(X, Y, fxy, levels=[radius**2])
    plt.axis('equal')
    plt.show()
    	

radius= float(input(' r '))
okru(radius)


def eleps(rx , ry):
    x0=1
    y0=0.5
    
    t = np.linspace(0, 2*pi, 100)
    X = x0 + rx*np.cos(t)
    Y = y0 + ry*np.sin(t)
   
    plt.plot( X , Y )
    plt.axis('equal')
    plt.show()
    	

rx = float(input(' rx '))
ry = float(input(' ry '))
eleps(rx , ry)
