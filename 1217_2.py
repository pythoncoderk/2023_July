import numpy as np

a = np.zeros(10, dtype=np.int32)
print(a)

b = [0 for i in range(1, 11)]
print(b)

for i in range(len(a)):
    a[i] = i
    b[i] = i
    print(f"a[{i}]:{a[i]},{id(a[i])},b[{i}]:{b[i]},{id(b[i])}")