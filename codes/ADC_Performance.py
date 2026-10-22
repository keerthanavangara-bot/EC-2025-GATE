import numpy as np
import matplotlib.pyplot as plt
import os

n_bits = 3
v_ref = 5.0
levels = 2**n_bits
step = v_ref / levels

t = np.linspace(0, 1, 1000)
v_in = v_ref * (0.5 + 0.4 * np.sin(2 * np.pi * 2 * t))
v_quant = np.floor(v_in / step) * step

plt.figure(figsize=(8, 5))
plt.plot(t, v_in, label='Analog Input', color='blue')
plt.step(t, v_quant, label='Quantized Output (3-bit ADC)', color='red', where='post')
plt.xlabel('Time (s)')
plt.ylabel('Voltage (V)')
plt.title('ADC Quantization Performance')
plt.legend()
plt.grid(True)

output_path = os.path.expanduser('~/Downloads/figs/ADC_Performance.png')
plt.savefig(output_path)
plt.close()
