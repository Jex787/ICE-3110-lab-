import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import firwin, freqz

# Define filter specifications
M = 61            # Filter length
fpb = 0.1          # Passband edge frequency (normalized)
fsb = 0.15         # Stopband edge frequency (normalized)

# Set the cutoff frequency to the average of the passband and stopband edges
fc = (fpb + fsb) / 2

# Design the FIR lowpass filter using the Hamming window
filter_coefficients = firwin(M, fc, window='hamming', pass_zero=True)

# Frequency response
w, h = freqz(filter_coefficients, worN=8000)

# Plot frequency response
plt.figure(figsize=(12, 6))
plt.plot(w / np.pi, 20 * np.log10(np.abs(h)), label='Magnitude Response (dB)')
plt.axvline(fpb, color='green', linestyle='--', label="Passband Edge (0.1)")
plt.axvline(fsb, color='red', linestyle='--', label="Stopband Edge (0.15)")
plt.xlabel('Normalized Frequency (×π rad/sample)')
plt.ylabel('Magnitude (dB)')
plt.title('Frequency Response of the Lowpass Filter')
plt.grid()
plt.legend()
plt.show()
