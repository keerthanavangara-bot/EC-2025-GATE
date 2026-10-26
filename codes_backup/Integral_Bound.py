import os
import numpy as np
import matplotlib.pyplot as plt
from CoordGeo.line.funcs import line_gen_num
from CoordGeo.plotting.funcs import label_pts

os.makedirs("figs", exist_ok=True)

x = np.linspace(2, 8, 200)
m, M = 1.0, 3.0
f = np.vstack((x, 2.0 + np.sin(x)))
lineM = line_gen_num(np.array([[2], [M]]), np.array([[8], [M]]), 2)
linem = line_gen_num(np.array([[2], [m]]), np.array([[8], [m]]), 2)

fig, ax = plt.subplots(figsize=(6, 4))
ax.plot(f[0, :], f[1, :], label='f(x)')
ax.plot(lineM[0, :], lineM[1, :], 'r--', label='M = 3.0')
ax.plot(linem[0, :], linem[1, :], 'g--', label='m = 1.0')
ax.fill_between(x, m, M, color='gray', alpha=0.2)
ax.set_xlabel('x')
ax.set_ylabel('f(x)')
ax.set_title('Integral Bounds (Q.51)')
ax.legend()
ax.grid(True)
plt.tight_layout()
plt.savefig("figs/Integral_Bound.png")
