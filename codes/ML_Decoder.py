import os
import numpy as np
import matplotlib.pyplot as plt
from CoordGeo.line.funcs import line_gen_num
from CoordGeo.plotting.funcs import label_pts

os.makedirs("figs", exist_ok=True)

S = np.array([[-2, 0, 2], [1/3, 1/3, 1/3]])      # symbols and priors
b1 = line_gen_num(np.array([[-1], [0]]), np.array([[-1], [0.5]]), 2)
b2 = line_gen_num(np.array([[1], [0]]), np.array([[1], [0.5]]), 2)

fig, ax = plt.subplots(figsize=(6, 4))
ax.plot(S[0, :], S[1, :], 'ro', label='Symbols S={-2,0,2}')
ax.plot(b1[0, :], b1[1, :], 'k--', label='ML Decision Boundaries')
ax.plot(b2[0, :], b2[1, :], 'k--')
ax.set_ylim(0, 0.5)
ax.set_xlabel('Received Signal Y')
ax.set_ylabel('Prior Probability')
ax.set_title('ML Decoder Decision Regions')
ax.legend()
ax.grid(True)
plt.tight_layout()
plt.savefig("figs/ML_Decoder.png")
