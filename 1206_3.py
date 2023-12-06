import numpy as np

x = np.array(
    [[1,2,3],
     [4,5,6]]
)

result = x.reshape(6,1)
print(result)