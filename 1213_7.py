l = [5,4,3,2,1]
min = l[0]
counts = len(l)-1
for i in range(len(l)-1):
    for j in range(counts):
        if min > l[j+1]:
            l[j], min = min, l[j]
        counts -= 1
print(l)
