import numpy as np

x = np.linspace(1, 20, 10)
print(x)

y = np.linspace(1, 20, 5, retstep=True)
print(y)

z = np.linspace(1, 20, 5, endpoint=False)
print(z)