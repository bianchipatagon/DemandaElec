import numpy as N
import matplotlib.pyplot as plt
from datetime import datetime
import pandas as pd
from scipy.signal import detrend



Vmad = pd.read_csv('/home/emi/Documents/MJO/datos/mjo/WH.txt', header=None, delimiter=',', na_values='-99') ### year, month, day, day of week, RMM1, RMM2, phase, amplitude



#################################
#######DEMANDA####################
#################################

Darg = pd.read_csv('/home/emi/Documents/MJO/datos/demanda/arg-dem-agrup.csv', header=None, delimiter=',', na_values='-99')


Darg_cruda = pd.read_csv('/home/emi/Documents/MJO/datos/demanda/arg-dem.txt', header=None, delimiter=';')

mad = pd.read_csv('/home/emi/Documents/MJO/datos/mjo/WH2011.txt', header=None, delimiter=',', na_values='-99') ### year, month, day, day oDf week, RMM1, RMM2, phase, amplitude
mad2 = pd.read_csv('/home/emi/Documents/MJO/datos/mjo/WH2014.txt', header=None, delimiter=',', na_values='-99')
mad3 = pd.read_csv('/home/emi/Documents/MJO/datos/mjo/WH2007.txt', header=None, delimiter=',', na_values='-99')


Darg_c_ver = Darg_cruda.loc[(Darg_cruda[1] == 1) | (Darg_cruda[1] == 2) | (Darg_cruda[1] == 12)]
Darg_c_oto = Darg_cruda.loc[(Darg_cruda[1] == 3) | (Darg_cruda[1] == 4) | (Darg_cruda[1] == 5)]
Darg_c_inv = Darg_cruda.loc[(Darg_cruda[1] == 6) | (Darg_cruda[1] == 7) | (Darg_cruda[1] == 8)]
Darg_c_pri = Darg_cruda.loc[(Darg_cruda[1] == 9) | (Darg_cruda[1] == 10) | (Darg_cruda[1] == 11)]

#Dargentina multiplico x 1000 x que esta en gigas
Darg_p_v = 100/(1000*Darg_c_ver[3].mean())
Darg_p_o = 100/(1000*Darg_c_oto[3].mean())
Darg_p_i = 100/(1000*Darg_c_inv[3].mean())
Darg_p_p = 100/(1000*Darg_c_pri[3].mean())


#### DargENTINA
series3 = pd.DataFrame()
# cDargamos mes, para despues Dfiltrar por estacion
series3[0] = mad3[1]
# cDargamos Dfase
series3[1] = mad3[6]
# cDargamos dia de la semana, para cuando trabajemos con demanda
series3[2] = mad3[3]
#  cDargamos amplitud, para quedarnos con MJO activas
series3[3] = mad3[7]
# series Duruguay Dargentina Dchile
series3[4] = Darg[1]*1000

# nos quedamos con MJO activos, esto es cuando la amplitud es >= 1
series3 = series3.loc[series3[3] > 1]
# sacamos los Dfines de semana
series3 = series3.loc[(series3[2] == 1) | (series3[2] == 2) | (series3[2] == 3) | (series3[2] == 1) | (series3[2] == 5)]

# VERANO
verano_A = series3.loc[(series3[0] == 1) | (series3[0] == 2) | (series3[0] == 12)]
Df1Av = verano_A.loc[verano_A[1] == 1]
Df2Av = verano_A.loc[verano_A[1] == 2]
Df3Av = verano_A.loc[verano_A[1] == 3]
Df4Av = verano_A.loc[verano_A[1] == 4]
Df5Av = verano_A.loc[verano_A[1] == 5]
Df6Av = verano_A.loc[verano_A[1] == 6]
Df7Av = verano_A.loc[verano_A[1] == 7]
Df8Av = verano_A.loc[verano_A[1] == 8]

