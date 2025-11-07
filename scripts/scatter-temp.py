import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from matplotlib.dates import DateFormatter
# ~ import pymannkendall as mk
import seaborn as sns
from scipy import stats
from statsmodels.tsa.seasonal import STL
import pickle
from matplotlib import cm


## demanda
demarg = pd.read_csv('/home/emi/Documents/MJO/datos/demanda/arg-dem.txt', header=None, delimiter=';', na_values='-99')
# ~ demuru = pd.read_csv('/home/emi/Documents/MJO/datos/demanda/uru-dem.txt', header=None, delimiter=';', na_values='-99')
# ~ demchi = pd.read_csv('/home/emi/Documents/MJO/datos/demanda/chi-dem3.txt', header=None, delimiter=';', na_values='-99')

## temperatura
temparg = pd.read_csv('/home/emi/Documents/MJO/datos/demanda/temp-arg.txt', header=None, delimiter=';', na_values='-99')
# ~ tempuru = pd.read_csv('/home/emi/Documents/MJO/datos/demanda/temp-uru.txt', header=None, delimiter=';', na_values='-99')
# ~ tempchi = pd.read_csv('/home/emi/Documents/MJO/datos/demanda/temp-chi.txt', header=None, delimiter=';', na_values='-99')
# ~ print(tempchi[3])
# ~ '''
## indice mjo (para sacar dia de la semana)
mjoarg = pd.read_csv('/home/emi/Documents/MJO/datos/mjo/WH2007.txt', header=None, delimiter=',', na_values='-99')
# ~ mjouru = pd.read_csv('/home/emi/Documents/MJO/datos/mjo/WH2011.txt', header=None, delimiter=',', na_values='-99')
# ~ mjochi = pd.read_csv('/home/emi/Documents/MJO/datos/mjo/WH2014.txt', header=None, delimiter=',', na_values='-99')

## nubosidad
with open('/home/emi/Dropbox/DTEC/MJO/merra/data/cldtot.pkl', 'rb') as file:
    data = pickle.load(file)

# ~ cld_uru = pd.DataFrame()
cld_arg = pd.DataFrame()
# ~ cld_chi = pd.DataFrame()

# ~ cld_uru = data[0]
cld_arg = data[1]
# ~ cld_chi = data[2]

# ~ cld_uru.index = pd.date_range(start="2000-01-01", end="2024-08-01",freq='D')
cld_arg.index = pd.date_range(start="2000-01-01", end="2024-08-01",freq='D')
# ~ cld_chi.index = pd.date_range(start="2000-01-01", end="2024-08-01",freq='D')

# ~ cld_uru = cld_uru.truncate(before=pd.Timestamp("2011-01-01"), after=pd.Timestamp("2022-12-31"))
cld_arg = cld_arg.truncate(before=pd.Timestamp("2007-01-01"), after=pd.Timestamp("2022-12-31"))
# ~ cld_chi = cld_chi.truncate(before=pd.Timestamp("2016-01-01"), after=pd.Timestamp("2022-12-31"))

## Argentina
seriesA = pd.DataFrame()

seriesA[0] = mjoarg[1] # mes
seriesA[1] = mjoarg[3] # dia de la semana
seriesA[2] = demarg[3] # demanda

### removemos tendencia demanda
stl = STL(seriesA[2], seasonal=13, period = 365, robust=True) 
result = stl.fit()
original_mean = seriesA[2].mean()
seriesA[2] = seriesA[2] - result.trend + original_mean

seriesA[3] = temparg[3] # temp
seriesA[4] = cld_arg.values

# sacamos los fines de semana
seriesA = seriesA.loc[(seriesA[1] == 1) | (seriesA[1] == 2) | (seriesA[1] == 3) | (seriesA[1] == 1) | (seriesA[1] == 5)]

# VERANO
verA = seriesA.loc[(seriesA[0] == 1) | (seriesA[0] == 2) | (seriesA[0] == 12)]
# hay que convertir a float
tverA = verA[3].values
dverA = verA[2].values
cverA = verA[4].values

float_tverA = [float(string) for string in tverA]
float_dverA = [float(string) for string in dverA]
float_cverA = [float(string) for string in cverA]

