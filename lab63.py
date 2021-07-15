import matplotlib.pyplot as plt
import numpy as np

def eleps(radius):
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
    plt.show()
radius= float(input(' r '))
eleps(radius)