# OTOÑO
otono_A = series3.loc[(series3[0] == 3) | (series3[0] == 4) | (series3[0] == 5)]
Df1Ao = otono_A.loc[otono_A[1] == 1]
Df2Ao = otono_A.loc[otono_A[1] == 2]
Df3Ao = otono_A.loc[otono_A[1] == 3]
Df4Ao = otono_A.loc[otono_A[1] == 4]
Df5Ao = otono_A.loc[otono_A[1] == 5]
Df6Ao = otono_A.loc[otono_A[1] == 6]
Df7Ao = otono_A.loc[otono_A[1] == 7]
Df8Ao = otono_A.loc[otono_A[1] == 8]

# INVIERNO
invierno_A = series3.loc[(series3[0] == 6) | (series3[0] == 7) | (series3[0] == 8)]
Df1Ai = invierno_A.loc[invierno_A[1] == 1]
Df2Ai = invierno_A.loc[invierno_A[1] == 2]
Df3Ai = invierno_A.loc[invierno_A[1] == 3]
Df4Ai = invierno_A.loc[invierno_A[1] == 4]
Df5Ai = invierno_A.loc[invierno_A[1] == 5]
Df6Ai = invierno_A.loc[invierno_A[1] == 6]
Df7Ai = invierno_A.loc[invierno_A[1] == 7]
Df8Ai = invierno_A.loc[invierno_A[1] == 8]

# primavera
primavera_A = series3.loc[(series3[0] == 9) | (series3[0] == 10) | (series3[0] == 11)]
Df1Ap = primavera_A.loc[primavera_A[1] == 1]
Df2Ap = primavera_A.loc[primavera_A[1] == 2]
Df3Ap = primavera_A.loc[primavera_A[1] == 3]
Df4Ap = primavera_A.loc[primavera_A[1] == 4]
Df5Ap = primavera_A.loc[primavera_A[1] == 5]
Df6Ap = primavera_A.loc[primavera_A[1] == 6]
Df7Ap = primavera_A.loc[primavera_A[1] == 7]
Df8Ap = primavera_A.loc[primavera_A[1] == 8]

porc = 100/(1000*Darg_cruda[3].mean())

Dargver = [Df1Av[4].mean()*Darg_p_v,Df2Av[4].mean()*Darg_p_v,Df3Av[4].mean()*Darg_p_v,Df4Av[4].mean()*Darg_p_v,Df5Av[4].mean()*Darg_p_v,Df6Av[4].mean()*Darg_p_v,Df7Av[4].mean()*Darg_p_v,Df8Av[4].mean()*Darg_p_v]
Dargver10 = [Df1Av[4].quantile(.3)*Darg_p_v,Df2Av[4].quantile(.3)*Darg_p_v,Df3Av[4].quantile(.3)*Darg_p_v,Df4Av[4].quantile(.3)*Darg_p_v,Df5Av[4].quantile(.3)*Darg_p_v,Df6Av[4].quantile(.3)*Darg_p_v,Df7Av[4].quantile(.3)*Darg_p_v,Df8Av[4].quantile(.3)*Darg_p_v]
Dargver90 = [Df1Av[4].quantile(.7)*Darg_p_v,Df2Av[4].quantile(.7)*Darg_p_v,Df3Av[4].quantile(.7)*Darg_p_v,Df4Av[4].quantile(.7)*Darg_p_v,Df5Av[4].quantile(.7)*Darg_p_v,Df6Av[4].quantile(.7)*Darg_p_v,Df7Av[4].quantile(.7)*Darg_p_v,Df8Av[4].quantile(.7)*Darg_p_v]
Dargoto = [Df1Ao[4].mean()*Darg_p_o,Df2Ao[4].mean()*Darg_p_o,Df3Ao[4].mean()*Darg_p_o,Df4Ao[4].mean()*Darg_p_o,Df5Ao[4].mean()*Darg_p_o,Df6Ao[4].mean()*Darg_p_o,Df7Ao[4].mean()*Darg_p_o,Df8Ao[4].mean()*Darg_p_o ]
Darginv = [Df1Ai[4].mean()*Darg_p_i,Df2Ai[4].mean()*Darg_p_i,Df3Ai[4].mean()*Darg_p_i,Df4Ai[4].mean()*Darg_p_i,Df5Ai[4].mean()*Darg_p_i,Df6Ai[4].mean()*Darg_p_i,Df7Ai[4].mean()*Darg_p_i,Df8Ai[4].mean()*Darg_p_i ]
Dargpri = [Df1Ap[4].mean()*Darg_p_p,Df2Ap[4].mean()*Darg_p_p,Df3Ap[4].mean()*Darg_p_p,Df4Ap[4].mean()*Darg_p_p,Df5Ap[4].mean()*Darg_p_p,Df6Ap[4].mean()*Darg_p_p,Df7Ap[4].mean()*Darg_p_p,Df8Ap[4].mean()*Darg_p_p ]

