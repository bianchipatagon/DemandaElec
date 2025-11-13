import numpy as N
import matplotlib.pyplot as plt
from datetime import datetime
import pandas as pd
import seaborn as sns
from scipy.stats import spearmanr
from matplotlib.ticker import MultipleLocator

#############
############# NUBOSIDAD
#############

cld = pd.read_csv('/home/emi/Documents/MAESTRIA/14-Metodología/DemandaElec/DATOS/prueba_cld.txt', header=None, delimiter=',', na_values='-99')
cld.index = pd.date_range(start="2021-01-01 00:00:00", end="2023-12-31  23:00:00",freq="H")

# promedio ponderado de nubosidad por la poblacion de GBA, GCA, GROS

cld[6] = round(0.81*cld[3] + 0.1*cld[4] + 0.09*cld[5],0)

# nos quedamos con los dias de la semana
cld = cld.loc[(cld[1] == 1) | (cld[1] == 2) | (cld[1] == 3) | (cld[1] == 4) | (cld[1] == 5)]

# abril
cld_abr = cld[cld.index.month == 4]
cld_abr1 = cld_abr.loc[(cld_abr[0] == 1)]
cld_abr2 = cld_abr.loc[(cld_abr[0] == 2)]
cld_abr3 = cld_abr.loc[(cld_abr[0] == 3)]
cld_abr4 = cld_abr.loc[(cld_abr[0] == 4)]
cld_abr5 = cld_abr.loc[(cld_abr[0] == 5)]
cld_abr6 = cld_abr.loc[(cld_abr[0] == 6)]
cld_abr7 = cld_abr.loc[(cld_abr[0] == 7)]
cld_abr8 = cld_abr.loc[(cld_abr[0] == 8)]
cld_abr9 = cld_abr.loc[(cld_abr[0] == 9)]
cld_abr10 = cld_abr.loc[(cld_abr[0] == 10)]
cld_abr11 = cld_abr.loc[(cld_abr[0] == 11)]
cld_abr12 = cld_abr.loc[(cld_abr[0] == 12)]
cld_abr13 = cld_abr.loc[(cld_abr[0] == 13)]
cld_abr14 = cld_abr.loc[(cld_abr[0] == 14)]
cld_abr15 = cld_abr.loc[(cld_abr[0] == 15)]
cld_abr16 = cld_abr.loc[(cld_abr[0] == 16)]
cld_abr17 = cld_abr.loc[(cld_abr[0] == 17)]
cld_abr18 = cld_abr.loc[(cld_abr[0] == 18)]
cld_abr19 = cld_abr.loc[(cld_abr[0] == 19)]
cld_abr20 = cld_abr.loc[(cld_abr[0] == 20)]
cld_abr21 = cld_abr.loc[(cld_abr[0] == 21)]
cld_abr22 = cld_abr.loc[(cld_abr[0] == 22)]
cld_abr23 = cld_abr.loc[(cld_abr[0] == 23)]
cld_abr24 = cld_abr.loc[(cld_abr[0] == 24)]

corr_abr_n = [N.corrcoef(cld_abr1[2],cld_abr1[6])[0, 1],N.corrcoef(cld_abr2[2],cld_abr2[6])[0, 1],N.corrcoef(cld_abr3[2],cld_abr3[6])[0, 1],N.corrcoef(cld_abr4[2],cld_abr4[6])[0, 1],N.corrcoef(cld_abr5[2],cld_abr5[6])[0, 1]
,N.corrcoef(cld_abr6[2],cld_abr6[6])[0, 1],N.corrcoef(cld_abr7[2],cld_abr7[6])[0, 1],N.corrcoef(cld_abr8[2],cld_abr8[6])[0, 1],N.corrcoef(cld_abr9[2],cld_abr9[6])[0, 1],N.corrcoef(cld_abr10[2],cld_abr10[6])[0, 1]
,N.corrcoef(cld_abr11[2],cld_abr11[6])[0, 1],N.corrcoef(cld_abr12[2],cld_abr12[6])[0, 1],N.corrcoef(cld_abr13[2],cld_abr13[6])[0, 1],N.corrcoef(cld_abr14[2],cld_abr14[6])[0, 1],N.corrcoef(cld_abr15[2],cld_abr15[6])[0, 1]
,N.corrcoef(cld_abr16[2],cld_abr16[6])[0, 1],N.corrcoef(cld_abr17[2],cld_abr17[6])[0, 1],N.corrcoef(cld_abr18[2],cld_abr18[6])[0, 1],N.corrcoef(cld_abr19[2],cld_abr19[6])[0, 1],N.corrcoef(cld_abr20[2],cld_abr20[6])[0, 1]
,N.corrcoef(cld_abr21[2],cld_abr21[6])[0, 1],N.corrcoef(cld_abr22[2],cld_abr22[6])[0, 1],N.corrcoef(cld_abr23[2],cld_abr23[6])[0, 1],N.corrcoef(cld_abr24[2],cld_abr24[6])[0, 1]]

