import numpy as np
import matplotlib.pyplot as plt

# 乱数を発生させる
x = np.random.rand(100)
y = np.random.rand(100)

# 散布図を描画
plt.scatter(x,y)
plt.show()