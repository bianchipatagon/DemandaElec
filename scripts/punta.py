import numpy as N
import matplotlib.pyplot as plt
from datetime import datetime
import pandas as pd
import seaborn as sns
from scipy.stats import spearmanr
from matplotlib.ticker import MultipleLocator

df = pd.read_csv('/home/emi/Documents/MAESTRIA/14-Metodología/DemandaElec/DATOS/prueba_v.txt', header=None, delimiter=',', na_values='-99')
df.index = pd.date_range(start="2021-01-01 00:00:00", end="2023-12-31  23:00:00",freq="H")
# ~ printE(df)
### JULIO
df_7 = df[df.index.month == 12]
df_7 = df_7.loc[(df_7[2] == 1) | (df_7[2] == 2) | (df_7[2] == 3) | (df_7[2] == 4) | (df_7[2] == 5)]
tem_7 = round(0.81*df_7[7] + 0.1*df_7[8] + 0.09*df_7[9],0)
cld_7 = round(0.81*df_7[4] + 0.1*df_7[5] + 0.09*df_7[6],0)
dem_7 = df_7[3]
############ punta
dem_7_max = dem_7.resample('D').max()
dem_7_min = dem_7.resample('D').min()
punta = dem_7_max - dem_7_min
############ Tmax
tem_7_max = tem_7.resample('D').max()
############ Tmin
tem_7_min = tem_7.resample('D').min()
############ Tmed
tem_7_med = tem_7.resample('D').mean()
############ deltaT
deltaT_7 = tem_7_max-tem_7_min 
############ nubosidad
cld_7_med = cld_7.resample('D').mean()
############ nubosidad noct
noct_7 = cld_7[cld_7.index.hour.isin([1,2,3,4,5,6,7,20,21,22,23,24])]
cld_7_noc = noct_7.resample('D').mean()
############ nubosidad diur
diu_7 = cld_7[cld_7.index.hour.isin([8,9,10,11,12,13,14,15,16,17,18,19])]
cld_7_diu = diu_7.resample('D').mean()


X = [1,2,3,4,5,6,7]
colors = ["tomato","tomato","tomato","tomato","dimgrey","dimgrey","dimgrey"]
# ~ corr_7 = [N.corrcoef(punta,tem_7_min)[0, 1],N.corrcoef(punta,tem_7_max)[0, 1],N.corrcoef(punta,tem_7_med)[0, 1],N.corrcoef(punta,deltaT)[0, 1],N.corrcoef(punta,cld_7_med)[0, 1],N.corrcoef(punta,cld_7_noc)[0, 1],N.corrcoef(punta,cld_7_diu)[0, 1]]
corr_7 = [punta.corr(tem_7_max),punta.corr(tem_7_min),punta.corr(tem_7_med),punta.corr(deltaT_7),punta.corr(cld_7_med),punta.corr(cld_7_noc),punta.corr(cld_7_diu)]
fig, ax = plt.subplots(1, 1,figsize=(2,2), sharex=True, sharey=True)
print(corr_7)
ax.bar(X, corr_7, width=1, edgecolor="white", linewidth=0.7 , alpha = 0.8, color=colors)
ax.tick_params(axis='y', labelsize=13)
ax.tick_params(axis='x', labelsize=13, labelrotation = 90)

ax.set_ylim(-1,1)
ax.set_yticks([-0.5, 0, 0.5]) 
# ~ ax.xaxis.set_tick_params(labelsize=0, color='white')
# ~ ax1.text(0.5, 0.5, 'abril', fontsize=15)
ax.axhline(linewidth=1, color='black')
ax.set_xticks([1,2,3,4,5,6,7], [r'$T_{max}$',r'$T_{min}$',r'$\bar{T}$','\u0394T',r'$\bar{CLD}$',r'$CLD_{noct}$',r'$CLD_{diu}$'])
for label, color in zip(ax.get_xticklabels(), colors):
    label.set_color(color)
plt.savefig('punta.jpg', dpi=300, bbox_inches="tight")
