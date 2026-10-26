import os
import numpy as np
import matplotlib.pyplot as plt
from CoordGeo.line.funcs import line_gen_num

os.makedirs("figs", exist_ok=True)

# Q.1.2.1 : A = [[2,3,4,5],[0,6,7,8],[0,0,a,b],[0,0,0,g]],  rank(A) >= 3 ?
def A_mat(a, b, g):
    return np.array([[2, 3, 4, 5], [0, 6, 7, 8], [0, 0, a, b], [0, 0, 0, g]], dtype=float)

cases = {'(i)': (0, 1, 1), '(ii)': (0, 0, 0), '(iii)': (1, 0, 0), '(iv)': (1, 1, 1)}
good = [k for k, v in cases.items() if np.linalg.matrix_rank(A_mat(*v)) >= 3]
print("Rank >= 3 for:", ", ".join(good), " -> option (a)")

L = 6.0   # half-size of the plotting box


def plane_pts(n, L):
    """Points of the plane n.x = 0 (spanned by two vectors perpendicular to n)."""
    n = np.asarray(n, float).reshape(-1)
    _, _, Vt = np.linalg.svd(n.reshape(1, -1))
    u, v = Vt[1], Vt[2]
    s, t = np.meshgrid(np.linspace(-L, L, 12), np.linspace(-L, L, 12))
    return [s * u[i] + t * v[i] for i in range(3)]


def draw_planes(ax, normals, colors):
    for n, c in zip(normals, colors):
        X, Y, Z = plane_pts(n, L)
        ax.plot_surface(X, Y, Z, color=c, alpha=0.25, linewidth=0)


def panel(ax, title, normals, labels, axes_names):
    """Planes n_k . x = 0 (equations taken directly from the rows of A) and their intersection."""
    colors = ['tab:blue', 'tab:orange', 'tab:green']
    draw_planes(ax, normals, colors[:len(normals)])
    N = np.array(normals, float)

    if len(normals) == 2:                      # two planes -> straight line
        d = np.cross(N[0], N[1])
        d = d / np.linalg.norm(d) * L
        line = line_gen_num((-d).reshape(-1, 1), d.reshape(-1, 1), 50)
        ax.plot(line[0, :], line[1, :], line[2, :], 'r-', linewidth=3, label='intersection (line)')
    else:                                      # three planes -> single point
        P = np.linalg.solve(N, np.zeros(3)).reshape(-1, 1)
        ax.plot(P[0, :], P[1, :], P[2, :], 'ro', markersize=8, label='intersection (origin)')

    for c, lab in zip(colors, labels):         # legend entries for the planes
        ax.plot([], [], color=c, linewidth=6, alpha=0.4, label=lab)
    ax.set_xlim(-L, L); ax.set_ylim(-L, L); ax.set_zlim(-L, L)
    ax.set_xlabel(axes_names[0]); ax.set_ylabel(axes_names[1]); ax.set_zlabel(axes_names[2])
    ax.set_title(title, fontsize=10)
    ax.legend(loc='upper left', fontsize=7)


fig = plt.figure(figsize=(15, 5))

# (i) alpha=0, beta=gamma=b != 0 : row 4 gives x4 = 0, row 3 is then 0 = 0
ax = fig.add_subplot(1, 3, 1, projection='3d')
panel(ax, '(i)  rank 3: two planes meet in a line  ($x_4$ = 0)',
      [(2, 3, 4), (0, 6, 7)],
      ['$2x_1+3x_2+4x_3=0$', '$6x_2+7x_3=0$'],
      ['$x_1$', '$x_2$', '$x_3$'])

# (iii) beta=gamma=0, alpha != 0 : row 3 gives x3 = 0, x4 stays free
ax = fig.add_subplot(1, 3, 2, projection='3d')
panel(ax, '(iii)  rank 3: two planes meet in a line  ($x_3$ = 0)',
      [(2, 3, 0), (0, 6, 0)],
      ['$2x_1+3x_2=0$', '$6x_2=0$'],
      ['$x_1$', '$x_2$', '$x_4$'])

# (iv) alpha=beta=gamma != 0 : row 4 gives x4 = 0, row 3 then gives x3 = 0
ax = fig.add_subplot(1, 3, 3, projection='3d')
panel(ax, '(iv)  rank 4: three planes meet in a point  ($x_4$ = 0)',
      [(2, 3, 4), (0, 6, 7), (0, 0, 1)],
      ['$2x_1+3x_2+4x_3=0$', '$6x_2+7x_3=0$', '$x_3=0$'],
      ['$x_1$', '$x_2$', '$x_3$'])

fig.suptitle('Q.1.2.1 : rank(A) $\\geq$ 3 for (i), (iii), (iv)  ->  option (a)', fontsize=12)
plt.tight_layout()
plt.savefig("figs/Matrix_Rank.png", dpi=150)
