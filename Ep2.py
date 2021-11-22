import matplotlib.pyplot as plt
import numpy as np

data = np.loadtxt("large.txt")
A = data[:-1]
b = data[-1]
x = np.linalg.solve(A, b)

plt.grid(True)
plt.bar(np.arange(x.shape[0]), x)
plt.show()