import numpy as np
import matplotlib.pyplot as plt
import subprocess, shlex

f = np.logspace(4, 9, 500)
fL = 1e6
fH = 50e6

H = (f / fL) / np.sqrt((1 + (f / fL)**2) * (1 + (f / fH)**2))

fig, ax = plt.subplots(figsize=(6, 4))
ax.semilogx(f / 1e6, 20 * np.log10(H / np.max(H)))
ax.axvline(1, color='r', linestyle='--', label='fL = 1 MHz')
ax.axvline(50, color='g', linestyle='--', label='fH = 50 MHz')
ax.set_xlabel('Frequency (MHz)')
ax.set_ylabel('Magnitude Response (dB)')
ax.set_title('Bandpass Filter Frequency Response')
ax.legend()
ax.grid(True)
plt.tight_layout()
plt.savefig("../figs/Bandpass_Filter.png")
