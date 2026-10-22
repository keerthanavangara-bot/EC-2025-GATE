import numpy as np
import matplotlib.pyplot as plt
import subprocess, shlex
from CoordGeo.line.funcs import line_gen
from CoordGeo.plotting.funcs import label_pts

theta = np.linspace(0, 2 * np.pi, 200)
z_x, z_y = np.cos(theta), np.sin(theta)

origin = np.array([0, 0]).reshape(-1, 1)
pt_one = np.array([1, 0]).reshape(-1, 1)
radius_line = line_gen(origin, pt_one)

fig, ax = plt.subplots(figsize=(6, 6))
ax.plot(z_x, z_y, 'b-', linewidth=2, label='Unit Circle C')
ax.plot(radius_line[0, :], radius_line[1, :], 'r--', label='Radius r=1')

pts = np.block([origin, pt_one])
ax.plot(pts[0, :], pts[1, :], 'ko', markersize=5)
label_pts(pts, ['O', '1'])

ax.set_xlim(-1.5, 1.5)
ax.set_ylim(-1.5, 1.5)
ax.axhline(0, color='black', linewidth=0.8, linestyle='--')
ax.axvline(0, color='black', linewidth=0.8, linestyle='--')
ax.set_aspect('equal')
ax.grid(True, linestyle=':', alpha=0.6)
ax.set_xlabel('Re(z)')
ax.set_ylabel('Im(z)')
ax.set_title('Unit Circle Contour in Complex Plane')
ax.legend(loc='upper right')

plt.tight_layout()
plt.savefig("../figs/Contour_Integral.png")
