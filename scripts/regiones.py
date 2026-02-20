import pandas as pd
import seaborn as sn
import matplotlib.pyplot as plt
import numpy as np
import os

regiones = pd.read_csv('/home/emi/Documents/MAESTRIA/14-Metodología/DemandaElec/scripts/demanda_region.txt',header=0, delimiter = ',')

corr_matrix = regiones.corr()

# 2. Plot with seaborn
plt.figure(figsize=(9, 7))

sn.heatmap(
    corr_matrix,
    annot=True,          # Show correlation values in each cell
    fmt=".2f",           # Format to 2 decimal places
    cmap="coolwarm",     # Color palette (-1 = blue, 0 = white, +1 = red)
    vmin=-1, vmax=1,     # Fix scale to correlation range
    square=True,         # Keep cells square
    linewidths=0.5,      # Add grid lines
    cbar_kws={"shrink": 0.8}
)

plt.savefig('regiones.png',dpi = 600,bbox_inches="tight")
plt.show()
