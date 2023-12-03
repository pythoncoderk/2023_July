import numpy
import numpy as np

n, m = map(int, input().split())
l = [list(input()) for i in range(n)]
print(n, m)
arr1 = np.array(l)
print(arr1)

arr2 = numpy.copy(arr1)
print(arr2)