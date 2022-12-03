import numpy as np
import matplotlib.pyplot as plt
x = np.linspace(0, 6, 100)  # 从0到6，等分成100个元素的数组
print(x)
y = np.cos(2*np.pi*x)*np.exp(-x)+0.8
plt.plot(x, y, 'k', color='r', linewidth=2, linestyle='-')
plt.show()
