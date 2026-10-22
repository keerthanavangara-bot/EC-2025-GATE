import numpy as np
import matplotlib.pyplot as plt
from CoordGeo.line.funcs import line_gen
from CoordGeo.plotting.funcs import label_pts

origin = np.array([0, 0]).reshape(-1, 1)
a = np.array([1, 1]).reshape(-1, 1)
b = np.array([0, 3 * np.sqrt(2)]).reshape(-1, 1)

x_opt = ((a.T @ b) / (a.T @ a)).item()
proj = x_opt * a

line_a = line_gen(origin, a * 3)
line_b = line_gen(origin, b)
line_proj = line_gen(origin, proj)
line_err = line_gen(b, proj)

fig, ax = plt.subplots(figsize=(6, 6))
ax.plot(line_a[0, :], line_a[1, :], 'g--', label=r'Line $\mathbf{a}$')
ax.plot(line_b[0, :], line_b[1, :], 'r-', linewidth=2, label=r'Vector $\mathbf{b}$')
ax.plot(line_proj[0, :], line_proj[1, :], 'b-', linewidth=2, label=r'Projection $x^*\mathbf{a}$')
ax.plot(line_err[0, :], line_err[1, :], 'k:', linewidth=1.5, label='Error Vector')

pts = np.block([a, b, proj])
ax.plot(pts[0, :], pts[1, :], 'ko', markersize=5)
label_pts(pts, [r'$\mathbf{a}$', r'$\mathbf{b}$', r'$x^*\mathbf{a}$'])

ax.set_xlim(-1, 5)
ax.set_ylim(-1, 5)
ax.set_aspect('equal')
ax.grid(True, linestyle=':', alpha=0.6)
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_title('Vector Orthogonal Projection')
ax.legend(loc='upper left')

plt.tight_layout()
plt.savefig("../figs/Vector_Projection.png")
