import os
import numpy as np
import matplotlib.pyplot as plt
from CoordGeo.line.funcs import line_gen_num
from CoordGeo.plotting.funcs import label_pts

os.makedirs("figs", exist_ok=True)

t = np.linspace(0, 20e-3, 1000)
Vi = 10 * np.sin(100 * np.pi * t)
sig = np.vstack((t * 1000, Vi))
cut = line_gen_num(np.array([[0], [-5]]), np.array([[20], [-5]]), 2)

fig, ax = plt.subplots(figsize=(6, 4))
ax.plot(sig[0, :], sig[1, :], label='Vi(t)')
ax.plot(cut[0, :], cut[1, :], 'r--', label='Cutoff Level (-5 V)')
ax.set_xlabel('Time (ms)')
ax.set_ylabel('Voltage (V)')
ax.set_title('Diode Forward Bias Conduction Interval')
ax.legend()
ax.grid(True)
plt.tight_layout()
plt.savefig("figs/Diode_Conduction.png")
