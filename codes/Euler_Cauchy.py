import os
import numpy as np
import matplotlib.pyplot as plt
from CoordGeo.line.funcs import line_gen_num
from CoordGeo.plotting.funcs import label_pts

os.makedirs("figs", exist_ok=True)

# t^2 y'' - 2 t y' + 2 y = 0,  y'(0) = 1,  y'(1) = -1
# Laplace transform gives  s^2 Y'' + 6 s Y' + 6 Y = 0  ->  Y = A/s^2 + B/s^3
# i.e.  y(t) = A t + (B/2) t^2  ->  y(t) = t - t^2   (A = 1, B = -2)
t_an = np.linspace(0, 1, 200)
y_an = np.vstack((t_an, t_an - t_an**2))


# ---------- Euler's method ----------
# State (u, v) = (y, y'),  u' = v,   v' = (2 t v - 2 u) / t^2
# The ODE is singular at t = 0, so start at a small t0 using y = t, y' = 1 (from y'(0) = 1)
# plus the unknown correction C t^2 ; C is fixed by shooting on y'(1) = -1.
def euler(C, t0=1e-2, h=1e-5):
    n = int(round((1 - t0) / h))
    t = t0 + h * np.arange(n + 1)
    u = np.zeros(n + 1)
    v = np.zeros(n + 1)
    u[0] = t0 + C * t0**2
    v[0] = 1 + 2 * C * t0
    for k in range(n):
        u[k + 1] = u[k] + h * v[k]
        v[k + 1] = v[k] + h * (2 * t[k] * v[k] - 2 * u[k]) / t[k]**2
    return t, u, v


t, u0, v0 = euler(0.0)
_, u1, v1 = euler(1.0)

# Euler's method is linear in the initial data, so y'(1) is linear in C
C = (-1 - v0[-1]) / (v1[-1] - v0[-1])
y_eu = u0 + C * (u1 - u0)
y_num = np.vstack((t, y_eu))

k = np.argmax(y_eu)
print("Euler: C = %.4f, y_max = %.4f at t = %.3f" % (C, y_eu[k], t[k]))
print("y_max (rounded) = %.2f" % y_eu[k])

# ---------- Stem plot of y(t) ----------
t0, h = 1e-2, 1e-5
t_s = np.arange(0.05, 1.0, 0.05)                      # sample instants
idx = np.round((t_s - t0) / h).astype(int)
S = np.vstack((t[idx], y_eu[idx]))                    # (t_k, y_k) from Euler's method

P = np.array([[0.5], [0.25]])                         # maximum point (0.5, 0.25)

fig, ax = plt.subplots(figsize=(6, 4))
ax.plot(y_an[0, :], y_an[1, :], 'b-', linewidth=1.2, label=r'Laplace: $y=t-t^2$')
for j in range(S.shape[1]):                           # one stem per sample, drawn with line_gen_num
    A = np.array([[S[0, j]], [0.0]])
    B = S[:, j].reshape(-1, 1)
    stem = line_gen_num(A, B, 2)
    ax.plot(stem[0, :], stem[1, :], 'r-', linewidth=1.2)
ax.plot(S[0, :], S[1, :], 'ro', markersize=5, label="Euler's method (stem)")
ax.plot(P[0, :], P[1, :], 'ko')
plt.sca(ax)
label_pts(P, ['(0.5, 0.25)'])
ax.set_ylim(-0.01, 0.29)
ax.set_xlabel('t')
ax.set_ylabel('y(t)')
ax.set_title('Euler-Cauchy equation: stem plot of y(t) on [0, 1]')
ax.legend(loc='upper right')
ax.grid(True)
plt.tight_layout()
plt.savefig("figs/Euler_Cauchy.png")
