n, k = map(int, input().split())
l = [int(input()) for i in range(n)]
if sum(l) >= k:
    print("No")
else:
    print("Yes")