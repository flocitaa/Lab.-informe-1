import matplotlib.pyplot as plt
import numpy as np
#datos
experiencia = np.array([1, 2, 3, 5, 6, 8, 10, 12])
salario  = np.array([1200, 1350, 1500, 1900, 2100, 2600, 3100, 3400])

#grafico
plt.scatter(experiencia, salario, color='purple', label='Salario real')

coeficientes= np.polyfit(experiencia, salario, 1)
linea_de_tendencia = np.poly1d(coeficientes)

plt.plot(experiencia, linea_de_tendencia(experiencia), color='indigo', linestyle='--', label='Tendencia Lineal')

plt.title('Relacion entre años de experiencia y salario mensual')
plt.xlabel('Experiencia (Años)')
plt.ylabel('Salario (USD)')

plt.grid(True,linestyle=':')
plt.legend()

plt.show()
