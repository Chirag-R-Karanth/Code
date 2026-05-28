import matplotlib.pyplot as plt
import numpy as np

# Sampling frequency
fs = 50000

# Time vector
t = np.linspace(0, 0.01, int(fs * 0.01))

# Generate signals
x1 = np.sin(2 * np.pi * 400 * t)
x2 = np.sin(2 * np.pi * 4000 * t)

# Autocorrelation
auto_x1 = np.correlate(x1, x1, mode="full")
auto_x2 = np.correlate(x2, x2, mode="full")

# Lag axis
lags = np.arange(-len(x1) + 1, len(x1))

# Plotting
plt.figure(figsize=(12, 8))

# 400 Hz signal
plt.subplot(2, 2, 1)
plt.plot(t, x1)
plt.title("400 Hz Signal")
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")
plt.grid(True)

# 4000 Hz signal
plt.subplot(2, 2, 2)
plt.plot(t, x2)
plt.title("4000 Hz Signal")
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")
plt.grid(True)

# Autocorrelation of 400 Hz
plt.subplot(2, 2, 3)
plt.plot(lags, auto_x1)
plt.title("Autocorrelation of 400 Hz Signal")
plt.xlabel("Lag")
plt.ylabel("Correlation")
plt.grid(True)

# Autocorrelation of 4000 Hz
plt.subplot(2, 2, 4)
plt.plot(lags, auto_x2)
plt.title("Autocorrelation of 4000 Hz Signal")
plt.xlabel("Lag")
plt.ylabel("Correlation")
plt.grid(True)

plt.tight_layout()
plt.show()
