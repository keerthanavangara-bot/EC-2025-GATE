import numpy as np
import matplotlib.pyplot as plt
import subprocess, shlex

f1 = 1000
t = np.linspace(0, 2/f1, 1000)
delta_f = 3 * f1 * np.cos(2 * np.pi * f1 * t) + 12 * f1 * np.cos(6 * np.pi * f1 * t)

fig, ax = plt.subplots(figsize=(6, 4))
ax.plot(t * 1000, delta_f / f1, label=r'$\Delta f(t) / f_1$')
ax.axhline(15, color='r', linestyle='--', label='Peak Deviation = $15f_1$')
ax.set_xlabel('Time (ms)')
ax.set_ylabel(r'Deviation ($	imes f_1$)')
ax.set_title('Instantaneous FM Frequency Deviation (Q.14)')
ax.legend()
ax.grid(True)
plt.tight_layout()
plt.savefig("figs/FM_Dev.png")
