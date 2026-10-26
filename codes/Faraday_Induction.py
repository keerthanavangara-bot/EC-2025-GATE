import os
import numpy as np
import matplotlib.pyplot as plt
from CoordGeo.line.funcs import line_gen_num
from CoordGeo.plotting.funcs import label_pts

os.makedirs("figs", exist_ok=True)

dB_dt, A, R = 0.5, 5.0, 4.0
I0 = (A * dB_dt) / R
Iline = line_gen_num(np.array([[0], [I0]]), np.array([[2], [I0]]), 200)

fig, ax = plt.subplots(figsize=(6, 4))
ax.plot(Iline[0, :], Iline[1, :], label=f'Induced Current I = {I0:.2f} A')
ax.set_ylim(0, 1)
ax.set_xlabel('Time (s)')
ax.set_ylabel('Current (A)')
ax.set_title('Induced Loop Current (Q.65)')
ax.legend()
ax.grid(True)
plt.tight_layout()
plt.savefig("figs/Faraday_Induction.png")
