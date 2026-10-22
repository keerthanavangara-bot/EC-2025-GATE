import numpy as np
import matplotlib.pyplot as plt
import subprocess, shlex

n = np.arange(0, 10)
x1 = np.ones(len(n))
x2 = 2 * x1

b = 1.0
h2 = np.array([0.5, 0.5])

y1 = np.convolve(np.convolve(x1, [1]), h2)[:len(n)] + b * (np.pad(h2, (0, len(n)-len(h2))) - (n==0).astype(float))
y2 = np.convolve(np.convolve(x2, [1]), h2)[:len(n)] + b * (np.pad(h2, (0, len(n)-len(h2))) - (n==0).astype(float))

fig, ax = plt.subplots(figsize=(6, 4))
ax.stem(n, y1, linefmt='b-', markerfmt='bo', basefmt=" ", label='Output y1 for x')
ax.stem(n, y2, linefmt='r--', markerfmt='rx', basefmt=" ", label='Output y2 for 2x')
ax.set_xlabel('n')
ax.set_ylabel('y[n]')
ax.set_title('Non-linear Response Verification (Q.17)')
ax.legend()
ax.grid(True)
plt.tight_layout()
plt.savefig("figs/LTI_System.png")
