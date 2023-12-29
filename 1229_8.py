n = int(input())
l = [int(input()) for i in range(99)]

if sum(l) >= n:
    print(n)
else:
    print(sum(l))