# julio
cld_jul = cld[cld.index.month == 7]
cld_jul1 = cld_jul.loc[(cld_jul[0] == 1)]
cld_jul2 = cld_jul.loc[(cld_jul[0] == 2)]
cld_jul3 = cld_jul.loc[(cld_jul[0] == 3)]
cld_jul4 = cld_jul.loc[(cld_jul[0] == 4)]
cld_jul5 = cld_jul.loc[(cld_jul[0] == 5)]
cld_jul6 = cld_jul.loc[(cld_jul[0] == 6)]
cld_jul7 = cld_jul.loc[(cld_jul[0] == 7)]
cld_jul8 = cld_jul.loc[(cld_jul[0] == 8)]
cld_jul9 = cld_jul.loc[(cld_jul[0] == 9)]
cld_jul10 = cld_jul.loc[(cld_jul[0] == 10)]
cld_jul11 = cld_jul.loc[(cld_jul[0] == 11)]
cld_jul12 = cld_jul.loc[(cld_jul[0] == 12)]
cld_jul13 = cld_jul.loc[(cld_jul[0] == 13)]
cld_jul14 = cld_jul.loc[(cld_jul[0] == 14)]
cld_jul15 = cld_jul.loc[(cld_jul[0] == 15)]
cld_jul16 = cld_jul.loc[(cld_jul[0] == 16)]
cld_jul17 = cld_jul.loc[(cld_jul[0] == 17)]
cld_jul18 = cld_jul.loc[(cld_jul[0] == 18)]
cld_jul19 = cld_jul.loc[(cld_jul[0] == 19)]
cld_jul20 = cld_jul.loc[(cld_jul[0] == 20)]
cld_jul21 = cld_jul.loc[(cld_jul[0] == 21)]
cld_jul22 = cld_jul.loc[(cld_jul[0] == 22)]
cld_jul23 = cld_jul.loc[(cld_jul[0] == 23)]
cld_jul24 = cld_jul.loc[(cld_jul[0] == 24)]

corr_jul_n = [N.corrcoef(cld_jul1[2],cld_jul1[6])[0, 1],N.corrcoef(cld_jul2[2],cld_jul2[6])[0, 1],N.corrcoef(cld_jul3[2],cld_jul3[6])[0, 1],N.corrcoef(cld_jul4[2],cld_jul4[6])[0, 1],N.corrcoef(cld_jul5[2],cld_jul5[6])[0, 1]
,N.corrcoef(cld_jul6[2],cld_jul6[6])[0, 1],N.corrcoef(cld_jul7[2],cld_jul7[6])[0, 1],N.corrcoef(cld_jul8[2],cld_jul8[6])[0, 1],N.corrcoef(cld_jul9[2],cld_jul9[6])[0, 1],N.corrcoef(cld_jul10[2],cld_jul10[6])[0, 1]
,N.corrcoef(cld_jul11[2],cld_jul11[6])[0, 1],N.corrcoef(cld_jul12[2],cld_jul12[6])[0, 1],N.corrcoef(cld_jul13[2],cld_jul13[6])[0, 1],N.corrcoef(cld_jul14[2],cld_jul14[6])[0, 1],N.corrcoef(cld_jul15[2],cld_jul15[6])[0, 1]
,N.corrcoef(cld_jul16[2],cld_jul16[6])[0, 1],N.corrcoef(cld_jul17[2],cld_jul17[6])[0, 1],N.corrcoef(cld_jul18[2],cld_jul18[6])[0, 1],N.corrcoef(cld_jul19[2],cld_jul19[6])[0, 1],N.corrcoef(cld_jul20[2],cld_jul20[6])[0, 1]
,N.corrcoef(cld_jul21[2],cld_jul21[6])[0, 1],N.corrcoef(cld_jul22[2],cld_jul22[6])[0, 1],N.corrcoef(cld_jul23[2],cld_jul23[6])[0, 1],N.corrcoef(cld_jul24[2],cld_jul24[6])[0, 1]]

