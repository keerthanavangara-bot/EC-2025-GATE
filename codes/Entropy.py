import os
import numpy as np
import matplotlib.pyplot as plt
from CoordGeo.line.funcs import line_gen_num
from CoordGeo.plotting.funcs import label_pts

os.makedirs("figs", exist_ok=True)

alpha = np.linspace(0.01, 0.99, 200)
H = -alpha * np.log2(alpha) - (1 - alpha) * np.log2(1 - alpha)
curve = np.vstack((alpha, H))
P = np.array([[0.5], [1.0]])                     # maximum at p = 1/2

fig, ax = plt.subplots(figsize=(6, 4))
ax.plot(curve[0, :], curve[1, :], 'b-', linewidth=2, label='Binary Entropy H(p)')
ax.plot(P[0, :], P[1, :], 'ko')
plt.sca(ax); label_pts(P, ['(0.5, 1)'])
ax.set_xlabel('Probability (p)')
ax.set_ylabel('Entropy (bits)')
ax.set_title('Binary Entropy Function')
ax.grid(True, linestyle=':', alpha=0.6)
ax.legend(loc='upper right')
plt.tight_layout()
plt.savefig('figs/Entropy.png')
