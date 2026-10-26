import os
import numpy as np
import matplotlib.pyplot as plt
from CoordGeo.line.funcs import line_gen_num
from CoordGeo.plotting.funcs import label_pts

os.makedirs("figs", exist_ok=True)

coeffs = [1, 7, 3, -33, 2, -40]
roots = np.roots(coeffs)
P = np.vstack((roots.real, roots.imag))
jw = line_gen_num(np.array([[0], [-3]]), np.array([[0], [3]]), 2)

fig, ax = plt.subplots(figsize=(6, 4))
ax.plot(P[0, :], P[1, :], 'bs', markersize=8)
ax.plot(jw[0, :], jw[1, :], 'k--')
ax.set_xlabel('Real')
ax.set_ylabel('Imaginary')
ax.set_title('Polynomial Roots (L=2, I=2, R=1) (Q.37)')
ax.grid(True)
plt.tight_layout()
plt.savefig("figs/Poly_Roots.png")
