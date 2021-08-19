import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np

fig, ax = plt.subplots()

anim_object, = plt.plot([], [], lw = 2, color = 'pink')

ax.set_xlim(-1, 1)
ax.set_ylim(-1, 1)

C = 0.3
D = 0.33
frames = 100
x = np.zeros((frames))
y = np.zeros((frames))



x[0] = 0.1
y[0] = 0.1

for i in range(1, frames, 1):
    x[i] = x[i-1]**2 - y[i-1]**2 + C
    y[i] = 2*x[i-1]*y[i-1] + D

def update(i):
  anim_object.set_data(x[:i], y[:i])

  return anim_object,

ani = FuncAnimation(fig, update, frames = frames, interval = 10)

ani.save('lab_74.gif')