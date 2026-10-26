import os
import numpy as np
import matplotlib.pyplot as plt
from CoordGeo.line.funcs import line_gen_num
from CoordGeo.plotting.funcs import label_pts

os.makedirs("figs", exist_ok=True)

f = np.logspace(4, 9, 500)
fL, fH = 1e6, 50e6
H = (f / fL) / np.sqrt((1 + (f / fL)**2) * (1 + (f / fH)**2))
resp = np.vstack((f / 1e6, 20 * np.log10(H / np.max(H))))

# vertical marker lines at fL and fH
vL = line_gen_num(np.array([[1], [-80]]), np.array([[1], [5]]), 2)
vH = line_gen_num(np.array([[50], [-80]]), np.array([[50], [5]]), 2)

fig, ax = plt.subplots(figsize=(6, 4))
ax.semilogx(resp[0, :], resp[1, :])
ax.plot(vL[0, :], vL[1, :], 'r--', label='fL = 1 MHz')
ax.plot(vH[0, :], vH[1, :], 'g--', label='fH = 50 MHz')
ax.set_ylim(-60, 5)
ax.set_xlabel('Frequency (MHz)')
ax.set_ylabel('Magnitude Response (dB)')
ax.set_title('Bandpass Filter Frequency Response')
ax.legend()
ax.grid(True)
plt.tight_layout()
plt.savefig("figs/Bandpass_Filter.png")
