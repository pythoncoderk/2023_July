import copy

num1 = [[1, 2], [3, 4]]
num2 = num1
num2[1][1] = 5
num3 = copy.copy(num1)
num3[1][1] = 6
num4 = copy.deepcopy(num1)
num4[1][1] = 7

print(num1)