import os
import numpy as np
import matplotlib.pyplot as plt
from CoordGeo.line.funcs import line_gen_num
from CoordGeo.plotting.funcs import label_pts

os.makedirs("figs", exist_ok=True)

f = np.logspace(1, 6, 500)
w = 2 * np.pi * f
R, C = 100, 1e-6

Y = 1/R + 1j * w * C
mag = np.vstack((f, np.abs(Y)))                 # 2 x N point matrix
phase = np.vstack((f, np.angle(Y, deg=True)))

# corner frequency: w = 1/(RC)  ->  |Y| = sqrt(2)/R , phase = 45 deg
fc = 1 / (2 * np.pi * R * C)
P1 = np.array([[fc], [np.sqrt(2) / R]])
P2 = np.array([[fc], [45.0]])

fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(7, 6))

ax1.semilogx(mag[0, :], mag[1, :], 'b-', linewidth=2)
ax1.plot(P1[0, :], P1[1, :], 'ko')
plt.sca(ax1); label_pts(P1, ['$f_c$'])
ax1.set_ylabel('Admittance Magnitude (S)')
ax1.set_title('AC Admittance Response')
ax1.grid(True, which='both', linestyle=':', alpha=0.6)

ax2.semilogx(phase[0, :], phase[1, :], 'r-', linewidth=2)
ax2.plot(P2[0, :], P2[1, :], 'ko')
plt.sca(ax2); label_pts(P2, ['$45^\\circ$'])
ax2.set_xlabel('Frequency (Hz)')
ax2.set_ylabel('Phase (degrees)')
ax2.grid(True, which='both', linestyle=':', alpha=0.6)

plt.tight_layout()
plt.savefig('figs/AC_Admittance.png')
