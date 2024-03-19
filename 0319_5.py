n, k = map(int, input().split())

l = [int(input()) for i in range(n)]

# print(n, k)
# print(l)

count = 0
for i in range(n):
    if l[i] == k:
        count += 1

if count >= 1:
    print("YES")
else:
    print("NO")