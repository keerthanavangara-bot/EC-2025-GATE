import os
import numpy as np
import matplotlib.pyplot as plt
from CoordGeo.line.funcs import line_gen_num
from CoordGeo.plotting.funcs import label_pts

os.makedirs("figs", exist_ok=True)

X = np.array([0, 1, 2, 3])
Y = np.array([1, 2, 1, 0])
idx = np.arange(4)
ideal = np.vstack((idx, X - Y))
out = np.vstack((idx, (X - Y) % 4))

fig, ax = plt.subplots(figsize=(6, 4))
ax.plot(ideal[0, :], ideal[1, :], 'ro-', label='Ideal Subtraction (X - Y)')
ax.plot(out[0, :], out[1, :], 'bs--', label='2-bit Subtractor Output F')
ax.set_xlabel('Test Index')
ax.set_ylabel('Value')
ax.set_title('Subtractor Operation Verification (Q.24)')
ax.legend()
ax.grid(True)
plt.tight_layout()
plt.savefig("figs/Adder_Subtractor.png")
