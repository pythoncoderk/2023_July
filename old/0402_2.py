n = int(input())

l = list(map(int, input().split()))

# print(n)
# print(l)

max_l = l[0]
for i in range(n):
    if max_l < l[i]:
        max_l = l[i]
print(max_l)