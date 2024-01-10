import sys

n, k = map(int, input().split())
l = [int(input()) for i in range(n)]
# print(n, k)
# print(l)
for i in l:
    if i == k:
        print("YES")
        sys.exit()
print("NO")