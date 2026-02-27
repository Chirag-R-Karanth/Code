import numpy as np
import matplotlib.pyplot as plt

# Characteristic polynomial coefficients depend on K
def root_locus(K):
    coeff = [1, 9, 8, K]  # s^3 + 9 s^2 + 8 s + K
    return np.roots(coeff)

Ks = np.linspace(0, 500, 400)  # K range
all_roots = np.array([root_locus(K) for K in Ks])

plt.figure(figsize=(6,6))
plt.plot(all_roots.real, all_roots.imag, '.', markersize=3)
plt.axhline(0)
plt.axvline(0)
plt.title("Root Locus of K/(s(s+1)(s+8))")
plt.xlabel("Real Axis")
plt.ylabel("Imaginary Axis")
plt.grid(True)
plt.show()