X = [1,2,3,4,5,6,7,8]

fig, (ax1,ax2,ax3,ax4) = plt.subplots(1,4,figsize=(7.75,1.75),sharey=True, sharex=True)

########## argentina

ax1.set_title('DEF', fontsize=13, weight='bold')
ax1.bar(X, Dargver, alpha = 0.8)
ax1.tick_params(labelsize=14)
ax1.axhline(y=0, color="black", linestyle="--", linewidth = 1.5, alpha = 1, zorder = 0)
ax1.set_yticks([-2,2], ['-2','2'])
ax1.set_ylim(-4.5,4.5)
# ~ ax1.xaxis.set_tick_params(length=0)

ax2.set_title('MAM', fontsize=13, weight='bold')
ax2.bar(X, Dargoto, alpha = 0.8)
ax2.tick_params(labelsize=14)
ax2.axhline(y=0, color="black", linestyle="--", linewidth = 1.5, alpha = 1, zorder = 0)
ax2.set_yticks([-2,2], ['-2','2'])
ax2.set_ylim(-4.5,4.5)
# ~ ax2.xaxis.set_tick_params(length=0)

ax3.set_title('JJA', fontsize=13, weight='bold')
ax3.bar(X, Darginv, alpha = 0.8)
ax3.tick_params(labelsize=14)
ax3.axhline(y=0, color="black", linestyle="--", linewidth = 1.5, alpha = 1, zorder = 0)
ax3.set_yticks([-2,2], ['-2','2'])
ax3.set_ylim(-4.5,4.5)
# ~ ax3.xaxis.set_tick_params(length=0)

ax4.set_title('SON', fontsize=13, weight='bold')
ax4.bar(X, Dargpri, alpha = 0.8, label= 'power demand')
ax4.tick_params(labelsize=14)
ax4.axhline(y=0, color="black", linestyle="--", linewidth = 1.5, alpha = 1, zorder = 0)
ax4.set_yticks([-2,2], ['-2','2'])
ax4.set_ylim(-4.5,4.5)
ax4.set_xticks([1,2,3,4,5,6,7,8], ['1','2','3','4','5','6','7','8'])



# ~ fig.text(0.91, 0.77, 'DJF', fontsize = 14, rotation='vertical')
# ~ fig.text(0.91, 0.57, 'MAM', fontsize = 14, rotation='vertical')
# ~ fig.text(0.91, 0.39, 'JJA', fontsize = 14, rotation='vertical')
# ~ fig.text(0.91, 0.19, 'SON', fontsize = 14, rotation='vertical')
fig.text(0.05, 0.22, 'variación [%]', fontsize=14, rotation='vertical')
fig.text(0.45, -0.12, 'fase MJO', fontsize=14)
fig.subplots_adjust(wspace=0.2)
fig.subplots_adjust(bottom=0.15)
plt.savefig('mjoD.png',bbox_inches="tight", dpi=600)

# ~ fig, (ax1,ax2,ax3,ax4) = plt.subplots(1, 4,figsize=(9,2.5), sharey=True, sharex= True)


