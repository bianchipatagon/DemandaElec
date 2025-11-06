import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import numpy as np
import pandas as pd
from matplotlib.dates import YearLocator, MonthLocator
from matplotlib.ticker import MultipleLocator

df = pd.read_csv('/home/emi/Documents/MAESTRIA/14-Metodología/DemandaElec/DATOS/arg-dem.txt', header=None, delimiter=';')
df.index= pd.date_range(start='2007-01-01', end='2022-12-31', freq = 'D')
print(df)

result = df.groupby(df.index.year)[3].agg(['min', 'max'])
result['range'] = result['max'] - result['min']
print(result)

fig, ax = plt.subplots(1,1,figsize=(5,4), sharey=True)

# ~ ax.plot(result.index, result['range'], color='black', linewidth=0.5)
ax.bar(result.index, result['range'], width=1, edgecolor="white", linewidth=0.7 , alpha=0.8)
ax.tick_params(axis='x', labelrotation = 90, labelsize=13)
ax.tick_params(axis='y', labelsize=13)
ax.set_ylabel('max-min [GWh]', fontsize=15)
ax.set_ylim(100, 310)

ax = plt.gca()
ax.xaxis.set_major_locator(MultipleLocator(1))  # Tick every 5 units

# ~ ax.set_xticks([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16], ['2007','2008','2009','2010','2011','2012','2013','2014','2015','2016','2017','2018','2019','2020','2021','2022'])
# ~ ax.set_xticks([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16], result.index)
# ~ plt.xticks(x[::1])
plt.tight_layout()
plt.savefig('minmax',bbox_inches="tight", dpi=600)

