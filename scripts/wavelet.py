import numpy as np
import matplotlib.pyplot as plt
import pywt
import pandas as pd

df = pd.read_csv('/home/emi/Documents/MAESTRIA/14-Metodología/DATOS/arg-dem.txt', header=None, delimiter=';')
df.index= pd.date_range(start='2007-01-01', end='2022-12-31', freq = 'D')

# Generate a sample signal with multiple frequency components
t = np.linspace(0, 4, 1000)
print(t)
t1 = list(range(len(df) ))
print(t1)

signal = df[3]

# Define the scales for the CWT
# Scales relate to frequencies - smaller scales = higher frequencies
scales = np.arange(1, 128)

# Choose a wavelet - 'cmor' (Complex Morlet) is good for frequency analysis
# The format is 'cmorB-C' where B is bandwidth and C is center frequency
wavelet = 'cmor1.5-1.0'

# Perform Continuous Wavelet Transform
coefficients, frequencies = pywt.cwt(signal, scales, wavelet, sampling_period=t1[1]-t1[0])

# Create the scaleogram
plt.figure(figsize=(12, 8))

# Plot the original signal
plt.subplot(2, 1, 1)
plt.plot(t1, signal)
plt.title('Original Signal')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.grid(True)

# Plot the scaleogram
plt.subplot(2, 1, 2)
plt.imshow(np.abs(coefficients), extent=[t1[0], t1[-1], frequencies[-1], frequencies[0]], 
           cmap='viridis', aspect='auto', interpolation='bilinear')
plt.colorbar(label='|CWT Coefficients|')
plt.title('Scaleogram')
plt.xlabel('Time (s)')
plt.ylabel('Frequency (Hz)')
plt.yscale('log')  # Log scale often works better for frequency visualization

plt.tight_layout()
plt.show()

