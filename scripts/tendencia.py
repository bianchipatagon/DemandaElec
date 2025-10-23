import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from statsmodels.tsa.seasonal import STL

df = pd.read_csv('/home/emi/Documents/MAESTRIA/14-Metodología/DATOS/arg-dem.txt', header=None, delimiter=';')
df.index= pd.date_range(start='2007-01-01', end='2022-12-31', freq = 'D')
print(df)
'''
df2 = pd.read_csv('/home/emi/Documents/MAESTRIA/14-Metodología/DATOS/PBI3M.txt', header=None, delimiter=';')
df2.index= pd.date_range(start='2007-01-01', end='2022-12-31', freq = '3M')
print(df2)
'''
df2 = pd.read_csv('/home/emi/Documents/MAESTRIA/14-Metodología/DATOS/PBI.txt', header=None, delimiter=';')
df2.index= pd.date_range(start='2007-01-01', end='2022-12-31', freq = 'Y')
print(df2)

stl = STL(df[3], seasonal=13, period = 365, robust=True) 
result = stl.fit()

# Plot the decomposition components
fig, (ax1, ax2, ax3, ax4) = plt.subplots(4, 1, figsize=(7, 4), sharex=True)

ax1.plot(df.index, df[3].rolling(window=3).mean(), color='black', linewidth=0.5)
ax1.set_title('a) Demanda')
start_date = pd.to_datetime('2007-01-01')
end_date = pd.to_datetime('2022-12-31')
ax1.set_xlim(start_date, end_date)

ax2.plot(df.index, result.trend, label='Trend',  color='black')
ax2.set_ylim([300,420])
ax2.set_title('b) Componente de tendencia + PBI')
ax2.set_xlim(start_date, end_date)

ax5 = ax2.twinx()
ax5.plot(df2.index, df2[1]/1000000000,'bo', markersize=4)
ax5.spines['right'].set_color('blue')
ax5.tick_params(axis='y', colors='blue')
ax5.set_ylabel('PBI [MMU$D]', color = 'blue')
# ~ ax5.set_ylim([250000,680000])

ax3.plot(df.index, result.seasonal.rolling(window=3).mean(), label='Seasonal',  color='black', linewidth=0.5)
ax3.set_title('c) Componente estacional')
ax3.set_xlim(start_date, end_date)

ax4.plot(df.index, result.resid.rolling(window=3).mean(), label='Residual', color='black', linewidth=0.5)
ax4.set_title('d) Residual')
ax4.set_xlim(start_date, end_date)

fig.text(0.008, 0.45, '[GWh]', rotation='vertical')
fig.subplots_adjust(hspace=0.1)

plt.tight_layout()
plt.savefig('decomp.png',bbox_inches="tight", dpi=600)

st = df[3] - result.trend
st = st.resample("M").mean()

st.to_csv('/home/emi/Documents/MAESTRIA/14-Metodología/DATOS/dem-st.txt', index=False)  

# ~ plt.show()

