import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation
	
fig, ax = plt.subplots()
ax.set_xlim(-50, 50)	
ax.set_ylim(-50, 50)	
anim_object, = plt.plot( [] , [] , '-', lw=2)
	
xdata, ydata = [], []

def cyc(r):
    t = np.arange(0, 2*np.pi+0.1, 0.1) 
    R = r 
    X= R * np.cos(t)
    Y= R * np.sin(t)
    return X, Y
    

def update(t):     
    anim_object.set_data(cyc(t)[0], cyc(t)[1]) 
    return anim_object,

ani = FuncAnimation(fig, update, frames = np.arange(0 , 10, 0.1) , interval=100 ) 
                  
ani.save('lec_.gif')
