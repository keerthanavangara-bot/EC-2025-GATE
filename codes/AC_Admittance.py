import numpy as np
import matplotlib.pyplot as plt

f = np.logspace(1, 6, 500)
w = 2 * np.pi * f
R = 100
C = 1e-6

Y = 1/R + 1j * w * C
mag = np.abs(Y)
phase = np.angle(Y, deg=True)

fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(7, 6))

ax1.semilogx(f, mag, 'b-', linewidth=2)
ax1.set_ylabel('Admittance Magnitude (S)')
ax1.set_title('AC Admittance Response')
ax1.grid(True, which='both', linestyle=':', alpha=0.6)

ax2.semilogx(f, phase, 'r-', linewidth=2)
ax2.set_xlabel('Frequency (Hz)')
ax2.set_ylabel('Phase (degrees)')
ax2.grid(True, which='both', linestyle=':', alpha=0.6)

plt.tight_layout()
plt.savefig('figs/AC_Admittance.png')
