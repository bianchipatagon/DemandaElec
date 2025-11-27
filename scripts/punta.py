import numpy as N
import matplotlib.pyplot as plt
from datetime import datetime
import pandas as pd
import seaborn as sns
from scipy.stats import spearmanr
from matplotlib.ticker import MultipleLocator

df = pd.read_csv('/home/emi/Documents/MAESTRIA/14-Metodología/DemandaElec/DATOS/prueba_v.txt', header=None, delimiter=',', na_values='-99')
df.index = pd.date_range(start="2021-01-01 00:00:00", end="2023-12-31  23:00:00",freq="H")

### ABRIL
df_4 = df[df.index.month == 4]
df_4 = df_4.loc[(df_4[2] == 1) | (df_4[2] == 2) | (df_4[2] == 3) | (df_4[2] == 4) | (df_4[2] == 5)]
tem_4 = round(0.81*df_4[7] + 0.1*df_4[8] + 0.09*df_4[9],0)
cld_4 = round(0.81*df_4[4] + 0.1*df_4[5] + 0.09*df_4[6],0)
dem_4 = df_4[3]
############ punta
dem_4_max = dem_4.resample('D').max()
dem_4_min = dem_4.resample('D').min()
punta_4 = dem_4_max - dem_4_min
############ Tmax
tem_4_max = tem_4.resample('D').max()
############ Tmin
tem_4_min = tem_4.resample('D').min()
############ Tmed
tem_4_med = tem_4.resample('D').mean()
############ deltaT
deltaT_4 = tem_4_max-tem_4_min 
############ nubosidad
cld_4_med = cld_4.resample('D').mean()
############ nubosidad noct
noct_4 = cld_4[cld_4.index.hour.isin([1,2,3,4,5,20,21,22,23,24])]
cld_4_noc = noct_4.resample('D').mean()
############ nubosidad diur
diu_4 = cld_4[cld_4.index.hour.isin([6,7,8,9,10,11,12,13,14,15,16,17,18,19])]
cld_4_diu = diu_4.resample('D').mean()

### JULIO
df_7 = df[df.index.month == 7]
df_7 = df_7.loc[(df_7[2] == 1) | (df_7[2] == 2) | (df_7[2] == 3) | (df_7[2] == 4) | (df_7[2] == 5)]
tem_7 = round(0.81*df_7[7] + 0.1*df_7[8] + 0.09*df_7[9],0)
cld_7 = round(0.81*df_7[4] + 0.1*df_7[5] + 0.09*df_7[6],0)
dem_7 = df_7[3]
############ punta
dem_7_max = dem_7.resample('D').max()
dem_7_min = dem_7.resample('D').min()
punta_7 = dem_7_max - dem_7_min
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
noct_7 = cld_7[cld_7.index.hour.isin([1,2,3,4,5,6,7,8,18,19,20,21,22,23,24])]
cld_7_noc = noct_7.resample('D').mean()
############ nubosidad diur
diu_7 = cld_7[cld_7.index.hour.isin([9,10,11,12,13,14,15,16,17])]
cld_7_diu = diu_7.resample('D').mean()

### OCTUBRE
df_10 = df[df.index.month == 9]
df_10 = df_10.loc[(df_10[2] == 1) | (df_10[2] == 2) | (df_10[2] == 3) | (df_10[2] == 4) | (df_10[2] == 5)]
tem_10 = round(0.81*df_10[7] + 0.1*df_10[8] + 0.09*df_10[9],0)
cld_10 = round(0.81*df_10[4] + 0.1*df_10[5] + 0.09*df_10[6],0)
dem_10 = df_10[3]
############ punta
dem_10_max = dem_10.resample('D').max()
dem_10_min = dem_10.resample('D').min()
punta_10 = dem_10_max - dem_10_min
############ Tmax
tem_10_max = tem_10.resample('D').max()
############ Tmin
tem_10_min = tem_10.resample('D').min()
############ Tmed
tem_10_med = tem_10.resample('D').mean()
############ deltaT
deltaT_10 = tem_10_max-tem_10_min 
############ nubosidad
cld_10_med = cld_10.resample('D').mean()
############ nubosidad noct
noct_10 = cld_10[cld_10.index.hour.isin([1,2,3,4,5,6,7,20,21,22,23,24])]
cld_10_noc = noct_10.resample('D').mean()
############ nubosidad diur
diu_10 = cld_10[cld_10.index.hour.isin([8,9,10,11,12,13,14,15,16,17,18,19])]
cld_10_diu = diu_10.resample('D').mean()

