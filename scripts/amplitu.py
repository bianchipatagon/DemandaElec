import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import numpy as np
import pandas as pd



cld = pd.read_csv('/home/emi/Documents/MAESTRIA/14-Metodología/DemandaElec/DATOS/prueba_cld.txt', header=None, delimiter=',', na_values='-99')
cld.index = pd.date_range(start="2021-01-01 00:00:00", end="2023-12-31  23:00:00",freq="H")
# nos quedamos con los dias de la semana
cld = cld.loc[(cld[1] == 1) | (cld[1] == 2) | (cld[1] == 3) | (cld[1] == 4) | (cld[1] == 5)]
# ~ print(cld)
hora = cld.groupby(cld.index.hour).mean()
print(hora)
# julio
cld_jul = cld[cld.index.month == 7]
horaJ = cld_jul.groupby(cld_jul.index.hour).mean()

# diciembre
cld_dic = cld[cld.index.month == 12]
horaD = cld_dic.groupby(cld_dic.index.hour).mean()
# ~ print(horaD)
fig, ax = plt.subplots(1,1,figsize=(3,2), sharey=True)

ax.plot(hora.index, hora[2]/1000, alpha = 0.8, linewidth = 2)
# ~ ax4.plot(horaJ.index, horaJ[2]/1000, alpha = 0.8, color='purple')
# ~ ax4.plot(horaD.index, horaD[2]/1000, alpha = 0.8, color='tomato')
ax.set_ylabel('[GW]')
# ~ ax4.set_title('d) 1 dia')
ax.set_xticks([4,8,12,16,20], ['04:00','08:00','12:00','16:00','20:00'])
ax.set_xlim(0, 23)

plt.plot([4, 4], [13.32, 18.6], color='red')
plt.plot([3.2, 4.8], [13.32, 13.32], color='red')
plt.plot([3.2, 4.8], [18.6, 18.6], color='red')
plt.plot([4, 20], [18.6, 18.6], color='red', linestyle='--')

ax.tick_params(axis='x', labelrotation = 90, labelsize=11)

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
plt.savefig('ampli.png',bbox_inches="tight", dpi=600)
# ~ plt.show()
