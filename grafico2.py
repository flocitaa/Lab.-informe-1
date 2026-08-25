import matplotlib.pyplot as plt

#datos
Fuentes_de_energia= ['Solar', 'Eólica', 'Hidroeléctrica', 'Térmica', 'Geotérmica']
Generacion_GWh= [850, 1200, 950, 600, 310]
#composicion del grafico
plt.bar(Fuentes_de_energia, Generacion_GWh, color=['indigo', 'darkmagenta', 'indigo', 'darkmagenta', 'indigo'])

plt.title('Capacidad de generacion eléctrica según fuente energética')
plt.xlabel('Fuentes de energía')
plt.ylabel('Generación GWh')

plt.grid(axis='y', linestyle='--')  
plt.show()
 
