n = int(input())
l = list(map(int, input().split()))

a = {l[0]}
for i in range(1, n):
    if l[i] in a:
        print("Yes")
    else:
        a.add(l[i])
        print("No")