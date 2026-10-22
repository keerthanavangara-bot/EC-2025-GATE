import numpy as np
import matplotlib.pyplot as plt
import os

t = np.linspace(0, 10, 500)
response = 1 - np.exp(-0.8 * t) * (np.cos(1.2 * t) + 0.6 * np.sin(1.2 * t))

plt.figure(figsize=(8, 5))
plt.plot(t, response, label='System Step Response', color='green')
plt.axhline(1.0, color='black', linestyle='--', label='Target Value')
plt.xlabel('Time (s)')
plt.ylabel('Output y(t)')
plt.title('Signal Flow Graph System Response')
plt.legend()
plt.grid(True)

output_path = os.path.expanduser('~/Downloads/figs/Signal_Flow_Graph.png')
plt.savefig(output_path)
plt.close()
