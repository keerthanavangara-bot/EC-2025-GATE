import os
import numpy as np
import matplotlib.pyplot as plt
from CoordGeo.line.funcs import line_gen_num
from CoordGeo.plotting.funcs import label_pts

os.makedirs("figs", exist_ok=True)

p_B = np.array([0.5, 0.5])
p_X = np.convolve(p_B, p_B)
p_Y = p_X.copy()
p_S = np.convolve(p_X, p_Y)
p_diff = (p_X[1] * p_Y[1]) / p_S[2]
PX = np.vstack((np.arange(len(p_X)), p_X))

fig, ax = plt.subplots(figsize=(6, 4))
ax.stem(PX[0, :], PX[1, :], basefmt=" ", label='PMF of X (Red Balls)')
ax.set_xlabel('Number of Balls')
ax.set_ylabel('Probability')
ax.set_title(f'Probability of Different Colours = {p_diff:.2f} (Q.13)')
ax.legend()
ax.grid(True)
plt.tight_layout()
plt.savefig("figs/Two_balls.png")