# octubre
cld_oct = cld[cld.index.month == 10]
cld_oct1 = cld_oct.loc[(cld_oct[0] == 1)]
cld_oct2 = cld_oct.loc[(cld_oct[0] == 2)]
cld_oct3 = cld_oct.loc[(cld_oct[0] == 3)]
cld_oct4 = cld_oct.loc[(cld_oct[0] == 4)]
cld_oct5 = cld_oct.loc[(cld_oct[0] == 5)]
cld_oct6 = cld_oct.loc[(cld_oct[0] == 6)]
cld_oct7 = cld_oct.loc[(cld_oct[0] == 7)]
cld_oct8 = cld_oct.loc[(cld_oct[0] == 8)]
cld_oct9 = cld_oct.loc[(cld_oct[0] == 9)]
cld_oct10 = cld_oct.loc[(cld_oct[0] == 10)]
cld_oct11 = cld_oct.loc[(cld_oct[0] == 11)]
cld_oct12 = cld_oct.loc[(cld_oct[0] == 12)]
cld_oct13 = cld_oct.loc[(cld_oct[0] == 13)]
cld_oct14 = cld_oct.loc[(cld_oct[0] == 14)]
cld_oct15 = cld_oct.loc[(cld_oct[0] == 15)]
cld_oct16 = cld_oct.loc[(cld_oct[0] == 16)]
cld_oct17 = cld_oct.loc[(cld_oct[0] == 17)]
cld_oct18 = cld_oct.loc[(cld_oct[0] == 18)]
cld_oct19 = cld_oct.loc[(cld_oct[0] == 19)]
cld_oct20 = cld_oct.loc[(cld_oct[0] == 20)]
cld_oct21 = cld_oct.loc[(cld_oct[0] == 21)]
cld_oct22 = cld_oct.loc[(cld_oct[0] == 22)]
cld_oct23 = cld_oct.loc[(cld_oct[0] == 23)]
cld_oct24 = cld_oct.loc[(cld_oct[0] == 24)]

corr_oct_n = [N.corrcoef(cld_oct1[2],cld_oct1[6])[0, 1],N.corrcoef(cld_oct2[2],cld_oct2[6])[0, 1],N.corrcoef(cld_oct3[2],cld_oct3[6])[0, 1],N.corrcoef(cld_oct4[2],cld_oct4[6])[0, 1],N.corrcoef(cld_oct5[2],cld_oct5[6])[0, 1]
,N.corrcoef(cld_oct6[2],cld_oct6[6])[0, 1],N.corrcoef(cld_oct7[2],cld_oct7[6])[0, 1],N.corrcoef(cld_oct8[2],cld_oct8[6])[0, 1],N.corrcoef(cld_oct9[2],cld_oct9[6])[0, 1],N.corrcoef(cld_oct10[2],cld_oct10[6])[0, 1]
,N.corrcoef(cld_oct11[2],cld_oct11[6])[0, 1],N.corrcoef(cld_oct12[2],cld_oct12[6])[0, 1],N.corrcoef(cld_oct13[2],cld_oct13[6])[0, 1],N.corrcoef(cld_oct14[2],cld_oct14[6])[0, 1],N.corrcoef(cld_oct15[2],cld_oct15[6])[0, 1]
,N.corrcoef(cld_oct16[2],cld_oct16[6])[0, 1],N.corrcoef(cld_oct17[2],cld_oct17[6])[0, 1],N.corrcoef(cld_oct18[2],cld_oct18[6])[0, 1],N.corrcoef(cld_oct19[2],cld_oct19[6])[0, 1],N.corrcoef(cld_oct20[2],cld_oct20[6])[0, 1]
,N.corrcoef(cld_oct21[2],cld_oct21[6])[0, 1],N.corrcoef(cld_oct22[2],cld_oct22[6])[0, 1],N.corrcoef(cld_oct23[2],cld_oct23[6])[0, 1],N.corrcoef(cld_oct24[2],cld_oct24[6])[0, 1]]


# diciembre
cld_dic = cld[cld.index.month == 12]
cld_dic1 = cld_dic.loc[(cld_dic[0] == 1)]
cld_dic2 = cld_dic.loc[(cld_dic[0] == 2)]
cld_dic3 = cld_dic.loc[(cld_dic[0] == 3)]
cld_dic4 = cld_dic.loc[(cld_dic[0] == 4)]
cld_dic5 = cld_dic.loc[(cld_dic[0] == 5)]
cld_dic6 = cld_dic.loc[(cld_dic[0] == 6)]
cld_dic7 = cld_dic.loc[(cld_dic[0] == 7)]
cld_dic8 = cld_dic.loc[(cld_dic[0] == 8)]
cld_dic9 = cld_dic.loc[(cld_dic[0] == 9)]
cld_dic10 = cld_dic.loc[(cld_dic[0] == 10)]
cld_dic11 = cld_dic.loc[(cld_dic[0] == 11)]
cld_dic12 = cld_dic.loc[(cld_dic[0] == 12)]
cld_dic13 = cld_dic.loc[(cld_dic[0] == 13)]
cld_dic14 = cld_dic.loc[(cld_dic[0] == 14)]
cld_dic15 = cld_dic.loc[(cld_dic[0] == 15)]
cld_dic16 = cld_dic.loc[(cld_dic[0] == 16)]
cld_dic17 = cld_dic.loc[(cld_dic[0] == 17)]
cld_dic18 = cld_dic.loc[(cld_dic[0] == 18)]
cld_dic19 = cld_dic.loc[(cld_dic[0] == 19)]
cld_dic20 = cld_dic.loc[(cld_dic[0] == 20)]
cld_dic21 = cld_dic.loc[(cld_dic[0] == 21)]
cld_dic22 = cld_dic.loc[(cld_dic[0] == 22)]
cld_dic23 = cld_dic.loc[(cld_dic[0] == 23)]
cld_dic24 = cld_dic.loc[(cld_dic[0] == 24)]

