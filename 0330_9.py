n, k = map(int, input().split())
l = list(map(int, input().split()))

# print(n, k)
# print(l)

l2 = []
for i in range(len(l)):
    if l[i] % k == 0:
        l2.append(l[i] // k)
print(*l2)
