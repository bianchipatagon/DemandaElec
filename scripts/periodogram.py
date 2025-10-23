import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import numpy as np
import pandas as pd
import matplotlib.mlab as mlab

df = pd.read_csv('/home/emi/Documents/MAESTRIA/14-Metodología/DATOS/arg-dem.txt', header=None, delimiter=';')
df.index= pd.date_range(start='2007-01-01', end='2022-12-31', freq = 'D')
print(df[3].values)

prng = np.random.RandomState(19680801)  # to ensure reproducibility

fs = 1000
t = np.linspace(0, 0.3, 301)
A = np.array([2, 8]).reshape(-1, 1)
f = np.array([150, 140]).reshape(-1, 1)
xn = (A * np.exp(2j * np.pi * f * t)).sum(axis=0) + 5 * prng.randn(*t.shape)
print(xn)
fig, (ax0, ax1) = plt.subplots(ncols=2, layout='constrained')

yticks = np.arange(-15, 30, 10)
yrange = (yticks[0], yticks[-1])
xticks = np.arange(0, 550, 200)

ax0.psd(df[3].values, NFFT=301, Fs=fs, window=mlab.window_none, pad_to=1024,
        scale_by_freq=True)
ax0.set_title('Periodogram')
ax0.set_yticks(yticks)
ax0.set_xticks(xticks)
ax0.grid(True)
ax0.set_ylim(yrange)

ax1.psd(df[3].values, NFFT=150, Fs=fs, window=mlab.window_none, pad_to=512, noverlap=75,
        scale_by_freq=True)
ax1.set_title('Welch')
ax1.set_xticks(xticks)
ax1.set_yticks(yticks)
ax1.set_ylabel('')  # overwrite the y-label added by `psd`
ax1.grid(True)
ax1.set_ylim(yrange)

plt.show()
