import os
import numpy as np
import matplotlib.pyplot as plt
from CoordGeo.line.funcs import line_gen_num
from CoordGeo.plotting.funcs import label_pts

os.makedirs("figs", exist_ok=True)

t = np.linspace(0, 10, 500)
y = np.vstack((t, 1 - np.exp(-0.8 * t) * (np.cos(1.2 * t) + 0.6 * np.sin(1.2 * t))))
target = line_gen_num(np.array([[0], [1]]), np.array([[10], [1]]), 2)

plt.figure(figsize=(8, 5))
plt.plot(y[0, :], y[1, :], label='System Step Response', color='green')
plt.plot(target[0, :], target[1, :], 'k--', label='Target Value')
plt.xlabel('Time (s)')
plt.ylabel('Output y(t)')
plt.title('Signal Flow Graph System Response')
plt.legend()
plt.grid(True)
plt.savefig('figs/Signal_Flow_Graph.png')
plt.close()
