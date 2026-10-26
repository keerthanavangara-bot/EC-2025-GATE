import os
import numpy as np
import matplotlib.pyplot as plt
from CoordGeo.line.funcs import line_gen_num
from CoordGeo.plotting.funcs import label_pts

os.makedirs("figs", exist_ok=True)

from CoordGeo.conics.funcs import circ_gen_num

O = np.array([0, 0]).reshape(-1, 1)
A = np.array([1, 0]).reshape(-1, 1)
circle = circ_gen_num(O, 1, 200)                 # unit circle |z| = 1
radius = line_gen_num(O, A, 20)

fig, ax = plt.subplots(figsize=(6, 6))
ax.plot(circle[0, :], circle[1, :], 'b-', linewidth=2, label='Unit Circle C')
ax.plot(radius[0, :], radius[1, :], 'r--', label='Radius r=1')

pts = np.block([O, A])
ax.plot(pts[0, :], pts[1, :], 'ko', markersize=5)
label_pts(pts, ['O', '1'])

re_axis = line_gen_num(np.array([[-1.5], [0]]), np.array([[1.5], [0]]), 2)
im_axis = line_gen_num(np.array([[0], [-1.5]]), np.array([[0], [1.5]]), 2)
ax.plot(re_axis[0, :], re_axis[1, :], 'k--', linewidth=0.8)
ax.plot(im_axis[0, :], im_axis[1, :], 'k--', linewidth=0.8)

ax.set_xlim(-1.5, 1.5)
ax.set_ylim(-1.5, 1.5)
ax.set_aspect('equal')
ax.grid(True, linestyle=':', alpha=0.6)
ax.set_xlabel('Re(z)')
ax.set_ylabel('Im(z)')
ax.set_title('Unit Circle Contour in Complex Plane (Q.52)')
ax.legend(loc='upper right')
plt.tight_layout()
plt.savefig("figs/Contour_Integral.png")
