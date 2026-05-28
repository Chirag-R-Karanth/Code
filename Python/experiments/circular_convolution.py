import numpy as np
import matplotlib.pyplot as plt
h = [1,2,3,4,5]
#input response
x = [1,2,1]
# Pad sequences to the same length
N=max(len(x), len(h))
x_padded = np.pad(x, (0, N-len(x)), mode='constant')
h_padded= np.pad(h, (0, N-len(h)), mode='constant')
# Perform circular convolution using np.fft.ifft()
X = np.fft.fft(x_padded)
H = np.fft.fft(h_padded)
Y = np.fft.ifft(X * H)
print("Circular Convolution Result:", np.real(Y))
