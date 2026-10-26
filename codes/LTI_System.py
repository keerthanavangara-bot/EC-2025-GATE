import os
import numpy as np
import matplotlib.pyplot as plt
from CoordGeo.line.funcs import line_gen_num
from CoordGeo.plotting.funcs import label_pts

os.makedirs("figs", exist_ok=True)

n = np.arange(0, 10)
x1 = np.ones(len(n))
x2 = 2 * x1

b = 1.0
h2 = np.array([0.5, 0.5])
pad = np.pad(h2, (0, len(n) - len(h2))) - (n == 0).astype(float)

y1 = np.convolve(x1, h2)[:len(n)] + b * pad
y2 = np.convolve(x2, h2)[:len(n)] + b * pad
Y1 = np.vstack((n, y1))
Y2 = np.vstack((n, y2))

fig, ax = plt.subplots(figsize=(6, 4))
ax.stem(Y1[0, :], Y1[1, :], linefmt='b-', markerfmt='bo', basefmt=" ", label='Output y1 for x')
ax.stem(Y2[0, :], Y2[1, :], linefmt='r--', markerfmt='rx', basefmt=" ", label='Output y2 for 2x')
ax.set_xlabel('n')
ax.set_ylabel('y[n]')
ax.set_title('Non-linear Response Verification (Q.17)')
ax.legend()
ax.grid(True)
plt.tight_layout()
plt.savefig("figs/LTI_System.png")