corr_dic_n = [N.corrcoef(cld_dic1[2],cld_dic1[6])[0, 1],N.corrcoef(cld_dic2[2],cld_dic2[6])[0, 1],N.corrcoef(cld_dic3[2],cld_dic3[6])[0, 1],N.corrcoef(cld_dic4[2],cld_dic4[6])[0, 1],N.corrcoef(cld_dic5[2],cld_dic5[6])[0, 1]
,N.corrcoef(cld_dic6[2],cld_dic6[6])[0, 1],N.corrcoef(cld_dic7[2],cld_dic7[6])[0, 1],N.corrcoef(cld_dic8[2],cld_dic8[6])[0, 1],N.corrcoef(cld_dic9[2],cld_dic9[6])[0, 1],N.corrcoef(cld_dic10[2],cld_dic10[6])[0, 1]
,N.corrcoef(cld_dic11[2],cld_dic11[6])[0, 1],N.corrcoef(cld_dic12[2],cld_dic12[6])[0, 1],N.corrcoef(cld_dic13[2],cld_dic13[6])[0, 1],N.corrcoef(cld_dic14[2],cld_dic14[6])[0, 1],N.corrcoef(cld_dic15[2],cld_dic15[6])[0, 1]
,N.corrcoef(cld_dic16[2],cld_dic16[6])[0, 1],N.corrcoef(cld_dic17[2],cld_dic17[6])[0, 1],N.corrcoef(cld_dic18[2],cld_dic18[6])[0, 1],N.corrcoef(cld_dic19[2],cld_dic19[6])[0, 1],N.corrcoef(cld_dic20[2],cld_dic20[6])[0, 1]
,N.corrcoef(cld_dic21[2],cld_dic21[6])[0, 1],N.corrcoef(cld_dic22[2],cld_dic22[6])[0, 1],N.corrcoef(cld_dic23[2],cld_dic23[6])[0, 1],N.corrcoef(cld_dic24[2],cld_dic24[6])[0, 1]]
horas = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24]

#############
############# TEMPERATURA
#############

tem = pd.read_csv('/home/emi/Documents/MAESTRIA/14-Metodología/DemandaElec/DATOS/prueba_t.txt', header=None, delimiter=',', na_values='-99')
tem.index = pd.date_range(start="2021-01-01 00:00:00", end="2023-12-31  23:00:00",freq="H")
print(tem)

# promedio ponderado de nubosidad por la poblacion de GBA, GCA, GROS

tem[9] = round(0.81*tem[6] + 0.1*tem[7] + 0.09*tem[8],0)

# nos quedamos con los dias de la semana
tem = tem.loc[(tem[1] == 1) | (tem[1] == 2) | (tem[1] == 3) | (tem[1] == 4) | (tem[1] == 5)]

# abril
tem_abr = tem[tem.index.month == 4]
tem_abr1 = tem_abr.loc[(tem_abr[0] == 1)]
tem_abr2 = tem_abr.loc[(tem_abr[0] == 2)]
tem_abr3 = tem_abr.loc[(tem_abr[0] == 3)]
tem_abr4 = tem_abr.loc[(tem_abr[0] == 4)]
tem_abr5 = tem_abr.loc[(tem_abr[0] == 5)]
tem_abr6 = tem_abr.loc[(tem_abr[0] == 6)]
tem_abr7 = tem_abr.loc[(tem_abr[0] == 7)]
tem_abr8 = tem_abr.loc[(tem_abr[0] == 8)]
tem_abr9 = tem_abr.loc[(tem_abr[0] == 9)]
tem_abr10 = tem_abr.loc[(tem_abr[0] == 10)]
tem_abr11 = tem_abr.loc[(tem_abr[0] == 11)]
tem_abr12 = tem_abr.loc[(tem_abr[0] == 12)]
tem_abr13 = tem_abr.loc[(tem_abr[0] == 13)]
tem_abr14 = tem_abr.loc[(tem_abr[0] == 14)]
tem_abr15 = tem_abr.loc[(tem_abr[0] == 15)]
tem_abr16 = tem_abr.loc[(tem_abr[0] == 16)]
tem_abr17 = tem_abr.loc[(tem_abr[0] == 17)]
tem_abr18 = tem_abr.loc[(tem_abr[0] == 18)]
tem_abr19 = tem_abr.loc[(tem_abr[0] == 19)]
tem_abr20 = tem_abr.loc[(tem_abr[0] == 20)]
tem_abr21 = tem_abr.loc[(tem_abr[0] == 21)]
tem_abr22 = tem_abr.loc[(tem_abr[0] == 22)]
tem_abr23 = tem_abr.loc[(tem_abr[0] == 23)]
tem_abr24 = tem_abr.loc[(tem_abr[0] == 24)]

