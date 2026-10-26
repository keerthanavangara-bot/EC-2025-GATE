import os
import numpy as np
import matplotlib.pyplot as plt
from CoordGeo.line.funcs import line_gen_num
from CoordGeo.plotting.funcs import label_pts

os.makedirs("figs", exist_ok=True)

f1 = 1000
t = np.linspace(0, 2 / f1, 1000)
delta_f = 3 * f1 * np.cos(2 * np.pi * f1 * t) + 12 * f1 * np.cos(6 * np.pi * f1 * t)
dev = np.vstack((t * 1000, delta_f / f1))
peak = line_gen_num(np.array([[0], [15]]), np.array([[2], [15]]), 2)
P = np.array([[0.0], [15.0]])

fig, ax = plt.subplots(figsize=(6, 4))
ax.plot(dev[0, :], dev[1, :], label=r'$\Delta f(t) / f_1$')
ax.plot(peak[0, :], peak[1, :], 'r--', label='Peak Deviation = $15f_1$')
ax.plot(P[0, :], P[1, :], 'ko')
plt.sca(ax); label_pts(P, ['15'])
ax.set_xlabel('Time (ms)')
ax.set_ylabel(r'Deviation ($\times f_1$)')
ax.set_title('Instantaneous FM Frequency Deviation (Q.14)')
ax.legend()
ax.grid(True)
plt.tight_layout()
plt.savefig("figs/FM_Dev.png")
