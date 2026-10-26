import os
import numpy as np
import matplotlib.pyplot as plt
from CoordGeo.line.funcs import line_gen_num
from CoordGeo.plotting.funcs import label_pts

os.makedirs("figs", exist_ok=True)

import math

N = 20
n = np.arange(1, N + 1)
S1 = np.vstack((n, np.cumsum(1.0 / np.sqrt(n))))
S2 = np.vstack((n, np.cumsum(1.0 / (n * (n + 1)))))
S3 = np.vstack((n, np.cumsum([1.0 / math.factorial(i) for i in n])))

lim2 = line_gen_num(np.array([[1], [1]]), np.array([[N], [1]]), 2)                 # limit 1
lim3 = line_gen_num(np.array([[1], [np.e - 1]]), np.array([[N], [np.e - 1]]), 2)   # limit e-1

fig, ax = plt.subplots(figsize=(6, 4))
ax.plot(S1[0, :], S1[1, :], 'o-', label=r'(i) $\sum 1/\sqrt{n}$ (Diverges)')
ax.plot(S2[0, :], S2[1, :], 's-', label=r'(ii) $\sum 1/n(n+1)$ (Converges to 1)')
ax.plot(S3[0, :], S3[1, :], '^--', label=r'(iii) $\sum 1/n!$ (Converges to e-1)')
ax.plot(lim2[0, :], lim2[1, :], 'k:', linewidth=0.8)
ax.plot(lim3[0, :], lim3[1, :], 'k:', linewidth=0.8)
ax.set_xlabel('N')
ax.set_ylabel('Partial Sum')
ax.set_title('Series Partial Sums Convergence')
ax.grid(True)
ax.legend()
plt.tight_layout()
plt.savefig("figs/Series_Convergence.png")
