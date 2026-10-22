import numpy as np
import matplotlib.pyplot as plt
import subprocess, shlex

t = np.linspace(-1, 1, 1000)
f = np.sinc(2 * t)

fig, ax = plt.subplots(figsize=(6, 4))
ax.plot(t, f, label='Original / Reconstructed f(t)')
ax.set_xlabel('Time (s)')
ax.set_ylabel('Amplitude')
ax.set_title('Signal Reconstruction')
ax.legend()
ax.grid(True)
plt.tight_layout()
plt.savefig("../figs/Sampling_Reconstruction.png")
