import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation

fig, ax = plt.subplots()

t = np.arange(-2*np.pi, 2*np.pi, 0.1) 
R = 3

anim_object, = plt.plot( [] , [] , '-', lw=2)
	
xdata, ydata = [], []

ax.set_xlim(-10, 10)	
ax.set_ylim(-10, 10)

def update(t): 
    X = R * ( t - np.sin(t))
    Y = R * ( 1 - np.cos(t))

    xdata.append(X) 
    ydata.append(Y) 
    anim_object.set_data(xdata, ydata) 
    return anim_object,

ani = FuncAnimation(fig, update, frames = t , interval=100 ) 
                  
ani.save('lec_7_create_animation.gif')
