import numpy as np
from scipy.fft import fft, rfft
from scipy.fft import fftfreq, rfftfreq
# ~ import plotly.graph_objs as go
# ~ from plotly.subplots import make_subplots
import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('/home/emi/Documents/MAESTRIA/14-Metodología/DATOS/arg-dem.txt', header=None, delimiter=';')
df.index= pd.date_range(start='2007-01-01', end='2022-12-31', freq = 'D')
print(df)

# Apply the FFT on the signal
fourier = fft(df[3])

# Plot the result (the spectrum |Xk|)
plt.plot(np.abs(fourier))
plt.show()

N = len(df[3])
normalize = N/2

# Plot the normalized FFT (|Xk|)/(N/2)
plt.plot(np.abs(fourier)/normalize)
plt.ylabel('Amplitude')
plt.xlabel('Samples')
plt.title('Normalized FFT Spectrum')
plt.show()

