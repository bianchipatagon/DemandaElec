import numpy as N
import matplotlib.pyplot as plt
from datetime import datetime
import pandas as pd
import seaborn as sns
from scipy.stats import spearmanr
from matplotlib.ticker import MultipleLocator


dire = pd.read_csv('/home/emi/Documents/MAESTRIA/14-Metodología/DemandaElec/DATOS/prueba_dir.txt', header=None, delimiter=',', na_values='-99')
dire.index = pd.date_range(start="2021-01-01 00:00:00", end="2023-12-31  23:00:00",freq="H")

# nos quedamos con los dias de la semana
# ~ cld = cld.loc[(cld[1] == 1) | (cld[1] == 2) | (cld[1] == 3) | (cld[1] == 4) | (cld[1] == 5)]

bins = [-22.5, 22.5, 67.5, 112.5, 157.5, 202.5, 247.5, 292.5, 337.5]
labels = ['N', 'NE', 'E', 'SE', 'S', 'SO', 'O', 'NO']


dire['wind_deg_adjusted'] = dire[3].apply(lambda x: x - 360 if x > 337.5 else x)
print(dire)
# Discretize into 8 directions
# ~ dire['wind_direction'] = pd.cut(dire['wind_deg_adjusted'], bins=bins,labels=labels,include_lowest=True)
dire['wind_direction'] = pd.cut(dire['wind_deg_adjusted'], bins=bins,labels=labels,include_lowest=True)
print(dire)



fig = plt.figure()
ax = fig.add_subplot(projection='polar')
c = ax.scatter(dire['wind_direction'], dire[2])
