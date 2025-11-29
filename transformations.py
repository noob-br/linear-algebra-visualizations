import numpy as np
import matplotlib.pyplot as plt

# check Base
vetor1 = np.array([1, 2])
vetor2 = np.array([3, 1])

matriz = np.column_stack([vetor1, vetor2])
determinante = np.linalg.det(matriz)

print("Determinante:", determinante)

# making linear combinations (span)
combinacoes = []
for a in range(-2, 3):
    for b in range(-2, 3):
        combinacao = a * vetor1 + b * vetor2
        combinacoes.append(combinacao)

combinacoes = np.array(combinacoes)

# Plotar
plt.figure(figsize=(10, 8))
plt.scatter(combinacoes[:, 0], combinacoes[:, 1], alpha=0.6, color='red', label='Span')
plt.quiver(0, 0, vetor1[0], vetor1[1], angles='xy', scale_units='xy', scale=1, 
           color='blue', width=0.015, label=f'Vetor 1: {vetor1}')
plt.quiver(0, 0, vetor2[0], vetor2[1], angles='xy', scale_units='xy', scale=1, 
           color='green', width=0.015, label=f'Vetor 2: {vetor2}')

plt.grid(True)
plt.legend()
plt.title(f'BASE DO R² - Determinante: {determinante:.2f}')
plt.xlim(-8, 8)
plt.ylim(-8, 8)
plt.savefig('base_visualization.png', dpi=150, bbox_inches='tight')
plt.show()
