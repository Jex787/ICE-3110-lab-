import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import firwin, freqz

# Define filter specifications
fs = 10000  # Sampling frequency in Hz
fp = 1500   # Passband edge frequency in Hz
transition_width = 500  # Transition width in Hz
M = 67      # Filter length

# Calculate cutoff frequency
fc = fp + transition_width / 2  # Cutoff frequency for the lowpass filter in Hz
normalized_cutoff = fc / (fs / 2)  # Normalize the cutoff frequency

# Design the lowpass filter using Blackman window
filter_coefficients = firwin(M, normalized_cutoff, window='blackman', pass_zero=True)

# Frequency response
w, h = freqz(filter_coefficients, worN=8000)

# Plot frequency response
plt.figure(figsize=(12, 6))
plt.plot(w * fs / (2 * np.pi), 20 * np.log10(np.abs(h)), label='Magnitude Response (dB)')
plt.axvline(fp, color='green', linestyle='--', label="Passband Edge (1.5 kHz)")
plt.axvline(fc, color='orange', linestyle='--', label="Cutoff Frequency (1.75 kHz)")
plt.xlabel('Frequency (Hz)')
plt.ylabel('Magnitude (dB)')
plt.title('Frequency Response of the Lowpass Filter')
plt.grid()
plt.legend()
plt.show()
