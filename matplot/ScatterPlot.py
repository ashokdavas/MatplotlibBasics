import numpy as np
import matplotlib.pyplot as plt

n = 1024
X = np.random.normal(0, 1, n)
Y = np.random.normal(0, 1, n)
# Element-wise arc tangent of x1/x2 choosing the quadrant correctly.
# The quadrant (i.e., branch) is chosen so that arctan2(x1, x2) is the signed angle in radians between the ray ending at the origin
#  and passing through the point (1,0),
#  and the ray ending at the origin and passing through the point (x2, x1).
T = np.arctan2(Y, X)
plt.figure(figsize=(8, 6), dpi=100)

# matplotlib.pyplot.scatter(x, y, s=20, c=None, marker='o',
#  cmap=None, norm=None, vmin=None, vmax=None, alpha=None, linewidths=None, verts=None,
#  edgecolors=None, hold=None, data=None, **kwargs)
# s is the size in point^2. larger the value of s, larger will be size of points in plot
# c : color, sequence, or sequence of color, optional, default: blue
# alpha correspnds to the transparency of represented figure
plt.scatter(X, Y, s=30, c=T, alpha=.5)

plt.xlim(-1.5, 1.5)
plt.xticks(())
plt.ylim(-1.5, 1.5)
plt.yticks(())

plt.show()
