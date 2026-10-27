import os
import subprocess
import sys
import numpy as np
import matplotlib.pyplot as plt

# Find the project root automatically.
# Expected structure:
# EC-2025-GATE/
# ├── codes/
# │   └── FM_Dev.py
# └── figs/

script_dir = os.path.dirname(os.path.abspath(__file__))
root = os.path.dirname(script_dir)
figs_dir = os.path.join(root, "figs")

# Create the figures directory using subprocess.
subprocess.run(
    [
        sys.executable,
        "-c",
        "import os, sys; os.makedirs(sys.argv[1], exist_ok=True)",
        figs_dir
    ],
    check=True
)

# Given FM signal
Ac = 1.0
f1 = 500.0
fc = 120.0 * f1

# Sampling parameters
duration = 0.2
fs = 250000.0
N = int(duration * fs)
t = np.arange(N) / fs

# Generate FM signal
phase = (
    2 * np.pi * fc * t
    + 3 * np.sin(2 * np.pi * f1 * t)
    + 4 * np.sin(6 * np.pi * f1 * t)
)

signal = Ac * np.cos(phase)

# Fourier transform
F = np.fft.rfft(signal)
freq = np.fft.rfftfreq(N, d=1 / fs)
amplitude = 2 * np.abs(F) / N

amplitude[0] /= 2
if N % 2 == 0:
    amplitude[-1] /= 2

# Sideband frequencies
n_sidebands = np.arange(-25, 26)
line_freq = fc + n_sidebands * f1
line_amp = np.zeros_like(line_freq, dtype=float)

freq_resolution = fs / N

for i, f_line in enumerate(line_freq):
    idx = int(round(f_line / freq_resolution))

    if 0 <= idx < len(amplitude):
        line_amp[i] = amplitude[idx]

# Create plots
fig, ax = plt.subplots(2, 1, figsize=(9, 7))

# Time-domain graph: display 2 milliseconds
time_window = t <= 0.002

ax[0].plot(
    t[time_window] * 1000,
    signal[time_window],
    linewidth=1.0
)

ax[0].set_title("FM Signal in Time Domain (0–2 ms)")
ax[0].set_xlabel("Time (ms)")
ax[0].set_ylabel("Amplitude")
ax[0].grid(True, alpha=0.3)

# Fourier amplitude spectrum
markerline, stemlines, baseline = ax[1].stem(
    line_freq / 1000,
    line_amp,
    basefmt=" "
)

plt.setp(markerline, markersize=2.5)
plt.setp(stemlines, linewidth=0.9)

ax[1].set_title("Fourier Transform Amplitude Spectrum")
ax[1].set_xlabel("Frequency (kHz)")
ax[1].set_ylabel("Fourier amplitude")
ax[1].set_xlim(
    (fc - 25 * f1) / 1000,
    (fc + 25 * f1) / 1000
)
ax[1].grid(True, alpha=0.3)

fig.tight_layout()

# Save figure directly to the project's figs folder
output_path = os.path.join(figs_dir, "FM_Dev.png")
fig.savefig(output_path, dpi=200, bbox_inches="tight")
plt.close(fig)

# Analytical verification
print(f"Graph saved at: {output_path}")
print(f"Carrier frequency = {fc} Hz")
print(f"Modulating frequency = {f1} Hz")
print(f"Peak frequency deviation = {15 * f1} Hz")
