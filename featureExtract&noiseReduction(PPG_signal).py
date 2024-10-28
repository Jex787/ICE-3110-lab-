import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import butter, filtfilt, find_peaks

# Generate synthetic PPG signal (for demonstration)
# Sampling frequency
fs = 100  # Hz
t = np.linspace(0, 10, fs * 10)  # 10 seconds of data
# Create a synthetic PPG signal with a frequency of 1.2 Hz (about 72 BPM)
ppg_signal = 1.0 * np.sin(2 * np.pi * 1.2 * t) + 0.05 * np.random.randn(len(t))  # Add small random noise

# Butterworth bandpass filter for noise reduction
def bandpass_filter(signal, lowcut, highcut, fs, order=4):
    nyquist = 0.5 * fs
    low = lowcut / nyquist
    high = highcut / nyquist
    b, a = butter(order, [low, high], btype='band')
    y = filtfilt(b, a, signal)
    return y

# Filter settings for PPG signal (0.5-5 Hz band)
lowcut = 0.5  # Lower frequency cutoff in Hz
highcut = 5.0 # Higher frequency cutoff in Hz

# Apply bandpass filter to reduce noise
filtered_ppg = bandpass_filter(ppg_signal, lowcut, highcut, fs)

# Peak detection for feature extraction
peaks, _ = find_peaks(filtered_ppg, distance=fs/2)  # Distance set to avoid multiple peaks per pulse

# Plotting
plt.figure(figsize=(12, 8))

# Plot original noisy PPG signal
plt.subplot(3, 1, 1)
plt.plot(t, ppg_signal, color='gray')
plt.title("Original Noisy PPG Signal")
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")

# Plot filtered PPG signal
plt.subplot(3, 1, 2)
plt.plot(t, filtered_ppg, color='blue')
plt.title("Filtered PPG Signal (Noise Reduced)")
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")

# Plot filtered signal with detected peaks
plt.subplot(3, 1, 3)
plt.plot(t, filtered_ppg, color='blue', label="Filtered PPG Signal")
plt.plot(t[peaks], filtered_ppg[peaks], "ro", label="Detected Peaks")
plt.title("Feature Extraction (Peak Detection)")
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")
plt.legend()

plt.tight_layout()
plt.show()
