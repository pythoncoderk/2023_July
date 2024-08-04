n = int(input())
a = [int(x) for x in input().split()]

memo = {a[0]}
for i in range(1, n):
    if a[i] in memo:
        print("Yes")
    else:
        memo.add(a[i])
        print("No")