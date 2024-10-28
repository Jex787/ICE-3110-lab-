import numpy as np
import matplotlib.pyplot as plt

# Define parameters for signal generation
fs = 500  # Sampling frequency (Hz)
T = 1     # Duration in seconds
t = np.linspace(0, T, int(fs * T), endpoint=False)  # Time vector

# Generate a signal with two frequencies
f1, f2 = 50, 120  # Frequencies in Hz
signal = 0.6 * np.sin(2 * np.pi * f1 * t) + 0.4 * np.sin(2 * np.pi * f2 * t)

# Compute FFT
N = len(signal)
fft_values = np.fft.fft(signal)
fft_magnitude = np.abs(fft_values) / N  # Magnitude normalization
fft_magnitude = fft_magnitude[:N // 2]  # Take the positive frequency part

# Frequency vector for plotting
frequencies = np.fft.fftfreq(N, 1 / fs)[:N // 2]

# Plotting
plt.figure(figsize=(12, 6))

# Plot time-domain signal
plt.subplot(2, 1, 1)
plt.plot(t, signal)
plt.title("Time-Domain Signal")
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")

# Plot frequency spectrum (magnitude)
plt.subplot(2, 1, 2)
plt.stem(frequencies, fft_magnitude, basefmt=" ")  # Removed 'use_line_collection'
plt.title("Frequency-Domain Representation (FFT)")
plt.xlabel("Frequency (Hz)")
plt.ylabel("Magnitude")

plt.tight_layout()
plt.show()
