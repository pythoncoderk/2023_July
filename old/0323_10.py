n = int(input())
l = list(map(int, input().split()))

# print(n)
# print(l)

l2 = []
for i in range(n-1):
    x = l[i] * l[i+1]
    l2.append(x)

print(*l2)