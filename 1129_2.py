import numpy as np
rng = np.random.default_rng()
a = rng.integers(-10, 11, (2, 5))
print(a)
print(np.any(a == 5))