import numpy as np
import matplotlib.pyplot as plt
import subprocess, shlex

t = np.linspace(0, 1, 1000)
m = np.cos(2 * np.pi * 2 * t)
env_am = 1 + 0.5 * m

fig, ax = plt.subplots(figsize=(6, 4))
ax.plot(t, env_am, 'r', label='AM Envelope (1 + 0.5 m(t)) > 0')
ax.plot(t, m, 'b--', label='Message m(t)')
ax.set_xlabel('Time (s)')
ax.set_ylabel('Amplitude')
ax.set_title('Envelope Detection in AM (Q.28)')
ax.legend()
ax.grid(True)
plt.tight_layout()
plt.savefig("figs/Envelope_Detector.png")
