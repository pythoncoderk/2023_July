n = int(input())
l = list(map(int, input().split()))
l2 = list(map(int, input().split()))

count = 0
for i in range(n):
    if l[i] == l2[i]:
        count += 1

print(count)