
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Problema 3: Juegos
# Nombre, copias vendidas en millones, es multijugador, año de lanzamiento

mc = ['Minecraft', 300, True, 2011]
gta = ['GTA V', 190, True, 2013]
tet = ['Tetris', 100, False, 1984]
wii = ['Wii Sports', 82.9, True, 2006]
pub = ['PUBG', 75, True, 2017]

# creamos una lista de listas
lista_juegos = [mc, gta, tet, wii, pub]

# organizamos la tabla utilizando pandas
df_juegos = pd.DataFrame(lista_juegos, columns=[
    "nombre", "copias_vendidas", "es_multijugador", "año_lanzamiento"
])

print(df_juegos)

# creamos el archivo csv
df_juegos.to_csv("juegos.csv", index=False)

# crear grafica de lineas
plt.plot(df_juegos["nombre"], df_juegos["copias_vendidas"])
plt.title("grafica de juegos 0142")
plt.xlabel("nombre de los juegos")
plt.ylabel("copias vendidas en millones")
plt.show()

# crear grafica de puntos
plt.scatter(df_juegos["nombre"], df_juegos["copias_vendidas"])
plt.title("juegos 0142")
plt.xlabel("nombre de los juegos")
plt.ylabel("copias vendidas en millones")
plt.show()

# grafica de barras
plt.bar(df_juegos["nombre"], df_juegos["copias_vendidas"])

# etiquetas y titulo
plt.title("juegos 0142")
plt.xlabel("nombre de los juegos")
plt.ylabel("copias vendidas en millones")

# mostrar la grafica
plt.show()

# ordenar la grafica de barras de manera descendente
# del juego mas vendido al menos vendido
df_juegos_ordenar = df_juegos.sort_values(
    "copias_vendidas", ascending=False
)

plt.bar(df_juegos_ordenar["nombre"], df_juegos_ordenar["copias_vendidas"])
plt.title("juegos mas vendidos 0142")
plt.xlabel("nombre de los juegos")
plt.ylabel("copias vendidas en millones")
plt.show()

# coloreando la grafica
plt.bar(
    df_juegos_ordenar["nombre"],
    df_juegos_ordenar["copias_vendidas"],
    color=["b", "g", "c", "m", "y"]
)
plt.title("juegos mas vendidos 0142")
plt.xlabel("nombre de los juegos")
plt.ylabel("copias vendidas en millones")
plt.show()

# grafica de pastel
plt.pie(
    df_juegos["copias_vendidas"],
    labels=df_juegos["nombre"],
    autopct="%1.1f%%"
)
plt.title("ventas de videojuegos 0142")
plt.show()
