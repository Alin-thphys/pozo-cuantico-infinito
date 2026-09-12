# Simulación de un Pozo Cuántico Infinito

Primer proyecto de física teórica y computacional: modelado de los niveles de energía y funciones de onda para una partícula en un pozo de potencial unidimensional infinito.

## Fundamento Teórico

Para una partícula de masa $m$ confinada en un pozo de potencial unidimensional de ancho $L$ tal que:

$$V(x) = \begin{cases} 0 & \text{si } 0 < x < L \\ \infty & \text{en cualquier otro caso} \end{cases}$$

La ecuación independiente del tiempo de Schrödinger se resuelve analíticamente. Los niveles de energía permitidos están dados por:

$$E_n = \frac{n^2 \pi^2 \hbar^2}{2 m L^2}, \quad n = 1, 2, 3, \dots$$

Y las funciones de onda normalizadas correspondientes son:

$$\psi_n(x) = \sqrt{\frac{2}{L}} \sin\left(\frac{n \pi x}{L}\right)$$

## Contenido del Repositorio

* `pozo_cuantico.py`: Script en Python utilizando `numpy` y `matplotlib` para calcular las energías discretas y graficar el comportamiento de las funciones de onda desplazadas según su nivel energético.
