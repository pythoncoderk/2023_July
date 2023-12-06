import numpy as np

x = np.array(
    [[1,2,3],
     [4,5,6]]
)

y = np.array(
    [[10,11,12],
     [13,14,15]]
)

result = np.concatenate([x, y], 1)
print(result)