corr_abr_t = [N.corrcoef(tem_abr1[2],tem_abr1[9])[0, 1],N.corrcoef(tem_abr2[2],tem_abr2[9])[0, 1],N.corrcoef(tem_abr3[2],tem_abr3[9])[0, 1],N.corrcoef(tem_abr4[2],tem_abr4[9])[0, 1],N.corrcoef(tem_abr5[2],tem_abr5[9])[0, 1]
,N.corrcoef(tem_abr6[2],tem_abr6[9])[0, 1],N.corrcoef(tem_abr7[2],tem_abr7[9])[0, 1],N.corrcoef(tem_abr8[2],tem_abr8[9])[0, 1],N.corrcoef(tem_abr9[2],tem_abr9[9])[0, 1],N.corrcoef(tem_abr10[2],tem_abr10[9])[0, 1]
,N.corrcoef(tem_abr11[2],tem_abr11[9])[0, 1],N.corrcoef(tem_abr12[2],tem_abr12[9])[0, 1],N.corrcoef(tem_abr13[2],tem_abr13[9])[0, 1],N.corrcoef(tem_abr14[2],tem_abr14[9])[0, 1],N.corrcoef(tem_abr15[2],tem_abr15[9])[0, 1]
,N.corrcoef(tem_abr16[2],tem_abr16[9])[0, 1],N.corrcoef(tem_abr17[2],tem_abr17[9])[0, 1],N.corrcoef(tem_abr18[2],tem_abr18[9])[0, 1],N.corrcoef(tem_abr19[2],tem_abr19[9])[0, 1],N.corrcoef(tem_abr20[2],tem_abr20[9])[0, 1]
,N.corrcoef(tem_abr21[2],tem_abr21[9])[0, 1],N.corrcoef(tem_abr22[2],tem_abr22[9])[0, 1],N.corrcoef(tem_abr23[2],tem_abr23[9])[0, 1],N.corrcoef(tem_abr24[2],tem_abr24[9])[0, 1]]

# julio
tem_jul = tem[tem.index.month == 7]
tem_jul1 = tem_jul.loc[(tem_jul[0] == 1)]
tem_jul2 = tem_jul.loc[(tem_jul[0] == 2)]
tem_jul3 = tem_jul.loc[(tem_jul[0] == 3)]
tem_jul4 = tem_jul.loc[(tem_jul[0] == 4)]
tem_jul5 = tem_jul.loc[(tem_jul[0] == 5)]
tem_jul6 = tem_jul.loc[(tem_jul[0] == 6)]
tem_jul7 = tem_jul.loc[(tem_jul[0] == 7)]
tem_jul8 = tem_jul.loc[(tem_jul[0] == 8)]
tem_jul9 = tem_jul.loc[(tem_jul[0] == 9)]
tem_jul10 = tem_jul.loc[(tem_jul[0] == 10)]
tem_jul11 = tem_jul.loc[(tem_jul[0] == 11)]
tem_jul12 = tem_jul.loc[(tem_jul[0] == 12)]
tem_jul13 = tem_jul.loc[(tem_jul[0] == 13)]
tem_jul14 = tem_jul.loc[(tem_jul[0] == 14)]
tem_jul15 = tem_jul.loc[(tem_jul[0] == 15)]
tem_jul16 = tem_jul.loc[(tem_jul[0] == 16)]
tem_jul17 = tem_jul.loc[(tem_jul[0] == 17)]
tem_jul18 = tem_jul.loc[(tem_jul[0] == 18)]
tem_jul19 = tem_jul.loc[(tem_jul[0] == 19)]
tem_jul20 = tem_jul.loc[(tem_jul[0] == 20)]
tem_jul21 = tem_jul.loc[(tem_jul[0] == 21)]
tem_jul22 = tem_jul.loc[(tem_jul[0] == 22)]
tem_jul23 = tem_jul.loc[(tem_jul[0] == 23)]
tem_jul24 = tem_jul.loc[(tem_jul[0] == 24)]

