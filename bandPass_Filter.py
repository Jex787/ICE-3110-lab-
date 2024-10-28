import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import firwin, freqz

# Define filter specifications
M = 32  # Filter length
fs = 1  # Sampling frequency (normalized for design, so fs=1)
fp1, fp2 = 0.2, 0.35  # Passband edge frequencies
fs1, fs2 = 0.1, 0.425  # Stopband edge frequencies

# Calculate the cutoff frequencies for firwin
cutoff = [fp1, fp2]

# Design the FIR bandpass filter
filter_coefficients = firwin(M, cutoff, pass_zero=False, fs=fs)

# Frequency response
w, h = freqz(filter_coefficients, worN=8000)

# Plot frequency response
plt.figure(figsize=(12, 6))
plt.plot(w / np.pi, 20 * np.log10(np.abs(h)), label='Magnitude Response (dB)')
plt.axvline(fp1, color='green', linestyle='--', label="Passband Edge fp1")
plt.axvline(fp2, color='green', linestyle='--', label="Passband Edge fp2")
plt.axvline(fs1, color='red', linestyle='--', label="Stopband Edge fs1")
plt.axvline(fs2, color='red', linestyle='--', label="Stopband Edge fs2")
plt.xlabel('Normalized Frequency (×π rad/sample)')
plt.ylabel('Magnitude (dB)')
plt.title('Frequency Response of the Bandpass Filter')
plt.grid()
plt.legend()
plt.show()
