import numpy as np
import matplotlib.pyplot as plt

v = np.array([-1, 2])
vx = np.array([-1,0]) # componente horizontal
vy = np.array([0,2]) # componente vertical

fig, axs = plt.subplots(1, 2, figsize=(12,5))
# 1 linha, 2 colunas | tamanho 12x5

# ------------------------------------------
# GRÁFICO 1 -> só o vetor original
# ------------------------------------------
axs[0].quiver(0, 0, v[0], v[1],
           angles='xy', scale_units='xy', scale=1,
           color='black', label = 'v')

axs[0].annotate("[-1, 2]",
             xy=(v[0], v[1]),        # onde está o ponto
             xytext=(-1.5, 2.2))  

axs[0].set_xlim(-3, 3)
axs[0].set_ylim(-3, 3)
axs[0].set_aspect('equal')
axs[0].grid(True)
axs[0].legend()
axs[0].set_title("Vetor Original")

# ------------------------------------------
# GRÁFICO 2 -> vetor + decomposição
# ------------------------------------------
# componente x (i)
axs[1].quiver(0, 0, vx[0], vx[1],
           angles= 'xy', scale_units='xy', scale=1,
           color='green', label='vx')

# componente Y (j) comeca onde vx termina
axs[1].quiver(vx[0], vx[1], vy[0], vy[1],
           angles= 'xy', scale_units='xy', scale=1,
           color='red', label='vy')

axs[1].annotate("[-1, 0]",
             xy=(vx[0], vx[1]),        # onde está o ponto
             xytext=(-1.2, -0.3))  

axs[1].annotate("[0, 2]",
             xy=(v[0], v[1]),        # onde está o ponto
             xytext=(-1.5, 2.2))  

axs[1].set_xlim(-3, 3)
axs[1].set_ylim(-3, 3)
axs[1].set_aspect('equal')
axs[1].grid(True)
axs[1].legend()
axs[1].set_title("Vetor Decomposto")

plt.show()