corr_jul_t = [N.corrcoef(tem_jul1[2],tem_jul1[9])[0, 1],N.corrcoef(tem_jul2[2],tem_jul2[9])[0, 1],N.corrcoef(tem_jul3[2],tem_jul3[9])[0, 1],N.corrcoef(tem_jul4[2],tem_jul4[9])[0, 1],N.corrcoef(tem_jul5[2],tem_jul5[9])[0, 1]
,N.corrcoef(tem_jul6[2],tem_jul6[9])[0, 1],N.corrcoef(tem_jul7[2],tem_jul7[9])[0, 1],N.corrcoef(tem_jul8[2],tem_jul8[9])[0, 1],N.corrcoef(tem_jul9[2],tem_jul9[9])[0, 1],N.corrcoef(tem_jul10[2],tem_jul10[9])[0, 1]
,N.corrcoef(tem_jul11[2],tem_jul11[9])[0, 1],N.corrcoef(tem_jul12[2],tem_jul12[9])[0, 1],N.corrcoef(tem_jul13[2],tem_jul13[9])[0, 1],N.corrcoef(tem_jul14[2],tem_jul14[9])[0, 1],N.corrcoef(tem_jul15[2],tem_jul15[9])[0, 1]
,N.corrcoef(tem_jul16[2],tem_jul16[9])[0, 1],N.corrcoef(tem_jul17[2],tem_jul17[9])[0, 1],N.corrcoef(tem_jul18[2],tem_jul18[9])[0, 1],N.corrcoef(tem_jul19[2],tem_jul19[9])[0, 1],N.corrcoef(tem_jul20[2],tem_jul20[9])[0, 1]
,N.corrcoef(tem_jul21[2],tem_jul21[9])[0, 1],N.corrcoef(tem_jul22[2],tem_jul22[9])[0, 1],N.corrcoef(tem_jul23[2],tem_jul23[9])[0, 1],N.corrcoef(tem_jul24[2],tem_jul24[9])[0, 1]]

# octubre
tem_oct = tem[tem.index.month == 10]
tem_oct1 = tem_oct.loc[(tem_oct[0] == 1)]
tem_oct2 = tem_oct.loc[(tem_oct[0] == 2)]
tem_oct3 = tem_oct.loc[(tem_oct[0] == 3)]
tem_oct4 = tem_oct.loc[(tem_oct[0] == 4)]
tem_oct5 = tem_oct.loc[(tem_oct[0] == 5)]
tem_oct6 = tem_oct.loc[(tem_oct[0] == 6)]
tem_oct7 = tem_oct.loc[(tem_oct[0] == 7)]
tem_oct8 = tem_oct.loc[(tem_oct[0] == 8)]
tem_oct9 = tem_oct.loc[(tem_oct[0] == 9)]
tem_oct10 = tem_oct.loc[(tem_oct[0] == 10)]
tem_oct11 = tem_oct.loc[(tem_oct[0] == 11)]
tem_oct12 = tem_oct.loc[(tem_oct[0] == 12)]
tem_oct13 = tem_oct.loc[(tem_oct[0] == 13)]
tem_oct14 = tem_oct.loc[(tem_oct[0] == 14)]
tem_oct15 = tem_oct.loc[(tem_oct[0] == 15)]
tem_oct16 = tem_oct.loc[(tem_oct[0] == 16)]
tem_oct17 = tem_oct.loc[(tem_oct[0] == 17)]
tem_oct18 = tem_oct.loc[(tem_oct[0] == 18)]
tem_oct19 = tem_oct.loc[(tem_oct[0] == 19)]
tem_oct20 = tem_oct.loc[(tem_oct[0] == 20)]
tem_oct21 = tem_oct.loc[(tem_oct[0] == 21)]
tem_oct22 = tem_oct.loc[(tem_oct[0] == 22)]
tem_oct23 = tem_oct.loc[(tem_oct[0] == 23)]
tem_oct24 = tem_oct.loc[(tem_oct[0] == 24)]

corr_oct_t = [N.corrcoef(tem_oct1[2],tem_oct1[9])[0, 1],N.corrcoef(tem_oct2[2],tem_oct2[9])[0, 1],N.corrcoef(tem_oct3[2],tem_oct3[9])[0, 1],N.corrcoef(tem_oct4[2],tem_oct4[9])[0, 1],N.corrcoef(tem_oct5[2],tem_oct5[9])[0, 1]
,N.corrcoef(tem_oct6[2],tem_oct6[9])[0, 1],N.corrcoef(tem_oct7[2],tem_oct7[9])[0, 1],N.corrcoef(tem_oct8[2],tem_oct8[9])[0, 1],N.corrcoef(tem_oct9[2],tem_oct9[9])[0, 1],N.corrcoef(tem_oct10[2],tem_oct10[9])[0, 1]
,N.corrcoef(tem_oct11[2],tem_oct11[9])[0, 1],N.corrcoef(tem_oct12[2],tem_oct12[9])[0, 1],N.corrcoef(tem_oct13[2],tem_oct13[9])[0, 1],N.corrcoef(tem_oct14[2],tem_oct14[9])[0, 1],N.corrcoef(tem_oct15[2],tem_oct15[9])[0, 1]
,N.corrcoef(tem_oct16[2],tem_oct16[9])[0, 1],N.corrcoef(tem_oct17[2],tem_oct17[9])[0, 1],N.corrcoef(tem_oct18[2],tem_oct18[9])[0, 1],N.corrcoef(tem_oct19[2],tem_oct19[9])[0, 1],N.corrcoef(tem_oct20[2],tem_oct20[9])[0, 1]
,N.corrcoef(tem_oct21[2],tem_oct21[9])[0, 1],N.corrcoef(tem_oct22[2],tem_oct22[9])[0, 1],N.corrcoef(tem_oct23[2],tem_oct23[9])[0, 1],N.corrcoef(tem_oct24[2],tem_oct24[9])[0, 1]]


