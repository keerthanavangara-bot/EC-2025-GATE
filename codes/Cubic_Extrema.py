import numpy as np
import matplotlib.pyplot as plt
import subprocess, shlex

x = np.linspace(-3, 4, 400)
f = 2 * x**3 - 3 * x**2 - 12 * x + 1

fig, ax = plt.subplots(figsize=(6, 4))
ax.plot(x, f, label=r'$f(x) = 2x^3-3x^2-12x+1$')
ax.plot(-1, 8, 'ro', label='Local Max (-1, 8)')
ax.plot(2, -19, 'go', label='Local Min (2, -19)')
ax.set_xlabel('x')
ax.set_ylabel('f(x)')
ax.set_title('Cubic Function Local Extrema (Q.25)')
ax.legend()
ax.grid(True)
plt.tight_layout()
plt.savefig("figs/Cubic_Extrema.png")
