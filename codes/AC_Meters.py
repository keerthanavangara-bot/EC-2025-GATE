import os
import numpy as np
import matplotlib.pyplot as plt
from CoordGeo.line.funcs import line_gen_num
from CoordGeo.plotting.funcs import label_pts

os.makedirs("figs", exist_ok=True)

C = np.linspace(1e-6, 50e-6, 500)
w, L = 200, 1.0
Z = np.abs(1j * w * L + 1 / (1j * w * C))
curve = np.vstack((C * 1e6, Z))

C0 = 1 / (w**2 * L)                              # resonance
P = np.array([[C0 * 1e6], [0.0]])
zero_line = line_gen_num(np.array([[0], [0]]), np.array([[50], [0]]), 2)

fig, ax = plt.subplots(figsize=(6, 4))
ax.plot(curve[0, :], curve[1, :])
ax.plot(zero_line[0, :], zero_line[1, :], 'k:', linewidth=0.8)
ax.plot(P[0, :], P[1, :], 'ro', label='Resonance C = 25 uF (Z = 0)')
plt.sca(ax); label_pts(P, ['(25, 0)'])
ax.set_xlabel('Capacitance (uF)')
ax.set_ylabel('Impedance (Ohm)')
ax.set_title('Resonant LC Branch Impedance (Q.39)')
ax.legend()
ax.grid(True)
plt.tight_layout()
plt.savefig("figs/AC_Meters.png")
