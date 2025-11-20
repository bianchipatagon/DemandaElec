import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import numpy as np
import pandas as pd
from scipy.stats import chi2_contingency, fisher_exact
import seaborn as sn

df = pd.read_csv('/home/emi/Documents/MAESTRIA/14-Metodología/DemandaElec/DATOS/indices.txt', header=None, delimiter=',')
print(df)


### hay que elegir los meses que tienen el promedio de cdad estacion
### o lo hago a nivel mensual para cada uno de las estaciones? voy a tener mas casos...

#### VERANO
ver = df.loc[(df[1] == 12) | (df[1] == 1) | (df[1] == 2)]
print(ver[2])

#### verano/MEI
meiV = pd.DataFrame()
# Apply qcut to var1 (quantile-based classification)
meiV[1] = pd.qcut(ver[2], q=3, labels=['T1', 'T2', 'T3'])
# Apply cut to var2 (fixed bins)
meiV[2] = pd.cut(ver[4],bins=[-np.inf, -0.5, 0.5, np.inf],labels=['Niña', 'neutro', 'Niño'])

# Create contingency table
cont1 = pd.crosstab(meiV[1], meiV[2])
chi2, p_value, dof, expected_freq = chi2_contingency(cont1)

print("verano mEI")
print(f"Chi-Square Statistic: {chi2:.4f}")
print(f"P-value: {p_value:.4f}")

#### verano/AAO
aaoV = pd.DataFrame()
# Apply qcut to var1 (quantile-based classification)
aaoV[1] = pd.qcut(ver[2], q=3, labels=['T1', 'T2', 'T3'])
# Apply cut to var2 (fixed bins)
aaoV[2] = pd.cut(ver[3],bins=[-np.inf, -1, 1, np.inf],labels=['AAO-', 'neutro', 'AAO+'])

# Create contingency table
cont2 = pd.crosstab(aaoV[1], aaoV[2])
# ~ print(cont1)

chi2, p_value, dof, expected_freq = chi2_contingency(cont2)

print("verano AAO")
print(f"Chi-Square Statistic: {chi2:.4f}")
print(f"P-value: {p_value:.4f}")

#### verano/TEMP
tV = pd.DataFrame()
# Apply qcut to var1 (quantile-based classification)
tV[1] = pd.qcut(ver[2], q=3, labels=['T1', 'T2', 'T3'])
# Apply cut to var2 (fixed bins)
tV[2] = pd.qcut(ver[5], q=3, labels=['temp-', 'T2', 'temp+'])

# Create contingency table
cont3 = pd.crosstab(tV[1], tV[2])
# ~ print(cont1)

chi2, p_value, dof, expected_freq = chi2_contingency(cont3)

print("veranoT")
print(f"Chi-Square Statistic: {chi2:.4f}")
print(f"P-value: {p_value:.4f}")

#### otoǹo
oto = df.loc[(df[1] == 3) | (df[1] == 4) | (df[1] == 5)]

#### verano/MEI
meiO = pd.DataFrame()
# Apply qcut to var1 (quantile-based classification)
meiO[1] = pd.qcut(oto[2], q=3, labels=['T1', 'T2', 'T3'])
# Apply cut to var2 (fixed bins)
meiO[2] = pd.cut(oto[4],bins=[-np.inf, -0.5, 0.5, np.inf],labels=['Niña', 'neutro', 'Niño'])

# Create contingency table
cont4 = pd.crosstab(meiO[1], meiO[2])
chi2, p_value, dof, expected_freq = chi2_contingency(cont4)

print("otoño mEI")
print(f"Chi-Square Statistic: {chi2:.4f}")
print(f"P-value: {p_value:.4f}")

#### verano/AAO
aaoO = pd.DataFrame()
# Apply qcut to var1 (quantile-based classification)
aaoO[1] = pd.qcut(oto[2], q=3, labels=['T1', 'T2', 'T3'])
# Apply cut to var2 (fixed bins)
aaoO[2] = pd.cut(oto[3],bins=[-np.inf, -1, 1, np.inf],labels=['AAO-', 'neutro', 'AAO+'])

# Create contingency table
cont5 = pd.crosstab(aaoO[1], aaoO[2])
# ~ print(cont1)

chi2, p_value, dof, expected_freq = chi2_contingency(cont5)

print("otono AAO")
print(f"Chi-Square Statistic: {chi2:.4f}")
print(f"P-value: {p_value:.4f}")