# diciembre
tem_dic = tem[tem.index.month == 12]
tem_dic1 = tem_dic.loc[(tem_dic[0] == 1)]
tem_dic2 = tem_dic.loc[(tem_dic[0] == 2)]
tem_dic3 = tem_dic.loc[(tem_dic[0] == 3)]
tem_dic4 = tem_dic.loc[(tem_dic[0] == 4)]
tem_dic5 = tem_dic.loc[(tem_dic[0] == 5)]
tem_dic6 = tem_dic.loc[(tem_dic[0] == 6)]
tem_dic7 = tem_dic.loc[(tem_dic[0] == 7)]
tem_dic8 = tem_dic.loc[(tem_dic[0] == 8)]
tem_dic9 = tem_dic.loc[(tem_dic[0] == 9)]
tem_dic10 = tem_dic.loc[(tem_dic[0] == 10)]
tem_dic11 = tem_dic.loc[(tem_dic[0] == 11)]
tem_dic12 = tem_dic.loc[(tem_dic[0] == 12)]
tem_dic13 = tem_dic.loc[(tem_dic[0] == 13)]
tem_dic14 = tem_dic.loc[(tem_dic[0] == 14)]
tem_dic15 = tem_dic.loc[(tem_dic[0] == 15)]
tem_dic16 = tem_dic.loc[(tem_dic[0] == 16)]
tem_dic17 = tem_dic.loc[(tem_dic[0] == 17)]
tem_dic18 = tem_dic.loc[(tem_dic[0] == 18)]
tem_dic19 = tem_dic.loc[(tem_dic[0] == 19)]
tem_dic20 = tem_dic.loc[(tem_dic[0] == 20)]
tem_dic21 = tem_dic.loc[(tem_dic[0] == 21)]
tem_dic22 = tem_dic.loc[(tem_dic[0] == 22)]
tem_dic23 = tem_dic.loc[(tem_dic[0] == 23)]
tem_dic24 = tem_dic.loc[(tem_dic[0] == 24)]

corr_dic_t = [N.corrcoef(tem_dic1[2],tem_dic1[9])[0, 1],N.corrcoef(tem_dic2[2],tem_dic2[9])[0, 1],N.corrcoef(tem_dic3[2],tem_dic3[9])[0, 1],N.corrcoef(tem_dic4[2],tem_dic4[9])[0, 1],N.corrcoef(tem_dic5[2],tem_dic5[9])[0, 1]
,N.corrcoef(tem_dic6[2],tem_dic6[9])[0, 1],N.corrcoef(tem_dic7[2],tem_dic7[9])[0, 1],N.corrcoef(tem_dic8[2],tem_dic8[9])[0, 1],N.corrcoef(tem_dic9[2],tem_dic9[9])[0, 1],N.corrcoef(tem_dic10[2],tem_dic10[9])[0, 1]
,N.corrcoef(tem_dic11[2],tem_dic11[9])[0, 1],N.corrcoef(tem_dic12[2],tem_dic12[9])[0, 1],N.corrcoef(tem_dic13[2],tem_dic13[9])[0, 1],N.corrcoef(tem_dic14[2],tem_dic14[9])[0, 1],N.corrcoef(tem_dic15[2],tem_dic15[9])[0, 1]
,N.corrcoef(tem_dic16[2],tem_dic16[9])[0, 1],N.corrcoef(tem_dic17[2],tem_dic17[9])[0, 1],N.corrcoef(tem_dic18[2],tem_dic18[9])[0, 1],N.corrcoef(tem_dic19[2],tem_dic19[9])[0, 1],N.corrcoef(tem_dic20[2],tem_dic20[9])[0, 1]
,N.corrcoef(tem_dic21[2],tem_dic21[9])[0, 1],N.corrcoef(tem_dic22[2],tem_dic22[9])[0, 1],N.corrcoef(tem_dic23[2],tem_dic23[9])[0, 1],N.corrcoef(tem_dic24[2],tem_dic24[9])[0, 1]]

fig, ((ax1,ax2),(ax3,ax4),(ax5,ax6),(ax7,ax8)) = plt.subplots(4, 2,figsize=(6,7.5), sharex=True, sharey=True)

