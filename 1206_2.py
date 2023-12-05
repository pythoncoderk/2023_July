import numpy as np

x = np.array(
    [[1,2,3],
     [4,5,6]]
)

y = np.array(
    [[10,20],
     [30,40],
     [50,60]]
)

result = np.dot(x, y)
print(result)