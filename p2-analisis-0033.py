# Keyla Paola NC = 0033 | Fecha 6/noviembre/2026
# imoportar librerias
import pandas as pd
import numpy as np
# 1. Crear el DataFrame con tus datos
inmuebles = {
    "Id_Casa": [101, 102, 103, 104, 105, 106],
    "Metros_Cuadrados": [65, 120, 85, 200, 150, 95],
    "Habitaciones": [2, 4, 3, 5, 4, 3],
    "Precio_Miles_USD": [150, 310, 210, 480, 390, 240]
}

df = pd.DataFrame(inmuebles)
print(df)
# --- Agrupar por 'Habitaciones' ---
grouped = df.groupby('Habitaciones')
print("Objeto GroupBy:")
print(grouped)

# --- Pasos de Agregación ---
print("\n--- Promedio de Metros Cuadrados por cantidad de habitaciones Keyla Paola NC = 0033 ---")
print(grouped['Metros_Cuadrados'].mean())

print("\n--- Precio Máximo por cantidad de habitaciones Keyla Paola NC = 0033 ---")
print(grouped['Precio_Miles_USD'].max())

print("Keyla Paola NC = 0033 | Fecha 6/noviembre/2026)")