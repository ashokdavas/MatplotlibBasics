import numpy as np
import matplotlib.pyplot as plt

n = 256
X = np.linspace(-np.pi, np.pi, n, endpoint=True)
Y = np.sin(2 * X)

plt.figure(figsize=(10, 8), dpi=100)
# shrinks the outer size
# plt.axes([0.025, 0.025, 0.95, 0.95])

# alpha - 0.0 transparent through 1.0 opaque
plt.plot(X, Y + 1, color='blue', alpha=1.00)
plt.fill_between(X, 1, Y + 1, color='blue', alpha=.25)

plt.plot(X, Y - 1, color='blue', alpha=1.00)
plt.fill_between(X, -1, Y - 1, (Y - 1) > -1, color='blue', alpha=.25)
plt.fill_between(X, -1, Y - 1, (Y - 1) < -1, color='red', alpha=.25)

plt.xlim(-4, 4)
plt.xticks(np.linspace(-4, 4, 9, endpoint=True))
plt.ylim(-2.5, 2.5)
plt.yticks(np.linspace(-2.5, 2.5, 11, endpoint=True))

plt.show()
