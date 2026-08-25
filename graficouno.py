import matplotlib.pyplot as plt


#datos
Salario_USD = [1200, 1350, 1500, 1900, 2100, 2600, 3100, 3400]
Experiencia_Anios = [1, 2, 3, 5, 6, 8, 10, 12]

plt.scatter(Salario_USD, Experiencia_Anios, color="darkblue", s=80, edgecolors="black")

plt.xlim(1000, 3600)

plt.title("Relación entre Salario y Experiencia")
plt.xlabel("Salario (USD)")
plt.ylabel("Experiencia (Años)")

plt.grid(True, linestyle='--', alpha=0.5)

plt.show()