### DICIEMBRA
df_12 = df[df.index.month == 12]
df_12 = df_12.loc[(df_12[2] == 1) | (df_12[2] == 2) | (df_12[2] == 3) | (df_12[2] == 4) | (df_12[2] == 5)]
tem_12 = round(0.81*df_12[7] + 0.1*df_12[8] + 0.09*df_12[9],0)
cld_12 = round(0.81*df_12[4] + 0.1*df_12[5] + 0.09*df_12[6],0)
dem_12 = df_12[3]
############ punta
dem_12_max = dem_12.resample('D').max()
dem_12_min = dem_12.resample('D').min()
punta_12 = dem_12_max - dem_12_min
############ Tmax
tem_12_max = tem_12.resample('D').max()
############ Tmin
tem_12_min = tem_12.resample('D').min()
############ Tmed
tem_12_med = tem_12.resample('D').mean()
############ deltaT
deltaT_12 = tem_12_max-tem_12_min 
############ nubosidad
cld_12_med = cld_12.resample('D').mean()
############ nubosidad noct
noct_12 = cld_12[cld_12.index.hour.isin([1,2,3,4,5,6,20,21,22,23,24])]
cld_12_noc = noct_12.resample('D').mean()
############ nubosidad diur
diu_12 = cld_12[cld_12.index.hour.isin([7,8,9,10,11,12,13,14,15,16,17,18,19])]
cld_12_diu = diu_12.resample('D').mean()

X = [1,2,3,4,5,6,7]
colors = ["tomato","tomato","tomato","tomato","dimgrey","dimgrey","dimgrey"]

corr_4 = [punta_4.corr(tem_4_max),punta_4.corr(tem_4_min),punta_4.corr(tem_4_med),punta_4.corr(deltaT_4),punta_4.corr(cld_4_med),punta_4.corr(cld_4_noc),punta_4.corr(cld_4_diu)]
corr_7 = [punta_7.corr(tem_7_max),punta_7.corr(tem_7_min),punta_7.corr(tem_7_med),punta_7.corr(deltaT_7),punta_7.corr(cld_7_med),punta_7.corr(cld_7_noc),punta_7.corr(cld_7_diu)]
corr_10 = [punta_10.corr(tem_10_max),punta_10.corr(tem_10_min),punta_10.corr(tem_10_med),punta_10.corr(deltaT_10),punta_10.corr(cld_10_med),punta_10.corr(cld_10_noc),punta_10.corr(cld_10_diu)]
corr_12 = [punta_12.corr(tem_12_max),punta_12.corr(tem_12_min),punta_12.corr(tem_12_med),punta_12.corr(deltaT_12),punta_12.corr(cld_12_med),punta_12.corr(cld_12_noc),punta_12.corr(cld_12_diu)]

fig, (ax1,ax2,ax3,ax4) = plt.subplots(1,4,figsize=(8,2), sharex=True, sharey=True)

ax1.bar(X, corr_4, width=1, edgecolor="white", linewidth=0.7 , alpha = 0.8, color=colors)
ax1.tick_params(axis='y', labelsize=13)
ax1.tick_params(axis='x', labelsize=13, labelrotation = 90)
ax1.set_ylim(-1,1)
ax1.set_yticks([-0.5,0, 0.5]) 
ax1.axhline(linewidth=1, color='black')
ax1.axhline(y=0.274,linewidth=0.75, color='black',ls =  '--')
ax1.axhline(y=-0.274,linewidth=0.75, color='black',ls =  '--')

