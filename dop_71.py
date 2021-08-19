import matplotlib.animation as animation
import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots()
ball, = plt.plot([], [], 'o', color='red', label='Ball')


def circle_move(R, angle_vel, time): 
    t = angle_vel * (np.pi/180) * time
    X = R * ( t - np.sin(t))
    Y = R * ( 1 - np.cos(t))
    return X,Y
	
edge = 40
plt.axis('equal')
ax.set_xlim( 0 , edge)
ax.set_ylim( 0 , edge)

def animate(i):
    ball.set_data(circle_move(R=3, angle_vel=1, time=i))

ani = animation.FuncAnimation(fig, animate , frames = 1000 , interval=10 ) 
                  
ani.save('aaaaaa_71.gif')
