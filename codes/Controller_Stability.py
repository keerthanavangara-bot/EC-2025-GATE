import os
import numpy as np
import matplotlib.pyplot as plt
from CoordGeo.line.funcs import line_gen_num
from CoordGeo.plotting.funcs import label_pts

os.makedirs("figs", exist_ok=True)

roots_I = np.roots([10, 0, 0, 1])
roots_PD = np.roots([10, 2, 5])
PI = np.vstack((roots_I.real, roots_I.imag))
PP = np.vstack((roots_PD.real, roots_PD.imag))
jw = line_gen_num(np.array([[0], [-1]]), np.array([[0], [1]]), 2)   # imaginary axis

fig, ax = plt.subplots(figsize=(6, 4))
ax.plot(PI[0, :], PI[1, :], 'ro', label='Integral Control Poles')
ax.plot(PP[0, :], PP[1, :], 'go', label='PD Control Poles')
ax.plot(jw[0, :], jw[1, :], 'k--')
ax.set_xlabel('Real')
ax.set_ylabel('Imaginary')
ax.set_title('Closed-Loop Poles Location')
ax.legend()
ax.grid(True)
plt.tight_layout()
plt.savefig("figs/Controller_Stability.png")
