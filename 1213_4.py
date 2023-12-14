l = [2,5,1,4,6,3]
x = len(l)-1
for i in range(len(l)-1):
    l_min = l[i]
    for j in range(x):
        if l_min < l[i+1]:
            l_change = l_min
            l_min = l[i+1]


        x -= 1
print(l)
