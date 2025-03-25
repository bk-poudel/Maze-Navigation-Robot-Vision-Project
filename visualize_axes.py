import numpy as np

import matplotlib.pyplot as plt

theta = np.arange(0, 360, 10)  # Angles from 0 to 460 degrees in steps of 10
r = 1  # Length of the line

plt.figure()
plt.axis('equal')
plt.xlim([-1.5, 1.5])
plt.ylim([-1.5, 1.5])

for angle in theta:
    x = r * np.cos(np.radians(angle))
    y = r * np.sin(np.radians(angle))
    plt.plot([0, x], [0, y], linewidth=2)
    plt.pause(0.1)  # Pause to visualize each line

plt.show()
