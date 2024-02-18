n, m = map(int, input().split())
l = [int(input()) for i in range(n-1)]

# print(n, m)
# print(l)

l2 = [l[i] if l[i] <= m else 0 for i in range(n-1)]
print(sum(l2))

