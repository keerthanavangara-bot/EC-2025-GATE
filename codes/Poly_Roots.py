import numpy as np
import matplotlib.pyplot as plt
import subprocess, shlex

coeffs = [1, 7, 3, -33, 2, -40]
roots = np.roots(coeffs)

fig, ax = plt.subplots(figsize=(6, 4))
ax.plot(roots.real, roots.imag, 'bs', markersize=8)
ax.axvline(0, color='k', linestyle='--')
ax.set_xlabel('Real')
ax.set_ylabel('Imaginary')
ax.set_title('Polynomial Roots (L=2, I=2, R=1) (Q.37)')
ax.grid(True)
plt.tight_layout()
plt.savefig("figs/Poly_Roots.png")
