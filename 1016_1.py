n = int(input())
l1 = list(map(int, input().split()))
l2 = list(map(int, input().split()))

x = 0
for i in range(n):
    if l1[i] == l2[i]:
        x += 1
print(x)