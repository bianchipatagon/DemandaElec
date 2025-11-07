import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import numpy as np
import pandas as pd

df = pd.read_csv('/home/emi/Documents/MAESTRIA/14-Metodología/DemandaElec/DATOS/arg-dem.txt', header=None, delimiter=';')
df.index= pd.date_range(start='2007-01-01', end='2022-12-31', freq = 'D')

df1 = pd.read_csv('/home/emi/Documents/MAESTRIA/14-Metodología/DemandaElec/DATOS/semana.txt', header=None, delimiter=';')
df1.index= pd.date_range(start='2021-11-29 00:00:00', end='2021-12-05 23:00:00', freq = 'H')
print(df1)
# Create figure and GridSpec
fig = plt.figure(figsize=(7, 4))
gs = gridspec.GridSpec(2, 3, figure=fig)

# Top subplot spans all 3 columns
ax1 = fig.add_subplot(gs[0, :])

# Bottom subplots
ax2 = fig.add_subplot(gs[1, 0])
ax3 = fig.add_subplot(gs[1, 1])
ax4 = fig.add_subplot(gs[1, 2])

# Example plots
ax1.plot(df.index, df[3], linewidth=0.5, alpha = 0.8)
# ~ ax1.fill_between(df.index, df[3], color='skyblue', alpha=0.4, label='Area under curve')

ax1.set_title('a) Período completo')
ax1.set_ylabel('[GWh]')
start_date = pd.to_datetime('2007-01-01')
end_date = pd.to_datetime('2022-12-31')
ax1.set_xlim(start_date, end_date)

ax2.plot(df.index, df[3], linewidth=0.75, alpha = 0.8)
ax2.set_title('b) 1 año')
start_date = pd.to_datetime('2021-01-10')
end_date = pd.to_datetime('2021-12-31')
ax2.set_xlim(start_date, end_date)
ax2.tick_params(axis='x', labelrotation = 90, labelsize=11)
ax2.set_ylabel('[GWh]')

ax3.plot(df1.index, df1[1], alpha = 0.8)
ax3.set_title('c) 1 semana')
start_date = pd.to_datetime('2021-11-29')
end_date = pd.to_datetime('2021-12-05')
ax3.set_xlim(start_date, end_date)
ax3.tick_params(axis='x', labelrotation = 90, labelsize=11)

ax4.plot(df1.index, df1[1], alpha = 0.8)
ax4.set_title('d) 1 dia')
start_date = pd.to_datetime('2021-11-29')
end_date = pd.to_datetime('2021-11-30')
ax4.set_xlim(start_date, end_date)
ax4.tick_params(axis='x', labelrotation = 90, labelsize=11)

'''
ax_bottom1.plot(x, np.cos(x))
ax_bottom1.set_title('Bottom Left')

ax_bottom2.plot(x, np.sin(2*x))
ax_bottom2.set_title('Bottom Center')

ax_bottom3.plot(x, np.cos(2*x))
ax_bottom3.set_title('Bottom Right')
'''
# ~ fig.text(0.003, 0.5, '[GWh]', rotation='vertical')
plt.tight_layout()
plt.savefig('multi.png',bbox_inches="tight", dpi=600)
# ~ plt.show()
