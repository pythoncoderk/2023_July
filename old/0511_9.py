l = list(map(int, input().split()))
l.sort()

# print(l)

l2 = []
for i in range(3-1):
    l2.append(l[i+1] - l[i])

if l2[0] == l2[1]:
    print("Yes")
else:
    print("No")