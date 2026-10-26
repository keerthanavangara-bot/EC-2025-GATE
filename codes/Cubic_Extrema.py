import os
import numpy as np
import matplotlib.pyplot as plt
from CoordGeo.line.funcs import line_gen_num
from CoordGeo.plotting.funcs import label_pts

os.makedirs("figs", exist_ok=True)

x = np.linspace(-3, 4, 400)
f = 2 * x**3 - 3 * x**2 - 12 * x + 1
curve = np.vstack((x, f))
P = np.array([[-1, 2], [8, -19]])                # local max, local min

fig, ax = plt.subplots(figsize=(6, 4))
ax.plot(curve[0, :], curve[1, :], label=r'$f(x) = 2x^3-3x^2-12x+1$')
ax.plot(P[0, 0], P[1, 0], 'ro', label='Local Max (-1, 8)')
ax.plot(P[0, 1], P[1, 1], 'go', label='Local Min (2, -19)')
plt.sca(ax); label_pts(P, ['(-1, 8)', '(2, -19)'])
ax.set_xlabel('x')
ax.set_ylabel('f(x)')
ax.set_title('Cubic Function Local Extrema')
ax.legend()
ax.grid(True)
plt.tight_layout()
plt.savefig("figs/Cubic_Extrema.png")
