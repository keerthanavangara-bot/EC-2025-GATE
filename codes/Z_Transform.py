import numpy as np
import matplotlib.pyplot as plt
import subprocess, shlex

fig, ax = plt.subplots(figsize=(6, 6))
circle = plt.Circle((0, 0), 1, color='gray', fill=False, linestyle='--', label='Unit Circle')
ax.add_patch(circle)

ax.plot(0.5, 0, 'o', color='blue', label='Zero at z=0.5')
ax.plot(0, 0, 'x', color='red', label='Pole at z=0')

ax.set_xlim(-1.5, 1.5)
ax.set_ylim(-1.5, 1.5)
ax.set_aspect('equal')
ax.set_xlabel('Re(z)')
ax.set_ylabel('Im(z)')
ax.set_title('Pole-Zero Diagram and Unit Circle (Q.27)')
ax.grid(True)
ax.legend()
plt.tight_layout()
plt.savefig("figs/Z_Transform.png")
