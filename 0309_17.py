n, p, q = map(int, input().split())
l = list(map(int, input().split()))

# print(n, p, q)
# print(l)

l2 = [q + l[i] for i in range(n)]
# print(l2)

l2.append(p)
print(min(l2))