import matplotlib.pyplot as plt

fig, ax = plt.subplots(figsize=(6, 4))
nodes = ['R(s)', 'X1', 'X2', 'C(s)']
x_pos = [0, 1, 2, 3]
y_pos = [0, 0, 0, 0]

ax.scatter(x_pos, y_pos, color='black', s=100)
for i, txt in enumerate(nodes):
ax.annotate(txt, (x_pos[i], y_pos[i] + 0.1), ha='center', fontsize=12)

ax.annotate('', xy=(1, 0), xytext=(0, 0), arrowprops=dict(arrowstyle='->', lw=1.5))
ax.annotate('', xy=(2, 0), xytext=(1, 0), arrowprops=dict(arrowstyle='->', lw=1.5))
ax.annotate('', xy=(3, 0), xytext=(2, 0), arrowprops=dict(arrowstyle='->', lw=1.5))

ax.set_xlim(-0.5, 3.5)
ax.set_ylim(-0.5, 0.5)
ax.set_title('Signal Flow Graph')
ax.axis('off')

plt.tight_layout()
plt.savefig('../figs/Signal_Flow_Graph.png', bbox_inches='tight')
plt.close(fig)
