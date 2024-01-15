l = list(map(int, input().split()))
l.sort()
l2 = []
for i in range(len(l)-1):
    l2.append(l[i+1] - l[i])

x = l2[0]
if l2.count(x) == len(l2):
    print("Yes")
else:
    print("No")