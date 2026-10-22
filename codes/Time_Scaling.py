import numpy as np
import matplotlib.pyplot as plt
import subprocess, shlex

t = np.linspace(0, 2, 500)
f_t = np.sin(2 * np.pi * t)
y_t = np.sin(2 * np.pi * 2 * t)

fig, ax = plt.subplots(figsize=(6, 4))
ax.plot(t, f_t, label='Original f(t) [Period T0]')
ax.plot(t, y_t, '--', label='Scaled y(t)=f(2t) [Period T0/2]')
ax.set_xlabel('Time t')
ax.set_ylabel('Amplitude')
ax.set_title('Time Scaling of Periodic Signal')
ax.legend()
ax.grid(True)
plt.tight_layout()
plt.savefig("../figs/Time_Scaling.png")
