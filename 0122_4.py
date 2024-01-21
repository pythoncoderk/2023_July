l = list(map(int, input().split()))
l.sort()
l2 = [l[i+1] - l[i] for i in range(len(l)-1)]

if len(l2) == l2.count(l2[0]):
    print("Yes")
else:
    print("No")
