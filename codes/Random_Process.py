import numpy as np
import matplotlib.pyplot as plt
import subprocess, shlex

T = 1.0
t = np.linspace(0, 2*T, 500)
p = lambda time: 1.0 if (0 <= time % T <= 0.5*T) else 0.0
var = [p(ti - T) for ti in t]

fig, ax = plt.subplots(figsize=(6, 4))
ax.plot(t, var, label=r'Variance $E[f(t)^2]$')
ax.set_xlabel('Time t')
ax.set_ylabel('Variance')
ax.set_title('Time-Dependent Variance of Random Process')
ax.legend()
ax.grid(True)
plt.tight_layout()
plt.savefig("../figs/Random_Process.png")
