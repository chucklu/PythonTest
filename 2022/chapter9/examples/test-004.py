import numpy as np
import matplotlib.pyplot as plt
x = np.linspace(-10, 10, 300)
y = []
for i in x:
    if np.sin(i) > 0:  # 调用sin，cos要使用np.sin，np.cos
        y.append(-1)
    else:
        y.append(1)
y = np.array(y)  # 需要把list转化成array，方便进行矩阵的运算
plt.plot(x, y)
plt.show()
