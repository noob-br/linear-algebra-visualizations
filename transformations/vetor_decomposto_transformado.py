import numpy as np
import matplotlib.pyplot as plt

v = np.array([-1, 2])
vx = np.array([1,0]) # componente horizontal
vy = np.array([0,1]) # componente vertical

t = np.array([5, 2]) # transformado
tx = np.array([1,-2]) # transformado horizontal
ty = np.array([3,0]) # transformado vertical
tdx = np.array([-1,2]) # aplicado formula horizontal
tdy = np.array([6,0]) # aplicado formula horizontal


fig, axs = plt.subplots(2, 3, figsize=(12,9))
plt.subplots_adjust(hspace=0.3)
fig.text(0.2, 0.35,
         r"$v = -1\hat{\imath} + 2\hat{\jmath}$",
         ha="center", va="center", fontsize=16)
         


# fig.text(0.5, 0.48, "Texto entre as linhas", 
#          ha='center', va='center', fontsize=16)# 1 linha, 2 colunas | tamanho 9x9

# ------------------------------------------
# GRÁFICO 1 -> só o vetor original
# ------------------------------------------
axs[0,0].quiver(0, 0, v[0], v[1],
           angles='xy', scale_units='xy', scale=1,
           color='black', label = 'v')

axs[0,0].annotate("[-1, 2]",
             xy=(v[0], v[1]),        # onde está o ponto
             xytext=(-1.5, 2.2))  

axs[0,0].set_xlim(-3, 3)
axs[0,0].set_ylim(-3, 3)
axs[0,0].set_aspect('equal')
axs[0,0].grid(True)
axs[0,0].legend()
axs[0,0].set_title("Vetor Original")

# ------------------------------------------
# GRÁFICO 2 -> vetor + decomposição
# ------------------------------------------
# componente x (i)
axs[0,1].quiver(0, 0, v[0], v[1],
           angles='xy', scale_units='xy', scale=1,
           color='black', label = 'v')

axs[0,1].quiver(0, 0, vx[0], vx[1],
           angles= 'xy', scale_units='xy', scale=1,
           color='green', label='î')

# componente Y (j) comeca onde vx termina
axs[0,1].quiver(0, 0, vy[0], vy[1],
           angles= 'xy', scale_units='xy', scale=1,
           color='red', label='j')

axs[0,1].annotate("[-1, 0]",
             xy=(vx[0], vx[1]),        # onde está o ponto
             xytext=(-1.2, -0.4))  

axs[0,1].annotate("[0, 2]",
             xy=(v[0], v[1]),        # onde está o ponto
             xytext=(-1.5, 2.2))  

axs[0,1].set_xlim(-3, 3)
axs[0,1].set_ylim(-3, 3)
axs[0,1].set_aspect('equal')
axs[0,1].grid(True)
axs[0,1].legend()
axs[0,1].set_title("Tag i-hat and j-hat")

# ------------------------------------------
# GRÁFICO 3 -> Transformado Decomposto (corrigido)
# ------------------------------------------
axs[0,2].quiver(0, 0, t[0], t[1],
           angles='xy', scale_units='xy', scale=1,
           color='black', label = 't')

# anotar coordenadas DO VETOR TRANSFORMADO acima do ponto
axs[0,2].annotate(f"[{t[0]}, {t[1]}]",
             xy=(t[0], t[1]),
             xytext=(0, 8),                # 8 pontos acima
             textcoords='offset points',
             ha='center', va='bottom',
             fontsize=10, color='black',
             bbox=dict(facecolor='white', alpha=0.6, edgecolor='none'))

# componente tx (i)
axs[0,2].quiver(0, 0, tx[0], tx[1],
           angles='xy', scale_units='xy', scale=1,
           color='green', label='tx')

# componente ty deve começar onde tx termina
axs[0,2].quiver(0, 0, ty[0], ty[1],
           angles='xy', scale_units='xy', scale=1,
           color='red', label='ty')

# anotações para tx e ty (posicionamento relativo)
axs[0,2].annotate(f"[{tx[0]}, {tx[1]}]",
             xy=(tx[0], tx[1]),
             xytext=(8, -8),
             textcoords='offset points',
             ha='left', va='top',
             fontsize=10, color='green',
             bbox=dict(facecolor='white', alpha=0.6, edgecolor='none'))

axs[0,2].annotate(f"[{ty[0]}, {ty[1]}]",
             xy=(tx[0]+ty[0], 0+ty[1]),
             xytext=(8, -8),
             textcoords='offset points',
             ha='left', va='top',
             fontsize=10, color='red',
             bbox=dict(facecolor='white', alpha=0.6, edgecolor='none'))

axs[0,2].set_xlim(-0.5, 5.5)
axs[0,2].set_ylim(-3, 3)
axs[0,2].set_aspect('equal')
axs[0,2].grid(True)

# legenda deslocada para não cobrir o gráfico
axs[0,2].legend(loc='upper left', bbox_to_anchor=(0.02, 0.98))

axs[0,2].set_title("Vetor transformado e\n vetores i-hat e j-hat transformado")