ax1.set_xticks([1,2,3,4,5,6,7], [r'$T_{max}$',r'$T_{min}$',r'$\bar{T}$','\u0394T',r'$\bar{NUB}$',r'$NUB_{noct}$',r'$NUB_{diu}$'])
ax1.set_title('abril', fontsize=13)

ax2.bar(X, corr_7, width=1, edgecolor="white", linewidth=0.7 , alpha = 0.8, color=colors)
ax2.tick_params(axis='y', labelsize=13)
ax2.tick_params(axis='x', labelsize=13, labelrotation = 90)
ax2.set_ylim(-1,1)
ax2.set_yticks([-0.5, 0, 0.5]) 
ax2.axhline(linewidth=1, color='black')
ax2.axhline(y=0.274,linewidth=0.75, color='black',ls =  '--')
ax2.axhline(y=-0.274,linewidth=0.75, color='black',ls =  '--')
ax2.set_xticks([1,2,3,4,5,6,7], [r'$T_{max}$',r'$T_{min}$',r'$\bar{T}$','\u0394T',r'$\bar{NUB}$',r'$NUB_{noct}$',r'$NUB_{diu}$'])
ax2.set_title('julio', fontsize=13)

ax3.bar(X, corr_10, width=1, edgecolor="white", linewidth=0.7 , alpha = 0.8, color=colors)
ax3.tick_params(axis='y', labelsize=13)
ax3.tick_params(axis='x', labelsize=13, labelrotation = 90)
ax3.set_ylim(-1,1)
ax3.set_yticks([-0.5, 0, 0.5]) 
ax3.axhline(linewidth=1, color='black')
ax3.axhline(y=0.274,linewidth=0.75, color='black',ls =  '--')
ax3.axhline(y=-0.274,linewidth=0.75, color='black',ls =  '--')
ax3.set_xticks([1,2,3,4,5,6,7], [r'$T_{max}$',r'$T_{min}$',r'$\bar{T}$','\u0394T',r'$\bar{NUB}$',r'$NUB_{noct}$',r'$NUB_{diu}$'])
ax3.set_title('octubre', fontsize=13)

ax4.bar(X, corr_12, width=1, edgecolor="white", linewidth=0.7 , alpha = 0.8, color=colors)
ax4.tick_params(axis='y', labelsize=13)
ax4.tick_params(axis='x', labelsize=13, labelrotation = 90)
ax4.set_ylim(-1,1)
ax4.set_yticks([-0.5, 0, 0.5]) 
ax4.axhline(linewidth=1, color='black')
ax4.axhline(y=0.274,linewidth=0.75, color='black',ls =  '--')
ax4.axhline(y=-0.274,linewidth=0.75, color='black',ls =  '--')
ax4.set_xticks([1,2,3,4,5,6,7], [r'$T_{max}$',r'$T_{min}$',r'$\bar{T}$','\u0394T',r'$\bar{NUB}$',r'$NUB_{noct}$',r'$NUB_{diu}$'])
ax4.set_title('diciembre', fontsize=13)

for label, color in zip(ax1.get_xticklabels(), colors):
    label.set_color(color)
for label, color in zip(ax2.get_xticklabels(), colors):
    label.set_color(color)
for label, color in zip(ax3.get_xticklabels(), colors):
    label.set_color(color)
for label, color in zip(ax4.get_xticklabels(), colors):
    label.set_color(color)
    
fig.text(.04, 0.5, 'coef. correlación []', va='center', rotation='vertical',fontsize=13)  

plt.savefig('punta.jpg', dpi=300, bbox_inches="tight")
