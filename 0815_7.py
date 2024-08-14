n = int(input())
l = [int(input()) for i in range(n)]

ans = 999999999999999999999999
l2 = []
for i in range(n):
    diff = 0
    for j in range(i, n):
        if i != j:
            diff = abs(l[i] - l[j])
            if ans > diff:
                ans = diff
                l2 = [l[i], l[j]]

l2.sort()
for i in l2:
    print(i)
