import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import firwin, freqz

# Define filter specifications
M = 32  # Filter length
fs = 1  # Sampling frequency (normalized for design, so fs=1)
fpb1, fpb2 = 0.2, 0.35  # Passband edge frequencies
fsb1, fsb2 = 0.1, 0.425  # Stopband edge frequencies

# Calculate the cutoff frequencies for firwin
cutoff = [fpb1, fpb2]

# Design the FIR bandpass filter
filter_coefficients = firwin(M, cutoff, pass_zero=False, fs=fs)

# Frequency response
w, h = freqz(filter_coefficients, worN=8000)

# Plot frequency response
plt.figure(figsize=(12, 6))
plt.plot(w / np.pi, 20 * np.log10(np.abs(h)), label='Magnitude Response (dB)')
plt.axvline(fpb1, color='green', linestyle='--', label="Passband Edge fpb1")
plt.axvline(fpb2, color='green', linestyle='--', label="Passband Edge fpb2")
plt.axvline(fsb1, color='red', linestyle='--', label="Stopband Edge fsb1")
plt.axvline(fsb2, color='red', linestyle='--', label="Stopband Edge fsb2")
plt.xlabel('Normalized Frequency (×π rad/sample)')
plt.ylabel('Magnitude (dB)')
plt.title('Frequency Response of the Bandpass Filter')
plt.grid()
plt.legend()
plt.show()
