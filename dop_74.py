import matplotlib.animation as animation
import matplotlib.pyplot as plt
import numpy as np
 
fig, ax = plt.subplots()
ball, = plt.plot([], [], color='r')


def init():
    ball.set_data([], [])
    return ball,

x1 = [10, 10 ,-10, -10, 10]
y1 = [10, -10, -10, 10, 10]
x = np.array(x1)
y = np.array(y1)

plt.axis('equal')
ax.set_xlim(-25, 25)
ax.set_ylim(-25, 25)

def animate(i):
    X = x * np.cos(i) - y * np.sin(i)
    Y = y * np.cos(i) + x * np.sin(i)
    
    ball.set_data(X, Y)
    return ball,
    
ani = animation.FuncAnimation(fig, animate , frames = np.arange( 0 , 2*np.pi, 0.1)  , interval=10 )

ani.save('a_74.gif')