#### otono/TEMP
tO = pd.DataFrame()
# Apply qcut to var1 (quantile-based classification)
tO[1] = pd.qcut(oto[2], q=3, labels=['T1', 'T2', 'T3'])
# Apply cut to var2 (fixed bins)
tO[2] = pd.qcut(oto[5], q=3, labels=['temp-', 'T2', 'temp+'])

# Create contingency table
cont6 = pd.crosstab(tO[1], tO[2])
# ~ print(cont1)

chi2, p_value, dof, expected_freq = chi2_contingency(cont6)

print("otonoT")
print(f"Chi-Square Statistic: {chi2:.4f}")
print(f"P-value: {p_value:.4f}")

#### invierno
inv = df.loc[(df[1] == 6) | (df[1] == 7) | (df[1] == 8)]

#### inv/MEI
meiI = pd.DataFrame()
# Apply qcut to var1 (quantile-based classification)
meiI[1] = pd.qcut(inv[2], q=3, labels=['T1', 'T2', 'T3'])
# Apply cut to var2 (fixed bins)
meiI[2] = pd.cut(inv[4],bins=[-np.inf, -0.5, 0.5, np.inf],labels=['Niña', 'neutro', 'Niño'])

# Create contingency table
cont7 = pd.crosstab(meiI[1], meiI[2])
chi2, p_value, dof, expected_freq = chi2_contingency(cont7)

print("invierno mEI")
print(f"Chi-Square Statistic: {chi2:.4f}")
print(f"P-value: {p_value:.4f}")

#### verano/AAO
aaoI = pd.DataFrame()
# Apply qcut to var1 (quantile-based classification)
aaoI[1] = pd.qcut(inv[2], q=3, labels=['T1', 'T2', 'T3'])
# Apply cut to var2 (fixed bins)
aaoI[2] = pd.cut(inv[3],bins=[-np.inf, -1, 1, np.inf],labels=['AAO-', 'neutro', 'AAO+'])

# Create contingency table
cont8 = pd.crosstab(aaoI[1], aaoI[2])
# ~ print(cont1)

chi2, p_value, dof, expected_freq = chi2_contingency(cont8)

print("invierno AAO")
print(f"Chi-Square Statistic: {chi2:.4f}")
print(f"P-value: {p_value:.4f}")

####invierno/TEMP
tI = pd.DataFrame()
# Apply qcut to var1 (quantile-based classification)
tI[1] = pd.qcut(inv[2], q=3, labels=['T1', 'T2', 'T3'])
# Apply cut to var2 (fixed bins)
tI[2] = pd.qcut(inv[5], q=3, labels=['temp-', 'T2', 'temp+'])

# Create contingency table
cont9 = pd.crosstab(tI[1], tI[2])
# ~ print(cont1)

chi2, p_value, dof, expected_freq = chi2_contingency(cont9)

print("invT")
print(f"Chi-Square Statistic: {chi2:.4f}")
print(f"P-value: {p_value:.4f}")

#### primavera
pri = df.loc[(df[1] == 9) | (df[1] == 10) | (df[1] == 11)]

#### primavera/MEI
meiP = pd.DataFrame()
# Apply qcut to var1 (quantile-based classification)
meiP[1] = pd.qcut(pri[2], q=3, labels=['T1', 'T2', 'T3'])
# Apply cut to var2 (fixed bins)
meiP[2] = pd.cut(pri[4],bins=[-np.inf, -0.5, 0.5, np.inf],labels=['Niña', 'neutro', 'Niño'])

# Create contingency table
cont10 = pd.crosstab(meiI[1], meiI[2])
chi2, p_value, dof, expected_freq = chi2_contingency(cont10)

print("pri mEI")
print(f"Chi-Square Statistic: {chi2:.4f}")
print(f"P-value: {p_value:.4f}")

#### primavera/AAO
aaoP = pd.DataFrame()
# Apply qcut to var1 (quantile-based classification)
aaoP[1] = pd.qcut(pri[2], q=3, labels=['T1', 'T2', 'T3'])
# Apply cut to var2 (fixed bins)
aaoP[2] = pd.cut(pri[3],bins=[-np.inf, -1, 1, np.inf],labels=['AAO-', 'neutro', 'AAO+'])

# Create contingency table
cont11 = pd.crosstab(aaoP[1], aaoP[2])
# ~ print(cont1)

chi2, p_value, dof, expected_freq = chi2_contingency(cont11)

