import numpy as np
import matplotlib.pyplot as plt

alpha = np.linspace(0.01, 0.99, 200)
H = -alpha * np.log2(alpha) - (1 - alpha) * np.log2(1 - alpha)

fig, ax = plt.subplots(figsize=(6, 4))
ax.plot(alpha, H, 'b-', linewidth=2, label='Binary Entropy H(p)')
ax.set_xlabel('Probability (p)')
ax.set_ylabel('Entropy (bits)')
ax.set_title('Binary Entropy Function')
ax.grid(True, linestyle=':', alpha=0.6)
ax.legend(loc='upper right')

plt.tight_layout()
plt.savefig('../figs/Entropy.png')
