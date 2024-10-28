import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import TransferFunction, tf2zpk

# Function to calculate and plot poles and zeros
def plot_poles_zeros(num, den, title):
    # Calculate poles and zeros
    zeros, poles, _ = tf2zpk(num, den)
    
    # Plot
    plt.figure(figsize=(8, 6))
    plt.scatter(np.real(zeros), np.imag(zeros), color='blue', marker='o', label="Zeros")
    plt.scatter(np.real(poles), np.imag(poles), color='red', marker='x', label="Poles")
    plt.axhline(0, color='black', linewidth=0.5)
    plt.axvline(0, color='black', linewidth=0.5)
    plt.xlabel("Real Part")
    plt.ylabel("Imaginary Part")
    plt.title(title)
    plt.legend()
    plt.grid()
    plt.show()

# Define systems
# System a: H(s) = (s^3 + 1) / (s^4 + 2s^2 + 1)
num_a = [1, 0, 0, 1]       # Numerator coefficients of H(s) for system a
den_a = [1, 0, 2, 0, 1]    # Denominator coefficients of H(s) for system a

# System b: H(s) = (4s^2 + 8s + 10) / (2s^3 + 8s^2 + 18s + 20)
num_b = [4, 8, 10]         # Numerator coefficients of H(s) for system b
den_b = [2, 8, 18, 20]     # Denominator coefficients of H(s) for system b

# Plot poles and zeros for each system
plot_poles_zeros(num_a, den_a, "Poles and Zeros of H(s) for System a")
plot_poles_zeros(num_b, den_b, "Poles and Zeros of H(s) for System b")
