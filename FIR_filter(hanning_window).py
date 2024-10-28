import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import firwin, freqz

# Define filter specifications
fs = 20000  # Sampling frequency in Hz
fp = 2000   # Passband edge frequency in Hz
fsb = 5000  # Stopband edge frequency in Hz
M = 21      # Filter length

# Normalize frequencies
normalized_fp = fp / (fs / 2)  # Normalize passband edge frequency
normalized_fsb = fsb / (fs / 2)  # Normalize stopband edge frequency

# Design the FIR filter using Hanning window
filter_coefficients = firwin(M, normalized_fp, window='hann', pass_zero=False)

# Frequency response
w, h = freqz(filter_coefficients, worN=8000)

# Plot frequency response
plt.figure(figsize=(12, 6))
plt.plot(w * fs / (2 * np.pi), 20 * np.log10(np.abs(h)), label='Magnitude Response (dB)')
plt.axvline(fp, color='green', linestyle='--', label="Passband Edge (2 kHz)")
plt.axvline(fsb, color='red', linestyle='--', label="Stopband Edge (5 kHz)")
plt.xlabel('Frequency (Hz)')
plt.ylabel('Magnitude (dB)')
plt.title('Frequency Response of the FIR Filter')
plt.grid()
plt.legend()
plt.show()
