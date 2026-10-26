import os
import numpy as np
import matplotlib.pyplot as plt
from CoordGeo.line.funcs import line_gen_num
from CoordGeo.plotting.funcs import label_pts

os.makedirs("figs", exist_ok=True)

G = np.array([
    [1, 0, 0, 1, 0, 1],
    [0, 1, 0, 0, 1, 1],
    [0, 0, 1, 1, 1, 0]
])

u = [np.array([int(x) for x in format(i, '03b')]) for i in range(1, 8)]
weights = np.array([np.sum(np.dot(vec, G) % 2) for vec in u])
d_min = weights.min()                            # min distance = min non-zero weight

dmin_line = line_gen_num(np.array([[0.5], [d_min]]), np.array([[7.5], [d_min]]), 2)

fig, ax = plt.subplots(figsize=(6, 4))
ax.bar(range(1, 8), weights, color='green')
ax.plot(dmin_line[0, :], dmin_line[1, :], 'r--', label=f'd_min = {d_min}')
ax.set_xlabel('Non-zero Codeword Index')
ax.set_ylabel('Hamming Weight')
ax.set_title('Hamming Weights of Codewords')
ax.legend()
plt.tight_layout()
plt.savefig("figs/Linear_Block_Code.png")
