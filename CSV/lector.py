import csv 
import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv('Data.csv')
pts = df['PTS']
print('Promedio de Puntos: ', pts.mean())
print('Varianza de Puntos: ', pts.var())
print('Desviación estandar de Puntos: ', pts.std())
print('Curtosis de Puntos: ', pts.kurt())
print('Asimetria: ', pts.skew())

plt.hist(pts, bins = 100)
plt.show()