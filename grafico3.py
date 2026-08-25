import matplotlib.pyplot as plt

#datos
tiempo = [0, 5, 10, 15, 20, 25, 30]
concentracion = [1.00, 0.78, 0.61, 0.47, 0.37, 0.29, 0.23]

plt.plot(tiempo, concentracion, marker='o', linestyle='-', color='blue', label='concentracion de soluto')

plt.title('Avance de una reaccion quimica')
plt.xlabel('Tiempo(min)')
plt.ylabel('Concentracion (mol/L)')

plt.grid(True)
plt.legend()

plt.show()

