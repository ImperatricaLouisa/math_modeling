import matplotlib.animation as animation
import matplotlib.pyplot as plt
import numpy as np
 
fig, ax = plt.subplots()
ball, = plt.plot([], [], color='r')


def init():
    ball.set_data([], [])
    return ball,

p = np.arange( 0 , 4*np.pi, 0.1) 
x = 12 * np.cos(p) + 8 * np.cos(1.5 * p)
y = 12 * np.sin(p) - 8 * np.sin(1.5 * p)



plt.axis('equal')
ax.set_xlim(-25, 25)
ax.set_ylim(-25, 25)

def animate(i):
    X = x * np.cos(i) - y * np.sin(i)
    Y = y * np.cos(i) + x * np.sin(i)
    
    ball.set_data(X, Y)
    return ball,
    
ani = animation.FuncAnimation(fig, animate , frames = np.arange( 0 , 2*np.pi, 0.1)  , interval=10 )

ani.save('aa_72.gif')