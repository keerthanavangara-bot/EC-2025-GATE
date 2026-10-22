import numpy as np
import matplotlib.pyplot as plt
import subprocess, shlex

x = np.linspace(2, 8, 200)
m, M = 1.0, 3.0
f = 2.0 + np.sin(x)

fig, ax = plt.subplots(figsize=(6, 4))
ax.plot(x, f, label='f(x)')
ax.axhline(M, color='r', linestyle='--', label='M = 3.0')
ax.axhline(m, color='g', linestyle='--', label='m = 1.0')
ax.fill_between(x, m, M, color='gray', alpha=0.2)
ax.set_xlabel('x')
ax.set_ylabel('f(x)')
ax.set_title(r'Integral Bounds (Q.51)')
ax.legend()
ax.grid(True)
plt.tight_layout()
plt.savefig("figs/Integral_Bound.png")
