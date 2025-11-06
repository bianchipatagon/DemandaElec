import numpy as N
import matplotlib.pyplot as plt
from datetime import datetime
import pandas as pd
import seaborn as sns
from scipy.stats import spearmanr
from matplotlib.ticker import MultipleLocator

cld = pd.read_csv('/home/emi/Documents/MAESTRIA/14-Metodología/DemandaElec/DATOS/prueba_cld.txt', header=None, delimiter=',', na_values='-99')
cld.index = pd.date_range(start="2021-01-01 00:00:00", end="2023-12-31  23:00:00",freq="H")
cld = cld.resample('D').sum()
#sacarle los dias de la semana
#graficar tambien curva diaria para enero, abril, julio y octubre
cld = cld.rolling(window=14).mean()
# ~ print(cld)
cld_daily = cld.groupby(cld.index.dayofyear).mean()
fig, ax = plt.subplots(1,1,figsize=(20, 15))
ax.plot(cld_daily.index, cld_daily[2])
plt.savefig('average.svg', dpi=300, bbox_inches="tight")


