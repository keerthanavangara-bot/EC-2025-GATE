import numpy as np
import matplotlib.pyplot as plt

fig, ax = plt.subplots(figsize=(6, 4))
t = np.linspace(0, 1, 500)
signal = np.sin(2 * np.pi * 5 * t)
quantized = np.round(signal * 4) / 4

ax.plot(t, signal, label='Analog Input', color='blue')
ax.step(t, quantized, label='Quantized Output', color='red', where='post')
ax.set_title('ADC Performance')
ax.set_xlabel('Time (s)')
ax.set_ylabel('Amplitude')
ax.grid(True)
ax.legend()

plt.tight_layout()
plt.savefig('../figs/ADC_Performance.png', bbox_inches='tight')
plt.close(fig)
