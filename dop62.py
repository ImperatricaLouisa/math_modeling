import matplotlib.pyplot as plt
import numpy as np

E = 0.5
fi = np.linspace(0, 6*np.pi, 100)

rx = 2
ry = 1
p = ( ry )**2 / rx 

r = p / ( 1 + E * np.cos(fi))

x = r*np.cos(fi)
y = r*np.sin(fi)

plt.plot( x , y )
plt.axis('equal')
plt.show()
    	



