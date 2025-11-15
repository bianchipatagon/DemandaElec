import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import numpy as np
import pandas as pd

df = pd.read_csv('/home/emi/Documents/MAESTRIA/14-Metodología/DemandaElec/DATOS/indices.txt', header=None, delimiter=',')
print(df)


df['rolling_3m'] = df[2].rolling(window=3).mean()
### hay que elegir los meses que tienen el promedio de cdad estacion
### o lo hago a nivel mensual para cada uno de las estaciones? voy a tener mas casos...
