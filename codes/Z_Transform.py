import os
import numpy as np
import matplotlib.pyplot as plt
from CoordGeo.line.funcs import line_gen_num
from CoordGeo.plotting.funcs import label_pts

os.makedirs("figs", exist_ok=True)

from CoordGeo.conics.funcs import circ_gen_num

O = np.array([0, 0]).reshape(-1, 1)
circle = circ_gen_num(O, 1, 200)                 # unit circle
Zr = np.array([[0.5], [0]])                      # zero at z = 0.5
Pl = np.array([[0], [0]])                        # pole at z = 0

fig, ax = plt.subplots(figsize=(6, 6))
ax.plot(circle[0, :], circle[1, :], color='gray', linestyle='--', label='Unit Circle')
ax.plot(Zr[0, :], Zr[1, :], 'o', color='blue', label='Zero at z=0.5')
ax.plot(Pl[0, :], Pl[1, :], 'x', color='red', label='Pole at z=0')
plt.sca(ax)
label_pts(np.block([Zr, Pl]), ['0.5', '0'])

ax.set_xlim(-1.5, 1.5)
ax.set_ylim(-1.5, 1.5)
ax.set_aspect('equal')
ax.set_xlabel('Re(z)')
ax.set_ylabel('Im(z)')
ax.set_title('Pole-Zero Diagram and Unit Circle (Q.27)')
ax.grid(True)
ax.legend()
plt.tight_layout()
plt.savefig("figs/Z_Transform.png")
