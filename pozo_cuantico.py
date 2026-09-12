import numpy as np
import matplotlib.pyplot as plt

# Constantes físicas fundamentales (en unidades simplificadas para la simulación)
# Usaremos masas y dimensiones normalizadas para observar el comportamiento analítico
hbar = 1.0  # Constante reducida de Planck
m = 1.0     # Masa de la partícula
L = 5.0     # Ancho del pozo cuántico

# Función para calcular los niveles de energía del pozo cuántico infinito
def energia_cuantica(n, m, L):
    """
    Calcula la energía E_n para el estado n en un pozo de potencial infinito de ancho L.
    E_n = (n^2 * pi^2 * hbar^2) / (2 * m * L^2)
    """
    return (n**2 * np.pi**2 * hbar**2) / (2 * m * L**2)

# Evaluamos los primeros 4 estados cuánticos (n = 1, 2, 3, 4)
estados = [1, 2, 3, 4]
energias = [energia_cuantica(n, m, L) for n in estados]

print("Niveles de energía calculados para el pozo cuántico:")
for n, E in zip(estados, energias):
    print(f"Estado n = {n}: E_{n} = {E:.4f}")

# Generación de la gráfica de las funciones de onda dentro del pozo
x = np.linspace(0, L, 500)
plt.figure(figsize=(8, 6))

for n in estados:
    # Función de onda normalizada: psi_n(x) = sqrt(2/L) * sin(n * pi * x / L)
    psi = np.sqrt(2 / L) * np.sin(n * np.pi * x / L)
    # Desplazamos la onda verticalmente según su nivel de energía para visualizar mejor
    plt.plot(x, psi + E, label=f'n = {n} (E = {energias[n-1]:.2f})')

plt.title("Funciones de onda y niveles de energía - Pozo Cuántico Infinito")
plt.xlabel("Posición x")
plt.ylabel("ψ_n(x) + E_n")
plt.axhline(0, color='black', linewidth=1)
plt.legend(loc='upper right')
plt.grid(True, linestyle='--', alpha=0.6)
plt.show()