ax1.bar(horas, corr_abr_t, width=1, edgecolor="white", linewidth=0.7 , alpha = 0.8, color="tomato" )
ax1.tick_params(axis='y', labelsize=14)
ax1.set_ylim(-1,1)
ax1.set_yticks([-0.5, 0, 0.5]) 
ax1.xaxis.set_tick_params(labelsize=0, color='white')
ax1.text(0.5, 0.5, 'abril', fontsize=15)
ax1.axhline(linewidth=1, color='black')
ax1.set_title('temperatura', fontsize=15)

ax3.bar(horas, corr_jul_t, width=1, edgecolor="white", linewidth=0.7, alpha = 0.8, color="tomato" )
ax3.tick_params(axis='y', labelsize=14)
ax3.set_ylim(-1,1)
ax3.set_yticks([-0.5, 0, 0.5]) 
ax3.xaxis.set_tick_params(labelsize=0, color='white')
ax3.text(0.5, 0.5, 'julio', fontsize=15)
ax3.axhline(linewidth=1, color='black')

ax5.bar(horas, corr_oct_t, width=1, edgecolor="white", linewidth=0.7, alpha = 0.8 , color="tomato" )
ax5.tick_params(axis='y', labelsize=15)
ax5.set_ylim(-1,1)
ax5.set_yticks([-0.5, 0, 0.5]) 
ax5.xaxis.set_tick_params(labelsize=0, color='white')
ax5.text(0.5, -0.6, 'octubre', fontsize=16)
ax5.axhline(linewidth=1, color='black')

ax7.bar(horas, corr_dic_t, width=1, edgecolor="white", linewidth=0.7 , alpha = 0.8, color="tomato" )
ax7.tick_params(axis='y', labelsize=14)
ax7.tick_params(axis='x', labelsize=14,labelrotation = 90)
ax7.set_ylim(-1,1)
ax7.set_yticks([-0.5, 0, 0.5]) 
ax7.text(0.5, -0.6, 'diciembre', fontsize=15)
ax7.axhline(linewidth=1, color='black')

ax2.bar(horas, corr_abr_n, width=1, edgecolor="white", linewidth=0.7 , alpha = 0.8, color="dimgray")
ax2.tick_params(axis='y', labelsize=14)
ax2.set_ylim(-1,1)
ax2.set_yticks([-0.5, 0, 0.5]) 
ax2.xaxis.set_tick_params(labelsize=0, color='white')
ax2.text(0.5, 0.5, 'abril', fontsize=15)
ax2.axhline(linewidth=1, color='black')
ax2.set_title('nubosidad', fontsize=15)

ax4.bar(horas, corr_jul_n, width=1, edgecolor="white", linewidth=0.7, alpha = 0.8, color="dimgray")
ax4.tick_params(axis='y', labelsize=14)
ax4.set_ylim(-1,1)
ax4.set_yticks([-0.5, 0, 0.5]) 
ax4.xaxis.set_tick_params(labelsize=0, color='white')
ax4.text(0.5, 0.5, 'julio', fontsize=15)
ax4.axhline(linewidth=1, color='black')

ax6.bar(horas, corr_oct_n, width=1, edgecolor="white", linewidth=0.7, alpha = 0.8, color="dimgray" )
ax6.tick_params(axis='y', labelsize=15)
ax6.set_ylim(-1,1)
ax6.set_yticks([-0.5, 0, 0.5]) 
ax6.xaxis.set_tick_params(labelsize=0, color='white')
ax6.text(0.5, -0.6, 'octubre', fontsize=16)
ax6.axhline(linewidth=1, color='black')

ax8.bar(horas, corr_dic_n, width=1, edgecolor="white", linewidth=0.7 , alpha = 0.8, color="dimgray")
ax8.tick_params(axis='y', labelsize=14)
ax8.tick_params(axis='x', labelsize=14,labelrotation = 90)
ax8.set_ylim(-1,1)
ax8.set_yticks([-0.5, 0, 0.5]) 
ax8.text(0.5, -0.6, 'diciembre', fontsize=15)
ax8.axhline(linewidth=1, color='black')


# ~ ax4.set_xticks([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24], ['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24'])
ax4.set_xticks([1,6,12,18,24], ['1','6','12','18','24'])

# ~ ax4.set_xlabel('Horas', fontsize=15)

fig.subplots_adjust(hspace=0.05,wspace=0.05)
fig.text(-0.03, 0.5, 'coef. correlación []', va='center', rotation='vertical',fontsize=15)  
fig.text(0.45, 0.04, 'horas', va='center',fontsize=15)  

# ~ kdeplot = sns.regplot(ax=ax,x = cld[6], y = cld[2], scatter_kws = {"color": "black", "alpha": 0.3},line_kws = {"color": "black"}, ci= None, label=None)
plt.savefig('corr.jpg', dpi=300, bbox_inches="tight")


