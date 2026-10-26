import os
import numpy as np
import matplotlib.pyplot as plt
from CoordGeo.line.funcs import line_gen_num
from CoordGeo.plotting.funcs import label_pts

os.makedirs("figs", exist_ok=True)

t = np.linspace(-1, 1, 1000)
f = np.vstack((t, np.sinc(2 * t)))
zero = line_gen_num(np.array([[-1], [0]]), np.array([[1], [0]]), 2)

fig, ax = plt.subplots(figsize=(6, 4))
ax.plot(f[0, :], f[1, :], label='Original / Reconstructed f(t)')
ax.plot(zero[0, :], zero[1, :], 'k:', linewidth=0.8)
ax.set_xlabel('Time (s)')
ax.set_ylabel('Amplitude')
ax.set_title('Signal Reconstruction (Q.38)')
ax.legend()
ax.grid(True)
plt.tight_layout()
plt.savefig("figs/Sampling_Reconstruction.png")
