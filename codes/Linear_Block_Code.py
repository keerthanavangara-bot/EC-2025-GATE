import numpy as np
import matplotlib.pyplot as plt
import subprocess, shlex

G = np.array([
    [1, 0, 0, 1, 0, 1],
    [0, 1, 0, 0, 1, 1],
    [0, 0, 1, 1, 1, 0]
])

u = [np.array([int(x) for x in format(i, '03b')]) for i in range(1, 8)]
weights = [np.sum(np.dot(vec, G) % 2) for vec in u]

fig, ax = plt.subplots(figsize=(6, 4))
ax.bar(range(1, 8), weights, color='green')
ax.axhline(3, color='r', linestyle='--', label='d_min = 3')
ax.set_xlabel('Non-zero Codeword Index')
ax.set_ylabel('Hamming Weight')
ax.set_title('Hamming Weights of Codewords (Q.33)')
ax.legend()
plt.tight_layout()
plt.savefig("figs/Linear_Block_Code.png")
