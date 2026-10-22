import numpy as np
import matplotlib.pyplot as plt
import subprocess, shlex

K = np.linspace(0, 50, 1000)
roots = []
for k in K:
    r = np.roots([1 + k, 3 + 7*k, 2 + 12*k])
    roots.append(r)

roots = np.array(roots)

fig, ax = plt.subplots(figsize=(6, 4))
ax.plot(roots[:, 0].real, roots[:, 0].imag, 'b.', markersize=1)
ax.plot(roots[:, 1].real, roots[:, 1].imag, 'b.', markersize=1)
ax.plot([-1], [1], 'rx', label='Point -1+j (Not on locus)')
ax.set_xlabel('Real')
ax.set_ylabel('Imaginary')
ax.set_title('Root Locus Diagram (Q.26)')
ax.grid(True)
ax.legend()
plt.tight_layout()
plt.savefig("figs/Root_Locus.png")
