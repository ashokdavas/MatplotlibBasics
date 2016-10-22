import numpy as np
import matplotlib.pyplot as plt

# matplotlib.pyplot.bar(left, height, width=0.8, bottom=None, hold=None, data=None, **kwargs)
# Make a bar plot with rectangles bounded by:
# left, left + width, bottom, bottom + height : (left, right, bottom and top edges)

n = 12
X = np.arange(n)
Y1 = (1 - X / float(n)) * np.random.uniform(0.5, 1.0, n)
Y2 = (1 - X / float(n)) * np.random.uniform(0.5, 1.0, n)

plt.figure(figsize=(10, 8), dpi=100)
# shrinks the outer size
# plt.axes([0.025, 0.025, 0.95, 0.95])
plt.bar(X, +Y1, facecolor='#9999ff', edgecolor='white', width=0.8)
plt.bar(X, -Y2, facecolor='#ff9999', edgecolor='white', width=0.8)  # 0.8 is also default width

# generate text for bar plot
for x, y in zip(X, Y1):
    plt.text(x + 0.4, y + 0.05, '%.2f' % y, ha='center', va='bottom')

for x, y in zip(X, Y2):
    plt.text(x + 0.4, -y - 0.05, '%.2f' % y, ha='center', va='top')

plt.xlim(-.5, n)
plt.xticks(())
plt.ylim(-1.25, 1.25)
plt.yticks(())

plt.show()