# OTOÑO
otoA = seriesA.loc[(seriesA[0] == 3) | (seriesA[0] == 4) | (seriesA[0] == 5)]
# hay que conototir a float
totoA= otoA[3].values
dotoA = otoA[2].values
float_totoA = [float(string) for string in totoA]
float_dotoA = [float(string) for string in dotoA]

# INVIERNO
invA = seriesA.loc[(seriesA[0] == 6) | (seriesA[0] == 7) | (seriesA[0] == 8)]
# hay que coninvtir a float
tinvA = invA[3].values
dinvA = invA[2].values
float_tinvA = [float(string) for string in tinvA]
float_dinvA = [float(string) for string in dinvA]

# primavera
priA = seriesA.loc[(seriesA[0] == 9) | (seriesA[0] == 10) | (seriesA[0] == 11)]
# hay que convertir a float
tpriA = priA[3].values
dpriA = priA[2].values
float_tpriA = [float(string) for string in tpriA]
float_dpriA = [float(string) for string in dpriA]



# GRAFICO
fig, (ax1,ax2,ax3,ax4) = plt.subplots(1, 4,figsize=(9,2),sharey=True)
sns.set(font_scale = 2)

# PRIMER FILA; ARGENTINA

# Normalize the third variable for colormap
norm = plt.Normalize(vmin=cverA.min(), vmax=cverA.max())
colors = cm.viridis(norm(cverA))
##### ver
kdeplot = sns.regplot(ax=ax1,x = float_tverA, y = float_dverA, scatter_kws = { "alpha": 0.6, 's': 8},line_kws = {"color": "black",'lw': 1}, ci= None, label=None)

r = np.corrcoef(float_tverA, float_dverA)
ax1.tick_params(labelsize=14)
# ~ ax1.text(16.2, 520,'r=', fontsize=15)
# ~ ax1.text(18.2, 520, round(r[0, 1], 2), fontsize=15)
ax1.set_title('DEF', fontsize = 13, weight='bold')
ax1.set_ylim(200, 570)
ax1.set_ylabel('[MWh]', fontsize=15)
ax1.set_yticks([300,400,500])

##### oto
kdeplot = sns.regplot(ax=ax2,x=float_totoA, y = float_dotoA, order=2, scatter_kws = {"alpha": 0.6, 's': 8}, line_kws = {"color": "black",'lw': 1}, ci= None, label=None)
r = np.corrcoef(float_totoA, float_dotoA)
ax2.tick_params(labelsize=14)
ax2.set_title('MAM', fontsize = 13, weight='bold')

# ~ ax2.text(-2.4, 185,'r=', fontsize=15)
# ~ ax2.text(-1.8, 185, round(r[0, 1], 2), fontsize=15)
ax2.set_ylim(200, 570)

##### inv
kdeplot = sns.regplot(ax=ax3,x=float_tinvA, y = float_dinvA, scatter_kws = {"alpha": 0.5, 's': 8}, line_kws = {"color": "black",'lw': 1}, ci= None, label=None)
r = np.corrcoef(float_tinvA, float_dinvA)
ax3.tick_params(labelsize=13)
# ~ ax3.text(15.5, 520,'r=', fontsize=15)
# ~ ax3.text(18, 520, round(r[0, 1], 2), fontsize=15)
ax3.set_ylim(200, 570)
ax3.set_title('JJA', fontsize = 14, weight='bold')

##### pri
kdeplot = sns.regplot(ax=ax4,x=float_tpriA, y = float_dpriA, order=2, scatter_kws = { "alpha": 0.5, 's': 8}, line_kws = {"color": "black",'lw': 1}, ci= None, label=None)
r = np.corrcoef(float_tpriA,float_dpriA)
ax4.tick_params(labelsize=13)
# ~ ax4.text(-2.4, 350,'r=', fontsize=15)
# ~ ax4.text(-1.8, 350, round(r[0, 1], 2), fontsize=15)
ax4.set_ylim(200, 570)
ax4.set_title('SON', fontsize = 14, weight='bold')


fig.subplots_adjust(hspace=0.2,wspace=0.25)
fig.text(0.45, -0.15, 'temperatura [°c]', fontsize = 15)
fig.subplots_adjust(wspace=0.1)


# ~ fig.subplots_adjust(bottom=0.13)
# ~ fig.subplots_adjust(left=0.15)

plt.savefig('scatter_temp.jpg', dpi=300, bbox_inches="tight")
# ~ plt.show()
