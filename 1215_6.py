import numpy as np
import matplotlib.pyplot as plt

points = np.arange(-5,5,0.01)

dx, dy = np.meshgrid(points, points)
print(dx)

plt.imshow(dx)
