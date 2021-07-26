import matplotlib.pyplot as plt
import numpy as np

E = np.arange ( 0 , 1 )
fi = np.linspace(0, 2*np.pi, 100)

rx = 2
ry = 1
p = ( ry )**2 / rx 

r = p / ( 1 + E * np.cos(fi))

x = r*np.cos(fi)
y = r*np.sin(fi)

plt.plot( x , y )
plt.axis('equal')
plt.show()
    	