print("primaveraAAO")
print(f"Chi-Square Statistic: {chi2:.4f}")
print(f"P-value: {p_value:.4f}")

####primavera/TEMP
tP = pd.DataFrame()
# Apply qcut to var1 (quantile-based classification)
tP[1] = pd.qcut(pri[2], q=3, labels=['T1', 'T2', 'T3'])
# Apply cut to var2 (fixed bins)
tP[2] = pd.qcut(pri[5], q=3, labels=['temp-', 'T2', 'temp+'])

# Create contingency table
cont12 = pd.crosstab(tP[1], tP[2])
# ~ print(cont1)

chi2, p_value, dof, expected_freq = chi2_contingency(cont12)

print("priT")
print(f"Chi-Square Statistic: {chi2:.4f}")
print(f"P-value: {p_value:.4f}")


fig, ((ax1,ax2,ax3),(ax4,ax5,ax6),(ax7,ax8,ax9),(ax10,ax11,ax12)) = plt.subplots(4,3,figsize=(6,6),sharey=True)
sn.heatmap(cont1, annot=True, annot_kws={"size": 15}, cmap="Blues",ax=ax1, vmin= 0, vmax=10, linewidths=2,cbar=False)
sn.heatmap(cont2, annot=True, annot_kws={"size": 15}, cmap="Blues",ax=ax2, vmin= 0, vmax=10, linewidths=2,cbar=False)
ax2.set_title('DJF', fontsize=16)

sn.heatmap(cont3, annot=True, annot_kws={"size": 15}, cmap="Blues",ax=ax3, vmin= 0, vmax=10, linewidths=2,cbar=False)
sn.heatmap(cont4, annot=True, annot_kws={"size": 15}, cmap="Blues",ax=ax4, vmin= 0, vmax=10, linewidths=2,cbar=False)
sn.heatmap(cont5, annot=True, annot_kws={"size": 15}, cmap="Blues",ax=ax5, vmin= 0, vmax=10, linewidths=2,cbar=False)
ax5.set_title('MAM', fontsize=16)

sn.heatmap(cont6, annot=True, annot_kws={"size": 15}, cmap="Blues",ax=ax6, vmin= 0, vmax=10, linewidths=2,cbar=False)
sn.heatmap(cont7, annot=True, annot_kws={"size": 15}, cmap="Blues",ax=ax7, vmin= 0, vmax=10, linewidths=2,cbar=False)
sn.heatmap(cont8, annot=True, annot_kws={"size": 15}, cmap="Blues",ax=ax8, vmin= 0, vmax=10, linewidths=2,cbar=False)
ax8.set_title('JJA', fontsize=16)

sn.heatmap(cont9, annot=True, annot_kws={"size": 15}, cmap="Blues",ax=ax9, vmin= 0, vmax=10, linewidths=2,cbar=False)
sn.heatmap(cont10, annot=True, annot_kws={"size": 15}, cmap="Blues",ax=ax10, vmin= 0, vmax=10, linewidths=2,cbar=False)
sn.heatmap(cont11, annot=True, annot_kws={"size": 15}, cmap="Blues",ax=ax11, vmin= 0, vmax=10, linewidths=2,cbar=False)
ax11.set_title('SON', fontsize=16)

sn.heatmap(cont12, annot=True, annot_kws={"size": 15}, cmap="Blues",ax=ax12, vmin= 0, vmax=10, linewidths=2,cbar=False)

ax1.yaxis.set_tick_params(labelsize=13, color='white', labelrotation=0)
ax4.yaxis.set_tick_params(labelsize=13, color='white', labelrotation=0)
ax7.yaxis.set_tick_params(labelsize=13, color='white', labelrotation=0)
ax10.yaxis.set_tick_params(labelsize=13, color='white', labelrotation=0)
ax10.xaxis.set_tick_params(labelsize=13, color='white', labelrotation=90)
ax11.xaxis.set_tick_params(labelsize=13, color='white', labelrotation=90)
ax12.xaxis.set_tick_params(labelsize=13, color='white', labelrotation=90)

fig.subplots_adjust(wspace=0.05, hspace=0.4)

plt.savefig('indices.svg', dpi=300, bbox_inches="tight")

# ~ sn.heatmap(corr, cmap="PuOr",ax=ax,cbar=i == 0, vmin= -1, vmax=1, linewidths=2,cbar_ax=None if i else cbar_ax, cbar_kws={'label': 'corr. coefficient []'})
