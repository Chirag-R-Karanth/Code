import numpy as np
import matplotlib.pyplot as plt

# Sampling frequency
fs = 50000

# Time vector
t = np.linspace(0, 0.01, int(fs * 0.01))

# Generate signals
x1 = np.sin(2 * np.pi * 400 * t)     # 400 Hz signal
x2 = np.sin(2 * np.pi * 4000 * t)    # 4000 Hz signal

# Convolution
conv_signal = np.convolve(x1, x2, mode='full')

# Time axis for convolution signal
t_conv = np.linspace(0, 2 * 0.01, len(conv_signal))

# Plotting
plt.figure(figsize=(12, 8))

# First signal
plt.subplot(3, 1, 1)
plt.plot(t, x1)
plt.title("400 Hz Sinusoidal Signal")
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")
plt.grid(True)

# Second signal
plt.subplot(3, 1, 2)
plt.plot(t, x2)
plt.title("4000 Hz Sinusoidal Signal")
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")
plt.grid(True)

# Convolution signal
plt.subplot(3, 1, 3)
plt.plot(t_conv, conv_signal)
plt.title("Convolution of 400 Hz and 4000 Hz Signals")
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")
plt.grid(True)

plt.tight_layout()
plt.show()
