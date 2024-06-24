l = list(map(int, input().split()))

# print(l)

l2 = []
for i in range(len(l)):
    x = l.count(l[i])
    l2.append(x)

print("Yes" if 2 in l2 else "No")