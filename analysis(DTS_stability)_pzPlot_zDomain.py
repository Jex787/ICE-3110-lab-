import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import tf2zpk

# Define a function for z-plane plot
def zplane(num, den, title):
    # Compute poles and zeros
    zeros, poles, _ = tf2zpk(num, den)
    
    # Plot
    plt.figure(figsize=(8, 6))
    plt.scatter(np.real(zeros), np.imag(zeros), color='blue', marker='o', label='Zeros')
    plt.scatter(np.real(poles), np.imag(poles), color='red', marker='x', label='Poles')
    
    # Draw unit circle for reference
    unit_circle = plt.Circle((0, 0), 1, color='black', fill=False, linestyle='--', linewidth=1)
    plt.gca().add_patch(unit_circle)
    
    plt.axhline(0, color='black', linewidth=0.5)
    plt.axvline(0, color='black', linewidth=0.5)
    plt.xlabel("Real Part")
    plt.ylabel("Imaginary Part")
    plt.title(title)
    plt.legend()
    plt.grid()
    plt.axis('equal')
    plt.show()

# Define the systems
# System a: H(z) = (1 + z^(-2)) / (2 + z^(-1) - 0.5z^(-2) + 0.25z^(-3))
num_a = [1, 0, 1]             # Numerator coefficients for H(z) in system a
den_a = [2, 1, -0.5, 0.25]    # Denominator coefficients for H(z) in system a

# System b: H(z) = (1 + z^(-1) + 1.5*z^(-2) + 0.5*z^(-3)) / (1 + 1.5*z^(-1) + 0.5*z^(-2))
num_b = [1, 1, 1.5, 0.5]      # Numerator coefficients for H(z) in system b
den_b = [1, 1.5, 0.5]         # Denominator coefficients for H(z) in system b

# Plot poles and zeros for each system
zplane(num_a, den_a, "Poles and Zeros of H(z) for System a")
zplane(num_b, den_b, "Poles and Zeros of H(z) for System b")
