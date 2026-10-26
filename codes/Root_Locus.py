import os
import numpy as np
import matplotlib.pyplot as plt
from CoordGeo.line.funcs import line_gen_num
from CoordGeo.plotting.funcs import label_pts

os.makedirs("figs", exist_ok=True)

K = np.linspace(0, 50, 1000)
roots = np.array([np.roots([1 + k, 3 + 7 * k, 2 + 12 * k]) for k in K])
B1 = np.vstack((roots[:, 0].real, roots[:, 0].imag))
B2 = np.vstack((roots[:, 1].real, roots[:, 1].imag))
P = np.array([[-1], [1]])

fig, ax = plt.subplots(figsize=(6, 4))
ax.plot(B1[0, :], B1[1, :], 'b.', markersize=1)
ax.plot(B2[0, :], B2[1, :], 'b.', markersize=1)
ax.plot(P[0, :], P[1, :], 'rx', label='Point -1+j (Not on locus)')
plt.sca(ax); label_pts(P, ['$-1+j$'])
ax.set_xlabel('Real')
ax.set_ylabel('Imaginary')
ax.set_title('Root Locus Diagram (Q.26)')
ax.grid(True)
ax.legend()
plt.tight_layout()
plt.savefig("figs/Root_Locus.png")
