import matplotlib.pyplot as plt
import numpy as np

def dibujar_estrella():
    # Coordenadas de los 5 vértices de la estrella
    angulos = np.linspace(0, 2 * np.pi, 6)[:-1]  # Divide el círculo en 5 partes
    radio_externo = 1
    radio_interno = 0.4  # Radio más pequeño para el cruce interno

    # Coordenadas de los puntos externos (las puntas de la estrella)
    x_externo = radio_externo * np.cos(angulos)
    y_externo = radio_externo * np.sin(angulos)

    # Coordenadas de los puntos internos (los cruces dentro de la estrella)
    angulos_internos = angulos + np.pi / 5  # Rotamos para ubicarlos correctamente
    x_interno = radio_interno * np.cos(angulos_internos)
    y_interno = radio_interno * np.sin(angulos_internos)

    # Orden correcto para unir los puntos en forma de estrella
    x_total = np.empty(10)
    y_total = np.empty(10)
    x_total[::2], y_total[::2] = x_externo, y_externo  # Puntas externas
    x_total[1::2], y_total[1::2] = x_interno, y_interno  # Puntas internas

    # Cerrar la estrella conectando el último punto con el primero
    x_total = np.append(x_total, x_total[0])
    y_total = np.append(y_total, y_total[0])

    # Dibujar la estrella
    plt.plot(x_total, y_total, 'r-')  # Línea roja
    plt.fill(x_total, y_total, 'yellow', edgecolor='black')  # Relleno amarillo
    plt.axis('equal')  # Mantiene la proporción
    plt.axis('off')  # Quita los ejes para que se vea mejor
    plt.show()

dibujar_estrella()
