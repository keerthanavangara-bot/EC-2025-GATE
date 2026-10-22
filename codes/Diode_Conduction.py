import numpy as np
import matplotlib.pyplot as plt
import subprocess, shlex

t = np.linspace(0, 20e-3, 1000)
Vi = 10 * np.sin(100 * np.pi * t)

fig, ax = plt.subplots(figsize=(6, 4))
ax.plot(t * 1000, Vi, label='Vi(t)')
ax.axhline(-5, color='r', linestyle='--', label='Cutoff Level (-5 V)')
ax.set_xlabel('Time (ms)')
ax.set_ylabel('Voltage (V)')
ax.set_title('Diode Forward Bias Conduction Interval (Q.61)')
ax.legend()
ax.grid(True)
plt.tight_layout()
plt.savefig("figs/Diode_Conduction.png")
