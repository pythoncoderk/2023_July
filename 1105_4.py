n = int(input())
l = [int(input()) for i in range(7)]
if sum(l) <= n:
    print(sum(l))
else:
    print(n)