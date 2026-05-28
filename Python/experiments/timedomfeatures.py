import librosa
import librosa.display
import matplotlib.pyplot as plt
import numpy as np
from scipy import signal
from scipy.io import wavfile

# ------------------------------------------------
# Load WAV File
# ------------------------------------------------

audio_path = "/home/neo_phantom_byte/Documents/Study/RVCE/Notes/4th Semester/Signals And Systems/Signal and systems lab/images/pwlpl-car-engine-start-sound-effect-521106.wav"  # Replace with your file name

# librosa loads audio
x, fs = librosa.load(audio_path, sr=None)

# Time axis
t = np.linspace(0, len(x) / fs, len(x))

# ------------------------------------------------
# FEATURE EXTRACTION
# ------------------------------------------------

# Duration
duration = len(x) / fs

# Amplitude
amplitude = np.max(np.abs(x))

print("AUDIO FEATURES")
print("---------------------------")
print("Sampling Rate :", fs, "Hz")
print("Duration      :", duration, "seconds")
print("Amplitude     :", amplitude)

# ------------------------------------------------
# Create Figure
# ------------------------------------------------

fig, axs = plt.subplots(4, 1, figsize=(12, 12))

# ------------------------------------------------
# 1. Original Signal
# ------------------------------------------------

axs[0].plot(t, x)

axs[0].set_title("Audio Signal")
axs[0].set_xlabel("Time (s)")
axs[0].set_ylabel("Amplitude")

axs[0].grid(True)

# ------------------------------------------------
# 2. Spectrogram
# ------------------------------------------------

frequencies, times, Sxx = signal.spectrogram(x, fs)

im1 = axs[1].pcolormesh(times, frequencies, 10 * np.log10(Sxx), shading="gouraud")

axs[1].set_title("Spectrogram")

axs[1].set_xlabel("Time (s)")
axs[1].set_ylabel("Frequency (Hz)")

fig.colorbar(im1, ax=axs[1])

# ------------------------------------------------
# 3. MFCC
# ------------------------------------------------

mfccs = librosa.feature.mfcc(y=x, sr=fs, n_mfcc=13)

img2 = librosa.display.specshow(mfccs, x_axis="time", sr=fs, ax=axs[2])

axs[2].set_title("MFCC")

fig.colorbar(img2, ax=axs[2])

# ------------------------------------------------
# 4. Chroma Features
# ------------------------------------------------

chroma = librosa.feature.chroma_stft(y=x, sr=fs)

img3 = librosa.display.specshow(
    chroma, x_axis="time", y_axis="chroma", sr=fs, ax=axs[3]
)

axs[3].set_title("Chroma Features")

fig.colorbar(img3, ax=axs[3])

# ------------------------------------------------
# Final Layout
# ------------------------------------------------

plt.tight_layout()

plt.show()
