import numpy as np
import matplotlib.pyplot as plt

from matplotlib.animation import FuncAnimation

import matplotlib.animation as animation


def cic( R , t ):
    x = R * (np.cos(t))**3
    y = R * (np.sin(t))**3
    return x, y

def cir_f( R , N , t ):
    x = np.zeros(N)
    y = np.zeros(N)
    for i in range ( 0 , N , 1 ):
        alpha = np.linspace( 0 , 2*np.pi , N)
        x[i] = R * t + R * np.cos(alpha[i])
        y[i] = R + R * np.sin(alpha[i])
    return x , y

fig, ax = plt.subplots()
fig = plt.figure(figsize=(10,3), facecolor = 'pink' , frameon = True)

ball, = plt.plot([], [], color='r', label='Ball')
ball2, = plt.plot([], [], 'o', color='g', label='Ball2')
ball3, = plt.plot([], [], color='b', label='Ball3')

def animate(i):
    ball.set_data(cic(R=1, t = np.linspace( 0 , 4 * np.pi * i / 100 , 1 * i)))
    ball2.set_data(cic(R=1, t = 4 * np.pi * i / 100 ))
    ball3.set_data(cic(R=1, t = 4 * np.pi * i / 100 ))
    
ani = animation.FuncAnimation(fig,animate,frames=100,interval=100)

ani.save('lec_71(2).gif')
