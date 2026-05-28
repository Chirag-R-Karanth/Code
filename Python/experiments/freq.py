import librosa
import librosa.display
import matplotlib.pyplot as plt
import numpy as np

# ------------------------------------------------
# Load WAV File
# ------------------------------------------------

audio_path = "/home/neo_phantom_byte/Documents/Study/RVCE/Notes/4th Semester/Signals And Systems/Signal and systems lab/images/pwlpl-car-engine-start-sound-effect-521106.wav"  # Replace with your file name

x, fs = librosa.load(audio_path, sr=None)

# ------------------------------------------------
# FFT COMPUTATION
# ------------------------------------------------

N = len(x)

fft_signal = np.fft.fft(x)

magnitude = np.abs(fft_signal)

frequency = np.fft.fftfreq(N, d=1 / fs)

# Keep only positive frequencies
positive_freqs = frequency[: N // 2]
positive_magnitude = magnitude[: N // 2]

# ------------------------------------------------
# FREQUENCY DOMAIN FEATURES
# ------------------------------------------------

# Spectral Centroid
spectral_centroid = librosa.feature.spectral_centroid(y=x, sr=fs)

# Spectral Bandwidth
spectral_bandwidth = librosa.feature.spectral_bandwidth(y=x, sr=fs)

# Spectral Rolloff
spectral_rolloff = librosa.feature.spectral_rolloff(y=x, sr=fs)

# Spectral Contrast
spectral_contrast = librosa.feature.spectral_contrast(y=x, sr=fs)

# ------------------------------------------------
# PRINT FEATURES
# ------------------------------------------------

print("FREQUENCY DOMAIN FEATURES")
print("--------------------------------")

print("Sampling Rate          :", fs, "Hz")

print("Mean Spectral Centroid :", np.mean(spectral_centroid))

print("Mean Spectral Bandwidth:", np.mean(spectral_bandwidth))

print("Mean Spectral Rolloff  :", np.mean(spectral_rolloff))

print("Spectral Contrast Shape:", spectral_contrast.shape)

# ------------------------------------------------
# PLOTTING
# ------------------------------------------------

fig, axs = plt.subplots(5, 1, figsize=(12, 15))

# ------------------------------------------------
# 1. Original Signal
# ------------------------------------------------

axs[0].plot(x)

axs[0].set_title("Original Audio Signal")
axs[0].set_xlabel("Samples")
axs[0].set_ylabel("Amplitude")

axs[0].grid(True)

# ------------------------------------------------
# 2. FFT Spectrum
# ------------------------------------------------

axs[1].plot(positive_freqs, positive_magnitude)

axs[1].set_title("FFT Spectrum")

axs[1].set_xlabel("Frequency (Hz)")
axs[1].set_ylabel("Magnitude")

axs[1].grid(True)

# ------------------------------------------------
# 3. Spectral Centroid
# ------------------------------------------------

axs[2].plot(spectral_centroid.T)

axs[2].set_title("Spectral Centroid")

axs[2].set_xlabel("Frames")
axs[2].set_ylabel("Hz")

axs[2].grid(True)

# ------------------------------------------------
# 4. Spectral Bandwidth
# ------------------------------------------------

axs[3].plot(spectral_bandwidth.T)

axs[3].set_title("Spectral Bandwidth")

axs[3].set_xlabel("Frames")
axs[3].set_ylabel("Bandwidth")

axs[3].grid(True)

# ------------------------------------------------
# 5. Spectral Rolloff
# ------------------------------------------------

axs[4].plot(spectral_rolloff.T)

axs[4].set_title("Spectral Rolloff")

axs[4].set_xlabel("Frames")
axs[4].set_ylabel("Hz")

axs[4].grid(True)

plt.tight_layout()

plt.show()
