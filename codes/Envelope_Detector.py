import os
import numpy as np
import matplotlib.pyplot as plt
from CoordGeo.line.funcs import line_gen_num
from CoordGeo.plotting.funcs import label_pts

os.makedirs("figs", exist_ok=True)

t = np.linspace(0, 1, 1000)
m = np.cos(2 * np.pi * 2 * t)
env = np.vstack((t, 1 + 0.5 * m))
msg = np.vstack((t, m))
zero = line_gen_num(np.array([[0], [0]]), np.array([[1], [0]]), 2)

fig, ax = plt.subplots(figsize=(6, 4))
ax.plot(env[0, :], env[1, :], 'r', label='AM Envelope (1 + 0.5 m(t)) > 0')
ax.plot(msg[0, :], msg[1, :], 'b--', label='Message m(t)')
ax.plot(zero[0, :], zero[1, :], 'k:', linewidth=0.8)
ax.set_xlabel('Time (s)')
ax.set_ylabel('Amplitude')
ax.set_title('Envelope Detection in AM')
ax.legend()
ax.grid(True)
plt.tight_layout()
plt.savefig("figs/Envelope_Detector.png")
