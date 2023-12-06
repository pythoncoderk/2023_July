n = int(input())
l = list(map(int, input().split()))
m = int(input())
l2 = []
for i in l:
    if i >= m:
        l2.append(i)
print(min(l2))