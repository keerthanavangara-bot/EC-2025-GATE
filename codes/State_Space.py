import numpy as np
import matplotlib.pyplot as plt
import subprocess, shlex

t = np.linspace(0, 2, 200)
x1 = 0.5 * (np.exp(2 * t) - 1)
x2 = 0.5 * (1 - np.exp(-2 * t))
x3 = t

fig, ax = plt.subplots(figsize=(6, 4))
ax.plot(t, x1, label='x1(t) [Unbounded]')
ax.plot(t, x2, label='x2(t) [Bounded]')
ax.plot(t, x3, label='x3(t) [Unbounded]')
ax.set_xlabel('Time t')
ax.set_ylabel('State Values')
ax.set_title('Internal State Signals Response')
ax.legend()
ax.grid(True)
plt.tight_layout()
plt.savefig("../figs/State_Space.png")
