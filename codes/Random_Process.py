import os
import numpy as np
import matplotlib.pyplot as plt
from CoordGeo.line.funcs import line_gen_num
from CoordGeo.plotting.funcs import label_pts

os.makedirs("figs", exist_ok=True)

T = 1.0
t = np.linspace(0, 2 * T, 500)
p = lambda time: 1.0 if (0 <= time % T <= 0.5 * T) else 0.0
var = np.vstack((t, [p(ti - T) for ti in t]))

fig, ax = plt.subplots(figsize=(6, 4))
ax.plot(var[0, :], var[1, :], label=r'Variance $E[f(t)^2]$')
ax.set_xlabel('Time t')
ax.set_ylabel('Variance')
ax.set_title('Time-Dependent Variance of Random Process')
ax.legend()
ax.grid(True)
plt.tight_layout()
plt.savefig("figs/Random_Process.png")
