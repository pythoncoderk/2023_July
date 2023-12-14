import numpy as np

my_list1 = [1,2,3,4]
my_array1 = np.array(my_list1)
print(my_array1)

my_list2 = [11,22,33,44]
my_list3 = [my_list1, my_list2]
print(my_list3)

my_array2 = np.array(my_list3)
print(my_array2)

print(my_array2.shape)

print(my_array2.dtype)

print(np.zeros(5))

my_zeroz = np.zeros(9)
print(my_zeroz.dtype)

my_ones = np.ones((5,5))
print(my_ones)

print(np.empty((3,4)))

print(np.eye(5))

print(np.arange(5,50,2))