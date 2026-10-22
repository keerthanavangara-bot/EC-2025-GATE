import numpy as np
import matplotlib.pyplot as plt

w = np.linspace(-5, 5, 500)
F_w = 2 / (1 + w**2)
bound = 2.0

fig, ax = plt.subplots(figsize=(6, 4))
ax.plot(w, F_w, label=r'$|F(\omega)| = \frac{2}{1+\omega^2}$')
ax.axhline(bound, color='r', linestyle='--', label=r'$\int_{-\infty}^{\infty} |f(t)| dt = 2$')
ax.set_xlabel(r'$\omega$')
ax.set_ylabel('Magnitude')
ax.set_title('Fourier Transform Upper Bound (Q.18)')
ax.legend()
ax.grid(True)
plt.tight_layout()
plt.savefig("figs/Fourier_Bound.png")
