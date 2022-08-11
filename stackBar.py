import matplotlib.pyplot as plt
import numpy as np

x = ['Bangladesh', 'India', 'Japan', 'China']
y1 = np.array([0.02, 0.12, 2.30, 2.25])
y2 = np.array([0.22, 1.11, 1.95, 2.69])
y3 = np.array([0.59, 1.52, 2.36, 2.99])

plt.bar(x, y1, color='r')
plt.bar(x, y2, bottom=y1, color='b')
plt.bar(x, y3, bottom=y1+y2, color='g')
plt.xlabel("Countries")
plt.ylabel("Categories")
plt.legend(["Divorced", "Married", "Single"])
plt.title("Single, Married and divorced ratio between 4 Countries")
plt.show()
