import numpy as np
import matplotlib.pyplot as plt
import subprocess, shlex

outcomes = np.add.outer(np.arange(1, 7), np.arange(1, 7)).flatten()
vals, counts = np.unique(outcomes, return_counts=True)
pmf = counts / 36.0

fig, ax = plt.subplots(figsize=(6, 4))
ax.bar(vals, pmf, color='purple')
ax.axhline(7, color='r', linestyle='--', label='Expectation E[X] = 7.00')
ax.set_xlabel('Sum of Two Dice')
ax.set_ylabel('Probability')
ax.set_title('PMF of the Sum of Two Fair Dice (Q.58)')
ax.legend()
plt.tight_layout()
plt.savefig("figs/Dice_Sum.png")
