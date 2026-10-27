import os
import subprocess
import sys
import numpy as np
import matplotlib.pyplot as plt

# Make CoordGeo importable
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from CoordGeo.line.funcs import line_gen_num

# Create figs directory using subprocess
subprocess.run(
    [sys.executable, "-c", "import os; os.makedirs('figs', exist_ok=True)"],
    check=True
)

# FM signal parameters
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

# Calculate Fourier amplitude spectrum
F = np.fft.rfft(signal)
freq = np.fft.rfftfreq(N, d=1 / fs)

amplitude = 2 * np.abs(F) / N
amplitude[0] /= 2

if N % 2 == 0:
    amplitude[-1] /= 2

# Create figure with two plots
fig, ax = plt.subplots(2, 1, figsize=(9, 7))

# --------------------------------------------------
# 1. FM signal: Amplitude versus Time
# --------------------------------------------------
time_window = t <= 8.0 / fc

ax[0].plot(
    t[time_window] * 1000,
    signal[time_window],
    linewidth=1.0
)

ax[0].set_title("FM Signal in Time Domain")
ax[0].set_xlabel("Time (ms)")
ax[0].set_ylabel("Amplitude")
ax[0].grid(True, alpha=0.3)

# --------------------------------------------------
# 2. Fourier amplitude spectrum using CoordGeo
# --------------------------------------------------

# FM spectral components occur at fc + n*f1
sideband_indices = np.arange(-25, 26)
sideband_freqs = fc + sideband_indices * f1
sideband_amps = np.zeros(len(sideband_freqs))

# Obtain the amplitude of each spectral component
for i, f_component in enumerate(sideband_freqs):
    idx = int(round(f_component / (fs / N)))

    if 0 <= idx < len(amplitude):
        sideband_amps[i] = amplitude[idx]

# Use CoordGeo to generate each vertical spectral line
for f_component, amp in zip(sideband_freqs, sideband_amps):

    A = np.array([
        [f_component / 1000.0],
        [0.0]
    ])

    B = np.array([
        [f_component / 1000.0],
        [amp]
    ])

    # Generate two points between A and B
    spike = line_gen_num(A, B, 2)

    ax[1].plot(
        spike[0, :],
        spike[1, :],
        linewidth=1.0
    )

# Mark the spectral peaks
ax[1].plot(
    sideband_freqs / 1000.0,
    sideband_amps,
    "o",
    markersize=2.5
)

ax[1].set_title("Fourier Transform Amplitude Spectrum")
ax[1].set_xlabel("Frequency (kHz)")
ax[1].set_ylabel("Fourier amplitude")
ax[1].grid(True, alpha=0.3)

ax[1].set_xlim(
    (fc - 25 * f1) / 1000.0,
    (fc + 25 * f1) / 1000.0
)

# Save figure
fig.tight_layout()
fig.savefig("figs/FM_Dev.png", dpi=200, bbox_inches="tight")
plt.close(fig)

# Calculate peak frequency deviation analytically
print("Saved plot to figs/FM_Dev.png")
print(f"Peak frequency deviation = {15 * f1:.1f} Hz")
