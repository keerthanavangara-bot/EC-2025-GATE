import numpy as np
import matplotlib.pyplot as plt
import subprocess, shlex

t = np.linspace(0, 2, 200)
dB_dt = 0.5
A = 5.0
R = 4.0
I = (A * dB_dt) / R * np.ones_like(t)

fig, ax = plt.subplots(figsize=(6, 4))
ax.plot(t, I, label='Induced Current I = 0.63 A')
ax.set_xlabel('Time (s)')
ax.set_ylabel('Current (A)')
ax.set_title('Induced Loop Current (Q.65)')
ax.legend()
ax.grid(True)
plt.tight_layout()
plt.savefig("figs/Faraday_Induction.png")
