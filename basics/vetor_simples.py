import numpy as np
import matplotlib.pyplot as plt

v = np.array([-1, 2])
vx = np.array([-1,0]) # componente horizontal
vy = np.array([0,2]) # componente vertical

# vetor original
plt.figure()
plt.quiver(0, 0, v[0], v[1],
           angles='xy', scale_units='xy', scale=1,
           color='black', label = 'v')

# componente x (i)
plt.quiver(0, 0, vx[0], vx[1],
           angles= 'xy', scale_units='xy', scale=1,
           color='green', label='vx')

# componente Y (j) comeca onde vx termina
plt.quiver(vx[0], vx[1], vy[0], vy[1],
           angles= 'xy', scale_units='xy', scale=1,
           color='red', label='vy')

plt.xlim(-3, 3)
plt.ylim(-3, 3)
plt.gca().set_aspect('equal')
plt.grid(True)
plt.legend()

plt.show()
