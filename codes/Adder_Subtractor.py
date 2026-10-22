import numpy as np
import matplotlib.pyplot as plt
import subprocess, shlex

X = np.array([0, 1, 2, 3])
Y = np.array([1, 2, 1, 0])
diff = (X - Y) % 4

fig, ax = plt.subplots(figsize=(6, 4))
ax.plot(range(4), X - Y, 'ro-', label='Ideal Subtraction (X - Y)')
ax.plot(range(4), diff, 'bs--', label='2-bit Subtractor Output F')
ax.set_xlabel('Test Index')
ax.set_ylabel('Value')
ax.set_title('Subtractor Operation Verification')
ax.legend()
ax.grid(True)
plt.tight_layout()
plt.savefig("../figs/Adder_Subtractor.png")
