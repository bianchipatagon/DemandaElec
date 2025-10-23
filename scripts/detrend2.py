from scipy import signal
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import statsmodels.api as sm
from scipy.stats import linregress

# DEMANDA
# Example timeseries
dm = pd.read_csv('/home/emi/Documents/MAESTRIA/14-Metodología/DATOS/arg-dem.txt', header=None, delimiter=';')
dm.index= pd.date_range(start='2007-01-01', end='2022-12-31', freq = 'D')
print(dm)

x = np.arange(len(dm))
y = dm[3].values
# Ajustar una regresión lineal
slope, intercept, r_value, p_value, std_err = linregress(x, y)

# Calcular la tendencia lineal
dm['tendencia'] = intercept + slope * x
dm['col_diff'] = dm[3] - dm['tendencia'] + intercept

dm = dm.resample("M").sum()
print('demanda')
print('dm')

# TEMPERATURA
# Example timeseries
t2 = pd.read_csv('/home/emi/Documents/MAESTRIA/14-Metodología/DATOS/temp-arg.txt', header=None, delimiter=';')
t2.index= pd.date_range(start='2007-01-01', end='2022-12-31', freq = 'D')
print(dm)

x = np.arange(len(t2))
y = t2[3].values
# Ajustar una regresión lineal
slope, intercept, r_value, p_value, std_err = linregress(x, y)

# Calcular la tendencia lineal
t2['tendencia'] = intercept + slope * x
t2['col_diff'] = t2[3] - t2['tendencia'] + intercept

t2 = t2.resample("M").sum()
dm = dm.resample("M").sum()
print('temp')
print(t2)



