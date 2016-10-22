import numpy as np
import matplotlib.pyplot as plt

# linespace uses number of points while arrange use steps
# 256 is the number of points
x = np.linspace(-np.pi, np.pi, 256, endpoint=True)
c, s = np.cos(x), np.sin(x)

plt.plot(x, c)
plt.plot(x, s)

plt.show()
