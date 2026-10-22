import numpy as np
import matplotlib.pyplot as plt
import math, subprocess, shlex

N = 20
n = np.arange(1, N + 1)

s1 = np.cumsum(1.0 / np.sqrt(n))
s2 = np.cumsum(1.0 / (n * (n + 1)))
s3 = np.cumsum([1.0 / math.factorial(i) for i in n])

fig, ax = plt.subplots(figsize=(6, 4))
ax.plot(n, s1, 'o-', label=r'(i) $\sum 1/\sqrt{n}$ (Diverges)')
ax.plot(n, s2, 's-', label=r'(ii) $\sum 1/n(n+1)$ (Converges to 1)')
ax.plot(n, s3, '^--', label=r'(iii) $\sum 1/n!$ (Converges to e-1)')
ax.set_xlabel('N')
ax.set_ylabel('Partial Sum')
ax.set_title('Series Partial Sums Convergence')
ax.grid(True)
ax.legend()
plt.tight_layout()
plt.savefig("../figs/Series_Convergence.png")
