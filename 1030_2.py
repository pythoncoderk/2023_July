import copy

n = int(input())
l = [int(input()) for i in range(n)]
x, y = map(int, input().split())
l2 = copy.copy(l)
l[x - 1] = l2[y -1]
l[y - 1] = l2[x - 1]
for i in l:
    print(i)