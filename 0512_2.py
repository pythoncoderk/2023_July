import bisect

n = int(input())
l = list(map(int, input().split()))
m = int(input())
l2 = [int(input()) for i in range(m)]
l.sort()

# print(n)
# print(l)
# print(m)
# print(l2)


for i in range(m):
    print(bisect.bisect_right(l, l2[i]-1))