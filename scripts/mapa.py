import cartopy.crs as ccrs
from cartopy.mpl.ticker import LongitudeFormatter, LatitudeFormatter
import matplotlib.pyplot as plt
import cartopy.feature as cfeature
from cartopy.feature import ShapelyFeature
from cartopy.io.shapereader import Reader
from matplotlib.patches import Rectangle
import pandas as pd
import geopandas as gpd
import matplotlib.colors as mcolors
import numpy as np
import matplotlib as mpl
from matplotlib.patches import Patch


Argentina = gpd.read_file('/home/emi/Documents/MAESTRIA/14-Metodología/DemandaElec/scripts/provincia/provinciaPolygon.shp')
GBA = gpd.read_file('/home/emi/Documents/MAESTRIA/14-Metodología/DemandaElec/scripts/AMBA/AMBA.shp')
GBA = GBA.dissolve()

Patagonia = Argentina.iloc[[10, 11, 20]]
Patagonia = Patagonia.dissolve()

Comahue = Argentina.iloc[[7, 13, 15]]
Comahue = Comahue.dissolve()

BsAs = Argentina.iloc[[19]]
BsAs = BsAs.dissolve()

Cuyo = Argentina.iloc[[3,12]]
Cuyo = Cuyo.dissolve()

Centro = Argentina.iloc[[1,6]]
Centro = Centro.dissolve()

Litoral = Argentina.iloc[[21,22]]
Litoral = Litoral.dissolve()

NOA = Argentina.iloc[[16,17,18,4,5,2]]
NOA = NOA.dissolve()

NEA = Argentina.iloc[[8,9,14,23]]
NEA = NEA.dissolve()

fig, ax = plt.subplots( 1,1, figsize=(10, 10))
Patagonia.plot(ax=ax, color='lightsteelblue', linewidth=1, alpha=0.9,edgecolor='grey')
Cuyo.plot(ax=ax, color='lightsteelblue', linewidth=1, alpha=0.9,edgecolor='grey')
Comahue.plot(ax=ax, color='lightsteelblue', linewidth=1, alpha=0.9,edgecolor='grey',label = '< 10000 GWh')

NOA.plot(ax=ax, color='cornflowerblue', linewidth=1, alpha=0.9,edgecolor='grey')
NEA.plot(ax=ax, color='cornflowerblue', linewidth=1, alpha=0.9,edgecolor='grey')
Centro.plot(ax=ax, color='cornflowerblue', linewidth=1, alpha=0.9,edgecolor='grey',label = '< 15000 GWh')

BsAs.plot(ax=ax, color='mediumblue', linewidth=1, alpha=0.9,edgecolor='grey')
Litoral.plot(ax=ax, color='mediumblue', linewidth=1, alpha=0.9,edgecolor='grey',label = '< 20000 GWh')

GBA.plot(ax=ax, color='darkblue', linewidth=1, alpha=0.9,edgecolor='grey',label = '< 52000 GWh')

ax.set_ylim(-58, -20)
ax.set_xlim(-74, -50)
ax.tick_params(axis='both', labelsize=16)
ax.text(-71,-45, 'Patagonia \n 4.5%')
ax.text(-70,-40, 'Comahue \n 3.7%')
ax.text(-63,-37, 'Buenos Aires \n 11.9%',color = 'white')
# ~ ax.text(-62,-37, 'Buenos Aires \n 11.9%')
ax.text(-66,-34, 'Centro \n 8.9%')
ax.text(-70,-33, 'Cuyo \n 6.1%')
ax.text(-61.5,-32, 'Litoral \n 11.8%',color = 'white')
ax.text(-67,-27, 'NOA \n 8.6%')
ax.text(-61,-26, 'NEA \n 7.7%')
ax.text(-58,-34, 'GBA \n 36.7%')

legend_elements = [
    Patch(facecolor='lightsteelblue', edgecolor='grey', label='< 10000 GWh'),
    Patch(facecolor='cornflowerblue', edgecolor='grey', label='< 15000 GWh'),
    Patch(facecolor='mediumblue', edgecolor='grey', label='< 20000 GWh'),
    Patch(facecolor='darkblue', edgecolor='grey', label='< 52000 GWh')
]

ax.legend(handles=legend_elements, fontsize=13, frameon=False, loc='center', bbox_to_anchor=(0.73, 0.27))

plt.savefig('mapa.png', dpi=600, bbox_inches="tight")

