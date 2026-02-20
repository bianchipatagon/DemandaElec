import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import numpy as np
import pandas as pd

df = pd.read_csv('/home/emi/Documents/MAESTRIA/14-Metodología/DemandaElec/DATOS/arg-dem.txt', header=None, delimiter=';')
df.index= pd.date_range(start='2007-01-01', end='2022-12-31', freq = 'D')

df1 = pd.read_csv('/home/emi/Documents/MAESTRIA/14-Metodología/DemandaElec/DATOS/semana.txt', header=None, delimiter=';')
df1.index= pd.date_range(start='2021-11-29 00:00:00', end='2021-12-05 23:00:00', freq = 'H')

cld = pd.read_csv('/home/emi/Documents/MAESTRIA/14-Metodología/DemandaElec/DATOS/prueba_cld.txt', header=None, delimiter=',', na_values='-99')
cld.index = pd.date_range(start="2021-01-01 00:00:00", end="2023-12-31  23:00:00",freq="H")
# nos quedamos con los dias de la semana
cld = cld.loc[(cld[1] == 1) | (cld[1] == 2) | (cld[1] == 3) | (cld[1] == 4) | (cld[1] == 5)]
print(cld)
hora = cld.groupby(cld.index.hour).mean()
print(hora)
# julio
cld_jul = cld[cld.index.month == 7]
horaJ = cld_jul.groupby(cld_jul.index.hour).mean()

# diciembre
cld_dic = cld[cld.index.month == 12]
horaD = cld_dic.groupby(cld_dic.index.hour).mean()

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
ax3.set_ylabel('[GW]')

ax4.plot(hora.index, hora[2]/1000, alpha = 0.8, label= 'anual')
ax4.plot(horaJ.index, horaJ[2]/1000, alpha = 0.8, color='purple',label= 'invierno' )
ax4.plot(horaD.index, horaD[2]/1000, alpha = 0.8, color='tomato',label= 'verano')
ax4.set_ylabel('[GW]')
ax4.set_title('d) 1 dia')
ax4.set_xticks([4,8,12,16,20], ['04:00','08:00','12:00','16:00','20:00'])
ax4.set_xlim(0, 23)
ax4.legend( frameon=False,bbox_to_anchor=(0.6, 0.5), borderaxespad=0.,fontsize=6)

# ~ start_date = pd.to_datetime('2021-11-29')
# ~ end_date = pd.to_datetime('2021-11-30')
# ~ ax4.set_xlim(start_date, end_date)
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
