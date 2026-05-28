import matplotlib.pyplot as plt
import numpy as np

# Sampling parameters
fs = 1000
t = np.linspace(0, 1, fs)

# Generate two sinusoidal signals
x1 = np.sin(2 * np.pi * 5 * t)
x2 = np.sin(2 * np.pi * 10 * t)

# Autocorrelation
auto_x1 = np.correlate(x1, x1, mode="full")
auto_x2 = np.correlate(x2, x2, mode="full")

# Cross-correlation
cross_corr = np.correlate(x1, x2, mode="full")

# Lag axis
lags = np.arange(-len(x1) + 1, len(x1))

# Plotting
plt.figure(figsize=(12, 10))

# Signal 1
plt.subplot(4, 1, 1)
plt.plot(t, x1)
plt.title("Signal 1 (5 Hz)")
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")
plt.grid(True)

# Signal 2
plt.subplot(4, 1, 2)
plt.plot(t, x2)
plt.title("Signal 2 (10 Hz)")
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")
plt.grid(True)

# Autocorrelation
plt.subplot(4, 1, 3)
plt.plot(lags, auto_x1, label="Auto x1")
plt.plot(lags, auto_x2, label="Auto x2")
plt.title("Autocorrelation")
plt.xlabel("Lag")
plt.ylabel("Correlation")
plt.legend()
plt.grid(True)

# Cross-correlation
plt.subplot(4, 1, 4)
plt.plot(lags, cross_corr)
plt.title("Cross-Correlation between x1 and x2")
plt.xlabel("Lag")
plt.ylabel("Correlation")
plt.grid(True)

plt.tight_layout()
plt.show()
