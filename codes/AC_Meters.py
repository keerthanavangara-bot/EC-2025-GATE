import numpy as np
import matplotlib.pyplot as plt
import subprocess, shlex

C = np.linspace(1e-6, 50e-6, 500)
w = 200
L = 1.0
Z = np.abs(1j * w * L + 1 / (1j * w * C))

fig, ax = plt.subplots(figsize=(6, 4))
ax.plot(C * 1e6, Z)
ax.plot(25, 0, 'ro', label='Resonance C = 25 uF (Z = 0)')
ax.set_xlabel('Capacitance (uF)')
ax.set_ylabel('Impedance (Ohm)')
ax.set_title('Resonant LC Branch Impedance')
ax.legend()
ax.grid(True)
plt.tight_layout()
plt.savefig("../figs/AC_Meters.png")
