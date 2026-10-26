import os
import numpy as np
import matplotlib.pyplot as plt
from CoordGeo.line.funcs import line_gen_num
from CoordGeo.plotting.funcs import label_pts

os.makedirs("figs", exist_ok=True)

t = np.linspace(0, 2, 200)
X1 = np.vstack((t, 0.5 * (np.exp(2 * t) - 1)))
X2 = np.vstack((t, 0.5 * (1 - np.exp(-2 * t))))
X3 = np.vstack((t, t))

fig, ax = plt.subplots(figsize=(6, 4))
ax.plot(X1[0, :], X1[1, :], label='x1(t) [Unbounded]')
ax.plot(X2[0, :], X2[1, :], label='x2(t) [Bounded]')
ax.plot(X3[0, :], X3[1, :], label='x3(t) [Unbounded]')
ax.set_xlabel('Time t')
ax.set_ylabel('State Values')
ax.set_title('Internal State Signals Response')
ax.legend()
ax.grid(True)
plt.tight_layout()
plt.savefig("figs/State_Space.png")
