import os
import numpy as np
import matplotlib.pyplot as plt
from CoordGeo.line.funcs import line_gen_num
from CoordGeo.plotting.funcs import label_pts

os.makedirs("figs", exist_ok=True)

t = np.linspace(0, 2, 500)
f_t = np.vstack((t, np.sin(2 * np.pi * t)))
y_t = np.vstack((t, np.sin(2 * np.pi * 2 * t)))

fig, ax = plt.subplots(figsize=(6, 4))
ax.plot(f_t[0, :], f_t[1, :], label='Original f(t) [Period T0]')
ax.plot(y_t[0, :], y_t[1, :], '--', label='Scaled y(t)=f(2t) [Period T0/2]')
ax.set_xlabel('Time t')
ax.set_ylabel('Amplitude')
ax.set_title('Time Scaling of Periodic Signal (Q.55)')
ax.legend()
ax.grid(True)
plt.tight_layout()
plt.savefig("figs/Time_Scaling.png")
