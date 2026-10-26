import os
import numpy as np
import matplotlib.pyplot as plt
from CoordGeo.line.funcs import line_gen_num
from CoordGeo.plotting.funcs import label_pts

os.makedirs("figs", exist_ok=True)

x = np.linspace(-5, 5, 200)
E = np.vstack((x, np.where(x >= 0, 1.0, -1.0)))
xaxis = line_gen_num(np.array([[-5], [0]]), np.array([[5], [0]]), 2)
yaxis = line_gen_num(np.array([[0], [-1.5]]), np.array([[0], [1.5]]), 2)

fig, ax = plt.subplots(figsize=(6, 4))
ax.plot(E[0, :], E[1, :], 'g-', linewidth=2, label='Electric Field E(x)')
ax.plot(xaxis[0, :], xaxis[1, :], 'k-', linewidth=0.8)
ax.plot(yaxis[0, :], yaxis[1, :], 'k-', linewidth=0.8)
ax.set_xlabel('Position x')
ax.set_ylabel('Electric Field Magnitude')
ax.set_title('Infinite Sheet Charge Electric Field')
ax.grid(True, linestyle=':', alpha=0.6)
ax.legend(loc='upper right')
plt.tight_layout()
plt.savefig('figs/Sheet_Charge.png')
