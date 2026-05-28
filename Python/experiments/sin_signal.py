import numpy as np
import matplotlib.pyplot as plt

# Parameters
A = 1          # Amplitude
f = 5          # Frequency in Hz
fs = 1000      # Sampling frequency
t = np.linspace(0, 1, fs)

# Generate sinusoidal signal
x = A * np.sin(2 * np.pi * f * t)

# Plot
plt.figure(figsize=(10, 4))
plt.plot(t, x)
plt.title("Sinusoidal Signal")
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")
plt.grid(True)
plt.show()
