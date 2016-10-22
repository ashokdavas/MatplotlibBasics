import numpy as np
import matplotlib.pyplot as plt

# linestyles = ['_', '-', '--', ':']
# colors = ('b', 'g', 'r', 'c', 'm', 'y', 'k')

# Create a figure of size 8x6 inches, 80 dots per inch
plt.figure(figsize=(8, 6), dpi=80)

# Create a new subplot from a grid of 1x1
plt.subplot(1, 1, 1)

X = np.linspace(-np.pi, np.pi, 256, endpoint=True)
C, S = np.cos(X), np.sin(X)

# Plot cosine with a blue non-continuous line of width 1 (pixels)
plt.plot(X, C, color="m", linewidth=1.0, linestyle="--")

# Plot sine with a green continuous line of width 1 (pixels)
plt.plot(X, S, color="green", linewidth=1.0, linestyle="-")

# Set x limits
plt.xlim(-4.0, 4.0)

# plt.xticks([-np.pi, -np.pi/2, 0, np.pi/2, np.pi])
# plt.yticks([-1, 0, +1]) # linespace also generated the list
# Set x ticks. 9 points to tick
plt.xticks(np.linspace(-4, 4, 9, endpoint=True))

# Set y limits
plt.ylim(-1.0, 1.0)

# Set y ticks
plt.yticks(np.linspace(-1, 1, 9, endpoint=True))

# Save figure using 72 dots per inch
# plt.savefig("simple.png", dpi=72)

# Show result on screen
plt.show()
