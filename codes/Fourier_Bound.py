import os
import numpy as np
import matplotlib.pyplot as plt
from CoordGeo.line.funcs import line_gen_num
from CoordGeo.plotting.funcs import label_pts

os.makedirs("figs", exist_ok=True)

w = np.linspace(-5, 5, 500)
F = np.vstack((w, 2 / (1 + w**2)))
bound = line_gen_num(np.array([[-5], [2]]), np.array([[5], [2]]), 2)
P = np.array([[0.0], [2.0]])

fig, ax = plt.subplots(figsize=(6, 4))
ax.plot(F[0, :], F[1, :], label=r'$|F(\omega)| = \frac{2}{1+\omega^2}$')
ax.plot(bound[0, :], bound[1, :], 'r--', label=r'$\int_{-\infty}^{\infty} |f(t)| dt = 2$')
ax.plot(P[0, :], P[1, :], 'ko')
plt.sca(ax); label_pts(P, ['(0, 2)'])
ax.set_xlabel(r'$\omega$')
ax.set_ylabel('Magnitude')
ax.set_title('Fourier Transform Upper Bound')
ax.legend()
ax.grid(True)
plt.tight_layout()
plt.savefig("figs/Fourier_Bound.png")