# ------------------------------------------
# GRÁFICO 4 -> Finding Transformed i and transformed j
# ------------------------------------------
# componente x (i)
axs[1,0].quiver(0, 0, tx[0], tx[1],
           angles= 'xy', scale_units='xy', scale=1,
           color='green', label='tx')

axs[1,0].quiver(0, 0, ty[0], ty[1],
# componente Y (j) comeca onde vx termina
           angles= 'xy', scale_units='xy', scale=1,
           color='red', label='ty')

axs[1,0].annotate("[1, -2]",
             xy=(tx[0], tx[1]),        # onde está o ponto
             xytext=(0.7, -2.4))  

axs[1,0].annotate("[3, 0]",
             xy=(t[0], t[1]),        # onde está o ponto
             xytext=(3.2, -0.2))  

axs[1,0].set_xlim(-0.5, 5.5)
axs[1,0].set_ylim(-3, 3)
axs[1,0].set_aspect('equal')
axs[1,0].grid(True)
axs[1,0].legend()
axs[1,0].set_title("v = -1(Transformed î) + 2(Transformed ĵ\nAplicando o conceito)")


# ------------------------------------------
# GRÁFICO 5 -> Transformed V
# ------------------------------------------

axs[1,1].quiver(0, 0, tdx[0], tdx[1],
           angles= 'xy', scale_units='xy', scale=1,
           color='green', label='tx')

axs[1,1].quiver(tdx[0], tdx[1], tdy[0], tdy[1],
# componente Y (j) comeca onde vx termina
           angles= 'xy', scale_units='xy', scale=1,
           color='red', label='ty')


# anotação do tdx (verde)
axs[1,1].annotate(f"[{tdx[0]}, {tdx[1]}]",
                  xy=(tdx[0], tdx[1]),
                  xytext=(8, -8),
                  textcoords='offset points',
                  ha='left', va='top',
                  fontsize=10, color='green',
                  bbox=dict(facecolor='white', alpha=0.6, edgecolor='none'))

# anotação do tdy (vermelho) — começa em tdx
axs[1,1].annotate(f"[{tdy[0]}, {tdy[1]}]",
                  xy=(tdx[0] + tdy[0], tdx[1] + tdy[1]),
                  xytext=(8, -8),
                  textcoords='offset points',
                  ha='left', va='top',
                  fontsize=10, color='red',
                  bbox=dict(facecolor='white', alpha=0.6, edgecolor='none'))

axs[1,1].set_xlim(-1.5, 5.5)
axs[1,1].set_ylim(-1, 6)
axs[1,1].set_aspect('equal')
axs[1,1].grid(True)
axs[1,1].legend()
axs[1,1].set_title("Vetores i-hat e j-hat resultantes",
         ha='center', va='center', fontsize=12)

# ------------------------------------------
# GRÁFICO 6 -> Finding Transformed i and transformed j
# ------------------------------------------
# componente x (i)

axs[1,2].quiver(0, 0, t[0], t[1],
           angles='xy', scale_units='xy', scale=1,
           color='black', label = 't')

axs[1,2].quiver(0, 0, tdx[0], tdx[1],
           angles= 'xy', scale_units='xy', scale=1,
           color='green', label='tx')

axs[1,2].quiver(tdx[0], tdx[1], tdy[0], tdy[1],
# componente Y (j) comeca onde vx termina
           angles= 'xy', scale_units='xy', scale=1,
           color='red', label='ty')

axs[1,2].annotate("[4, -2]",
             xy=(v[0], v[1]),        # onde está o ponto
             xytext=(4, -2.2))  

# anotação do tdx (verde)
axs[1,2].annotate(f"[{tdx[0]}, {tdx[1]}]",
                  xy=(tdx[0], tdx[1]),
                  xytext=(8, -8),
                  textcoords='offset points',
                  ha='left', va='top',
                  fontsize=10, color='green',
                  bbox=dict(facecolor='white', alpha=0.6, edgecolor='none'))

# anotação do tdy (vermelho) — começa em tdx
axs[1,2].annotate(f"[{tdy[0]}, {tdy[1]}]",
                  xy=(tdx[0] + tdy[0], tdx[1] + tdy[1]),
                  xytext=(8, -8),
                  textcoords='offset points',
                  ha='left', va='top',
                  fontsize=10, color='red',
                  bbox=dict(facecolor='white', alpha=0.6, edgecolor='none'))

# anotação do vetor final t
axs[1,2].annotate(f"[{t[0]}, {t[1]}]",
                  xy=(t[0], t[1]),
                  xytext=(8, 8),
                  textcoords='offset points',
                  ha='left', va='bottom',
                  fontsize=10, color='black',
                  bbox=dict(facecolor='white', alpha=0.6, edgecolor='none'))

axs[1,2].set_xlim(-1.5, 5.5)
axs[1,2].set_ylim(-1, 6)
axs[1,2].set_aspect('equal')
axs[1,2].grid(True)
axs[1,2].legend()
axs[1,2].set_title("Vetores resultantes",
         ha='center', va='center', fontsize=12)

fig.suptitle(r"$\vec v = -1\hat{\imath} + 2\hat{\jmath}$",
             fontsize=20, fontweight='bold')

plt.show()
