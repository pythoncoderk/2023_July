import copy

l = [2,5,1,4,6,3]
l2 = copy.deepcopy(l)
print(l)
print(l2)
x = len(l)-1
l_min = l[0]
for i in range(len(l)-1):
    for j in range(x):
        if l_min > l[i+1]:
            l_min, l[i+1] = l[i+1], l_min

