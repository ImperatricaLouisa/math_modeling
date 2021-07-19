import matplotlib.pyplot as plt
import numpy as np

b0 = np.pi / 2
a = 1
A = 1
B = int(input('B: '))
b = 3
t = np.arange(-13, 13, 0.1 )

xt = A * np.sin( a * t + b0 )
yt = B * np.sin( b * t )

plt.plot( xt , yt )
plt.axis('equal')
plt.show()