import numpy as np
import matplotlib.pyplot as plt
import subprocess, shlex

roots_I = np.roots([10, 0, 0, 1])
roots_PD = np.roots([10, 2, 5])

fig, ax = plt.subplots(figsize=(6, 4))
ax.plot(roots_I.real, roots_I.imag, 'ro', label='Integral Control Poles')
ax.plot(roots_PD.real, roots_PD.imag, 'go', label='PD Control Poles')
ax.axvline(0, color='k', linestyle='--')
ax.set_xlabel('Real')
ax.set_ylabel('Imaginary')
ax.set_title('Closed-Loop Poles Location')
ax.legend()
ax.grid(True)
plt.tight_layout()
plt.savefig("../figs/Controller_Stability.png")
