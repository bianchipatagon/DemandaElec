import pywt
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('/home/emi/Documents/MAESTRIA/14-Metodología/DATOS/arg-dem.txt', header=None, delimiter=';')
df.index= pd.date_range(start='2007-01-01', end='2022-12-31', freq = 'D')
signal = df[3]

n = len(signal)  # 128

    # In the PyWavelets implementation, scale 1 corresponds to a wavelet with
    # domain [-8, 8], which means that it covers 17 samples (upper - lower + 1).
    # Scale s corresponds to a wavelet with s*17 samples.
    # The scales in scale_list range from 1 to 16.75. The widest wavelet is
    # 17*16.75 = 284.75 wide, which is just over double the size of the signal.
scale_list = np.arange(start=0, stop=n) / 8 + 1  # 128
wavelet = "mexh"
coefficients, frequencies = pywt.cwt(signal, scale_list, wavelet)
plt.subplot(2, 1, 2)

plt.imshow(np.abs(coefficients), 
           cmap='viridis', aspect='auto', interpolation='bilinear')
plt.colorbar(label='|CWT Coefficients|')
plt.title('Scaleogram')
plt.xlabel('Time (s)')
plt.ylabel('Frequency (Hz)')
plt.yscale('log')  # Log scale often works better for frequency visualization

plt.tight_layout()
plt.show()
