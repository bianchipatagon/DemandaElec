import numpy as N
import matplotlib.pyplot as plt
from datetime import datetime
import pandas as pd
from scipy.signal import detrend
import math



Vsam = pd.read_csv('/home/emi/Documents/MJO/datos/AAO/SAM.txt', header=None, delimiter=',', na_values='-99') ### year, month, day, day of week, SAM



#################################
#######DEMANDA####################
#################################

Darg = pd.read_csv('/home/emi/Documents/MJO/datos/demanda/arg-dem-agrup.txt', header=None, delimiter=',', na_values='-9999')

Darg_cruda = pd.read_csv('/home/emi/Documents/MJO/datos/demanda/arg-dem.txt', header=None, delimiter=';')

sam1 = pd.read_csv('/home/emi/Documents/MJO/datos/AAO/SAM2011.txt', header=None, delimiter=',', na_values='-99') ### year, month, day, day of week, SAM
sam2 = pd.read_csv('/home/emi/Documents/MJO/datos/AAO/SAM2014.txt', header=None, delimiter=',', na_values='-99') ### year, month, day, day of week, SAM
sam3 = pd.read_csv('/home/emi/Documents/MJO/datos/AAO/SAM2007.txt', header=None, delimiter=',', na_values='-99') ### year, month, day, day of week, SAM


Darg_c_ver = Darg_cruda.loc[(Darg_cruda[1] == 1) | (Darg_cruda[1] == 2) | (Darg_cruda[1] == 12)]
Darg_c_oto = Darg_cruda.loc[(Darg_cruda[1] == 3) | (Darg_cruda[1] == 4) | (Darg_cruda[1] == 5)]
Darg_c_inv = Darg_cruda.loc[(Darg_cruda[1] == 6) | (Darg_cruda[1] == 7) | (Darg_cruda[1] == 8)]
Darg_c_pri = Darg_cruda.loc[(Darg_cruda[1] == 9) | (Darg_cruda[1] == 10) | (Darg_cruda[1] == 11)]

#Dargentina multiplico x 1000 x que esta en gigas
Darg_p_v = 100/(1000*Darg_c_ver[3].mean())
Darg_p_o = 100/(1000*Darg_c_oto[3].mean())
Darg_p_i = 100/(1000*Darg_c_inv[3].mean())
Darg_p_p = 100/(1000*Darg_c_pri[3].mean())
# ~ print(Dchi_p_v)
# ~ print(Darg_p_v)
# ~ print(Darg_p_o)
# ~ print(Darg_p_i)
# ~ print(Darg_p_p)


#### DargENTINA
series3 = pd.DataFrame()
# cargamos mes, para despues filtrar por estacion
series3[0] = sam3[1]
# cargamos dia de la semana, para cuando trabajemos con demanda
series3[1] = sam3[3]
#  cargamos amplitud, para quedarnos con MJO activas
series3[2] = sam3[4]
# series uruguay argentina chile
series3[3] = Darg[1]*1000

# sacamos los Dfines de semana
# ~ series3 = series3.loc[(series3[1] == 1) | (series3[1] == 2) | (series3[1] == 3) | (series3[1] == 1) | (series3[1] == 5)]

# VERANO
verano_A = series3.loc[(series3[0] == 1) | (series3[0] == 2) | (series3[0] == 12)]
DnegAv = verano_A.loc[verano_A[2] <= -1]
DneuAv = verano_A.loc[(verano_A[2] >= -1) & (verano_A[2] <= 1)]
DposAv = verano_A.loc[verano_A[2] >= 1]
print(DnegAv)
print(DneuAv)
print(DposAv)
print(DnegAv[3].mean())
print(DneuAv[3].mean())
print(DposAv[3].mean())

# OTOÑO
otono_A = series3.loc[(series3[0] == 3) | (series3[0] == 4) | (series3[0] == 5)]
DnegAo = otono_A.loc[otono_A[2] <= -1]
DneuAo = otono_A.loc[(otono_A[2] >= -1) & (otono_A[2] <= 1)]
DposAo = otono_A.loc[otono_A[2] >= 1]

