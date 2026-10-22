import numpy as np
import matplotlib.pyplot as plt
import subprocess, shlex

cases = ['(i)', '(ii)', '(iii)', '(iv)']
ranks, nullities = [], []

A_i = np.array([[2, 3, 4, 5], [0, 6, 7, 8], [0, 0, 0, 2], [0, 0, 0, 2]])
A_ii = np.array([[2, 3, 4, 5], [0, 6, 7, 8], [0, 0, 0, 0], [0, 0, 0, 0]])
A_iii = np.array([[2, 3, 4, 5], [0, 6, 7, 8], [0, 0, 2, 0], [0, 0, 0, 0]])
A_iv = np.array([[2, 3, 4, 5], [0, 6, 7, 8], [0, 0, 2, 2], [0, 0, 0, 2]])

for A in [A_i, A_ii, A_iii, A_iv]:
    r = np.linalg.matrix_rank(A)
    ranks.append(r)
    nullities.append(4 - r)

fig, ax = plt.subplots(figsize=(6, 4))
x = np.arange(len(cases))
ax.bar(x - 0.2, ranks, 0.4, label='Rank', color='skyblue')
ax.bar(x + 0.2, nullities, 0.4, label='Nullity', color='salmon')
ax.axhline(3, color='red', linestyle='--', label='Threshold (Rank >= 3)')
ax.set_xticks(x)
ax.set_xticklabels(cases)
ax.set_ylabel('Dimensions')
ax.set_title('Matrix Rank and Nullity Analysis (Q.11)')
ax.legend()
plt.tight_layout()
plt.savefig("figs/Matrix_Rank.png")
