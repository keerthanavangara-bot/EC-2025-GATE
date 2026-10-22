import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-5, 5, 200)
E = np.where(x >= 0, 1.0, -1.0)

fig, ax = plt.subplots(figsize=(6, 4))
ax.plot(x, E, 'g-', linewidth=2, label='Electric Field E(x)')
ax.axhline(0, color='black', linewidth=0.8)
ax.axvline(0, color='black', linewidth=0.8)
ax.set_xlabel('Position x')
ax.set_ylabel('Electric Field Magnitude')
ax.set_title('Infinite Sheet Charge Electric Field')
ax.grid(True, linestyle=':', alpha=0.6)
ax.legend(loc='upper right')

plt.tight_layout()
plt.savefig('../figs/Sheet_Charge.png')
