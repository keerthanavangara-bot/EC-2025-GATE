import numpy as np
import matplotlib.pyplot as plt
import subprocess, shlex

fig, ax = plt.subplots(figsize=(6, 4))
ax.plot([-2, 0, 2], [1/3, 1/3, 1/3], 'ro', label='Symbols S={-2,0,2}')
ax.axvline(-1, color='k', linestyle='--', label='ML Decision Boundaries')
ax.axvline(1, color='k', linestyle='--')
ax.set_xlabel('Received Signal Y')
ax.set_ylabel('Prior Probability')
ax.set_title('ML Decoder Decision Regions')
ax.legend()
ax.grid(True)
plt.tight_layout()
plt.savefig("../figs/ML_Decoder.png")
