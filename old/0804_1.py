n = int(input())
l = list(map(int, input().split()))

for i in range(1, n):
    l2 = l[:i]
    if l[i] in l2:
        print("Yes")
    else:
        print("No")