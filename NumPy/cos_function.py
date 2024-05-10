import matplotlib.pyplot as plt
import numpy as np

x_range = np.linspace(-10, 10, 10**6)
y = np.cos(x_range)

plt.plot(x_range, y)
plt.show()
