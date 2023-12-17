import timeit

import numpy as np

def test_arr():
    return np.arange(100, 10000000)
arr_time = timeit.timeit("test_arr()", globals=globals())
print(arr_time)


