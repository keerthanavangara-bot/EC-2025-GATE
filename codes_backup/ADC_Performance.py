import os
import numpy as np
import matplotlib.pyplot as plt
from CoordGeo.line.funcs import line_gen_num
from CoordGeo.plotting.funcs import label_pts

os.makedirs("figs", exist_ok=True)

n_bits, v_ref = 3, 5.0
levels = 2**n_bits
step = v_ref / levels

t = np.linspace(0, 1, 1000)
v_in = v_ref * (0.5 + 0.4 * np.sin(2 * np.pi * 2 * t))
v_quant = np.floor(v_in / step) * step
vin = np.vstack((t, v_in))
vq = np.vstack((t, v_quant))

plt.figure(figsize=(8, 5))
# quantisation levels drawn with line_gen_num
for k in range(levels + 1):
    L = line_gen_num(np.array([[0], [k * step]]), np.array([[1], [k * step]]), 2)
    plt.plot(L[0, :], L[1, :], color='gray', linewidth=0.5, linestyle=':')
plt.plot(vin[0, :], vin[1, :], label='Analog Input', color='blue')
plt.step(vq[0, :], vq[1, :], label='Quantized Output (3-bit ADC)', color='red', where='post')
plt.xlabel('Time (s)')
plt.ylabel('Voltage (V)')
plt.title('ADC Quantization Performance')
plt.legend()
plt.grid(True)
plt.savefig('figs/ADC_Performance.png')
plt.close()
