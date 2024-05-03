n, m = map(int, input().split())

l = [int(input()) for i in range(n-1)]

# print(n, m)
# print(l)

l2 = [l[i] for i in range(n-1) if l[i] <= m]

print(sum(l2))