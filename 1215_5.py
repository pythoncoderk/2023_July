import numpy as np

arr = np.arange(11)
print(arr)

print(np.sqrt(arr))

print(np.exp(arr))

a = np.random.rand(10)
print(a)

rng = np.random.default_rng()
b = rng.standard_normal(10)
print(b)

print(np.add(a, b))

print(np.maximum(a, b))