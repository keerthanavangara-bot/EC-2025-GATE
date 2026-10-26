import os
import numpy as np
import matplotlib.pyplot as plt
from CoordGeo.line.funcs import line_gen_num
from CoordGeo.plotting.funcs import label_pts

os.makedirs("figs", exist_ok=True)

outcomes = np.add.outer(np.arange(1, 7), np.arange(1, 7)).flatten()
vals, counts = np.unique(outcomes, return_counts=True)
pmf = counts / 36.0
EX = np.sum(vals * pmf)                          # = 7

# vertical line at x = E[X]  (E[X] is a value of the sum, so it sits on the x-axis)
mean_line = line_gen_num(np.array([[EX], [0]]), np.array([[EX], [pmf.max() * 1.1]]), 2)

fig, ax = plt.subplots(figsize=(6, 4))
ax.bar(vals, pmf, color='purple')
ax.plot(mean_line[0, :], mean_line[1, :], 'r--', label=f'Expectation E[X] = {EX:.2f}')
ax.set_xlabel('Sum of Two Dice')
ax.set_ylabel('Probability')
ax.set_title('PMF of the Sum of Two Fair Dice (Q.58)')
ax.legend()
plt.tight_layout()
plt.savefig("figs/Dice_Sum.png")
