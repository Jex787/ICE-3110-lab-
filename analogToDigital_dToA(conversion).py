import numpy as np
import matplotlib.pyplot as plt
from scipy.fft import fft, fftfreq
from scipy.signal import resample

# Parameters
fs = 1000  # Sampling rate (Hz)
T = 1.0    # Duration of the signal in seconds
t = np.linspace(0, T, int(fs * T), endpoint=False)  # Time vector

# Generate an analog signal (combination of 5 Hz and 50 Hz sine waves)
f1, f2 = 5, 50
analog_signal = np.sin(2 * np.pi * f1 * t) + 0.5 * np.sin(2 * np.pi * f2 * t)

# Perform ADC - Sampling the analog signal
sampling_rate = 200  # Sampling rate for ADC (Hz)
t_sampled = np.linspace(0, T, int(sampling_rate * T), endpoint=False)
digital_signal = np.sin(2 * np.pi * f1 * t_sampled) + 0.5 * np.sin(2 * np.pi * f2 * t_sampled)

# DAC - Reconstruction by resampling to the original rate
reconstructed_signal = resample(digital_signal, len(t))

# FFT of the sampled signal
fft_values = fft(digital_signal)
fft_freqs = fftfreq(len(digital_signal), 1 / sampling_rate)

# Plotting
plt.figure(figsize=(12, 10))

# Original Analog Signal
plt.subplot(3, 1, 1)
plt.plot(t, analog_signal, label="Original Analog Signal", color="blue")
plt.xlabel("Time [s]", fontsize=12)
plt.ylabel("Amplitude", fontsize=12)
plt.title("Original Analog Signal", fontsize=14)
plt.legend()
plt.grid()

# Digital Signal after ADC (Sampled)
plt.subplot(3, 1, 2)
plt.stem(t_sampled, digital_signal, basefmt=" ", markerfmt="ro", label="Sampled Digital Signal (ADC)")
plt.xlabel("Time [s]", fontsize=12)
plt.ylabel("Amplitude", fontsize=12)
plt.title("Digital Signal after ADC", fontsize=14)
plt.legend()
plt.grid()

# Reconstructed Signal (DAC)
plt.subplot(3, 1, 3)
plt.plot(t, reconstructed_signal, label="Reconstructed Analog Signal (DAC)", color="green")
plt.xlabel("Time [s]", fontsize=12)
plt.ylabel("Amplitude", fontsize=12)
plt.title("Reconstructed Signal after DAC", fontsize=14)
plt.legend()
plt.grid()

# Adjust layout to prevent overlap
plt.tight_layout(pad=3.0)

plt.show()