# INVIERNO
invierno_A = series3.loc[(series3[0] == 6) | (series3[0] == 7) | (series3[0] == 8)]
DnegAi = invierno_A.loc[invierno_A[2] <= -1]
DneuAi = invierno_A.loc[(invierno_A[2] >= -1) & (invierno_A[2] <= 1)]
DposAi = invierno_A.loc[invierno_A[2] >= 1]

# primavera
primavera_A = series3.loc[(series3[0] == 9) | (series3[0] == 10) | (series3[0] == 11)]
DnegAp = primavera_A.loc[primavera_A[2] <= -1]
DneuAp = primavera_A.loc[(primavera_A[2] >= -1) & (primavera_A[2] <= 1)]
DposAp = primavera_A.loc[primavera_A[2] >= 1]

porc = 100/(1000*Darg_cruda[3].mean())

Dargver = [DnegAv[3].mean()*Darg_p_v,DposAv[3].mean()*Darg_p_v]
Dargoto = [DnegAo[3].mean()*Darg_p_o,DposAo[3].mean()*Darg_p_o]
Darginv = [DnegAi[3].mean()*Darg_p_i,DposAi[3].mean()*Darg_p_i]
Dargpri = [DnegAp[3].mean()*Darg_p_p,DposAp[3].mean()*Darg_p_p]

X = [1,2]
fig, (ax1,ax2,ax3,ax4) = plt.subplots(1, 4,figsize=(7.5,1.75), sharex= True, sharey=True)

########## argentina

ax1.set_title('DEF', fontsize=13, weight='bold')
ax1.bar(X, Dargver, alpha = 0.8)
ax1.tick_params(labelsize=14)
ax1.axhline(y=0, color="black", linestyle="--", linewidth = 1.5, alpha = 1, zorder = 0)
ax1.set_yticks([-2,2], ['-2','2'])
ax1.set_ylim(-3,3)
# ~ ax1.xaxis.set_tick_params(length=0)

ax2.set_title('MAM', fontsize=13, weight='bold')
ax2.bar(X, Dargoto, alpha = 0.8)
ax2.tick_params(labelsize=14)
ax2.axhline(y=0, color="black", linestyle="--", linewidth = 1.5, alpha = 1, zorder = 0)
ax2.set_yticks([-2,2], ['-2','2'])
ax2.set_ylim(-3,3)
# ~ ax2.xaxis.set_tick_params(length=0)

ax3.set_title('JJA', fontsize=13, weight='bold')
ax3.bar(X, Darginv, alpha = 0.8)
ax3.tick_params(labelsize=14)
ax3.axhline(y=0, color="black", linestyle="--", linewidth = 1.5, alpha = 1, zorder = 0)
ax3.set_yticks([-2,2], ['-2','2'])
ax3.set_ylim(-3,3)
# ~ ax3.xaxis.set_tick_params(length=0)

ax4.set_title('SON', fontsize=13, weight='bold')
ax4.bar(X, Dargpri, alpha = 0.8, label= 'radiation')
ax4.tick_params(labelsize=14)
ax4.axhline(y=0, color="black", linestyle="--", linewidth = 1.5, alpha = 1, zorder = 0)
ax4.set_yticks([-2,2], ['-2','2'])
ax4.set_ylim(-3,3)
ax4.set_xticks([1,2], ['<-1','>+1'])
# ~ ax4.tick_params(axis='x', labelrotation=90)



# ~ fig.text(0.91, 0.77, 'DJF', fontsize = 14, rotation='vertical')
# ~ fig.text(0.91, 0.59, 'MAM', fontsize = 14, rotation='vertical')
# ~ fig.text(0.91, 0.44, 'JJA', fontsize = 14, rotation='vertical')
# ~ fig.text(0.91, 0.25, 'SON', fontsize = 14, rotation='vertical')
fig.text(0.05, 0.22, 'variación [%]', fontsize=14, rotation='vertical')
fig.text(0.45, -0.12, 'Indice AAO', fontsize=14)
fig.subplots_adjust(wspace=0.15)
fig.subplots_adjust(bottom=0.2)
plt.savefig('AAO_D.png',bbox_inches="tight", dpi=600)

