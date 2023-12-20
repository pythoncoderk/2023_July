l = list(map(int, input().split()))
l.sort()
l2 = []
for i in range(len(l)-1):
    l2.append(l[i+1] - l[i])
if l2.count(l2[0]) == len(l2):
    print("Yes")
else:
    print("No")