n = int(input())
l = list(map(int, input().split()))
l = l[::-1]
# print(l)
x = 0
for i in range(n):
    if l[i] % 2 == 1:
        x = i + 1
        break
print(len(l) - x + 1)