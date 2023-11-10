n = int(input())
l = list(map(int, input().split()))
for i in range(n):
    if l.count(l[i]) >= 2:
        print("Yes")
    else:
        print("No")
