import matplotlib.pyplot as plt
import numpy as np

def f():
    x = np.linspace(-10, 10, 1000)
    
    y = np.zeros([len(x)])
    
    a = int(input(' a: '))
    b = int(input(' b: '))
    
    for i in range(0, len(x), 1): 
        if a>x[i]:
            y[i] = a ** 2
            
        elif x[i]>b:
            y[i] = b ** 2
            
        else:
            y[i] = x[i] ** 2
            
    plt.plot(x, y)
    plt.axis('equal')
    plt.show()

f()