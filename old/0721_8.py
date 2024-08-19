l = list(map(int, input().split()))

# print(l)

l2 = [l.count(l[i]) for i in range(len(l))]

# print(l2)

print("Yes" if l2.count(3) == 3 and l2.count(2) == 2 else "No")