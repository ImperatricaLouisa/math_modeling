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





#import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation
	
fig, ax = plt.subplots()

t = np.arange(0, 2*np.pi, 0.1) 


anim_object, = plt.plot( [] , [] , '-', lw=2)
	
xdata, ydata = [], []

ax.set_xlim(-2*np.pi, 2*np.pi)	
ax.set_ylim(-2*np.pi, 2*np.pi)

def update(t): 
    R = t 
    X= R * np.cos(t)
    Y= R * np.sin(t)
    
    xdata.append(X) 
    ydata.append(Y) 
    anim_object.set_data(xdata, ydata) 
    return anim_object,

#def animate(i):
#    ball.set_data(circle_move(R=0.5, vx0=0.01, vy0=0.01, time=i))

ani = FuncAnimation(fig, update, frames = t , interval=100 ) 
                  
ani.save('lec_7_create_animation.gif')